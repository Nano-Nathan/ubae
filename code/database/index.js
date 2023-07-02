const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

// Función para insertar los datos en la base de datos
function createDatabase() {
    // Crear las tablas en la base de datos
    db.serialize(() => {
        db.run('CREATE TABLE nodos (id INTEGER PRIMARY KEY, coordenada_x INTEGER, coordenada_y INTEGER)');
        db.run('CREATE TABLE distancias (id_nodo1 INTEGER, id_nodo2 INTEGER, distancia REAL)');
    });

    // Ruta de los archivos de datos
    const coordenadasFile = './resources/coordenadas';
    const distanciasFile = './resources/distancias';

    // Leer el archivo de coordenadas
    const coordenadasData = fs.readFileSync(coordenadasFile, 'utf8');
    const coordenadasLines = coordenadasData.trim().split('\n');

    // Leer el archivo de distancias
    const distanciasData = fs.readFileSync(distanciasFile, 'utf8');
    const distanciasLines = distanciasData.trim().split('\n');

    // Insertar las coordenadas en la base de datos
    db.serialize(() => {
        db.run('BEGIN TRANSACTION');
        console.log("Insertando nodos...")
        for (const coordenadasLine of coordenadasLines) {
            const [id, coordenada_x, coordenada_y] = coordenadasLine.trim().split(' ');

            db.run('INSERT INTO nodos (id, coordenada_x, coordenada_y) VALUES (?, ?, ?)', [id, coordenada_x, coordenada_y]);
        }

        db.run('COMMIT');
    });

    // Insertar las distancias en la base de datos
    db.serialize(() => {
        db.run('BEGIN TRANSACTION');
        console.log("Insertando distancias...")
        for (const distanciasLine of distanciasLines) {
            const [id_nodo1, id_nodo2, distancia] = distanciasLine.trim().split(' ');
            db.run('INSERT INTO distancias (id_nodo1, id_nodo2, distancia) VALUES (?, ?, ?)', [id_nodo1, id_nodo2, distancia]);
        }
        db.run('COMMIT');
    });
}

// Crear una nueva instancia de la aplicación Express
const app = express();
app.use(express.json());

// Configurar la conexión a la base de datos SQLite
const db = new sqlite3.Database('db/database.sqlite3');

// Verifica si la tabla 'nodos' existe
db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='nodos'", (error, row) => {
    if (error) {
        console.error('Error al verificar la existencia de la base de datos:', error);
        return;
    }

    if (row) {
        console.log('La base de datos existe');
    } else {
        console.log('La base de datos no existe, se genera.');
        // Insertar los datos en la base de datos
        createDatabase();
    }
});

// Endpoint para obtener un único nodo
app.get('/nodo/:id', (req, res) => {
    const nodeId = req.params.id;

    // Obtener el nodo de la base de datos
    db.get('SELECT * FROM nodos WHERE id = ?', [nodeId], (err, row) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ error: 'Error al obtener el nodo' });
        }

        if (!row) {
            return res.status(404).json({ error: 'Nodo no encontrado' });
        }

        res.json(row);
    });
});

// Endpoint para obtener un nodo y sus adyacentes con sus respectivas distancias
app.get('/adyacentes/:id', (req, res) => {
    const nodeId = req.params.id;

    // Obtener el nodo y sus adyacentes de la base de datos
    db.get('SELECT * FROM nodos WHERE id = ?', [nodeId], (err, nodeRow) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ error: 'Error al obtener el nodo' });
        }

        if (!nodeRow) {
            return res.status(404).json({ error: 'Nodo no encontrado' });
        }

        db.all('SELECT * FROM distancias WHERE id_nodo1 = ? or id_nodo2 = ?', [nodeId, nodeId], (err, rows) => {
            if (err) {
                console.error(err);
                return res.status(500).json({ error: 'Error al obtener los nodos adyacentes' });
            }

            const result = rows.map(adjacentNode => {
                object = {
                    distancia: adjacentNode.distancia
                }
                if (adjacentNode.id_nodo1 == nodeId) {
                    object.node = adjacentNode.id_nodo2
                } else {
                    object.node = adjacentNode.id_nodo1
                }
                return object
            })
            /*,a = {
                nodo: nodeRow,
                adyacentes: rows.map(adjacentNode => ({
                    nodo: adjacentNode,
                    distancia: adjacentNode.distancia
                }))
            }*/;

            res.json(result);
        });
    });
});

// Endpoint para obtener la distancia entre dos nodos
app.get('/distancia/:id1/:id2', (req, res) => {
    const id1 = req.params.id1;
    const id2 = req.params.id2;

    // Obtener la distancia entre los dos nodos de la base de datos
    db.get('SELECT distancia FROM distancias WHERE (id_nodo1 = ? AND id_nodo2 = ?) OR (id_nodo1 = ? AND id_nodo2 = ?)', [id1, id2, id2, id1], (err, row) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ error: 'Error al obtener la distancia' });
        }

        if (!row) {
            return res.status(404).json({ error: 'Distancia no encontrada' });
        }

        res.json(row);
    });
});

// Iniciar el servidor en el puerto 3000
app.listen(3000, () => {
    console.log('Servidor iniciado en el puerto 3000');
});

// Agrega un evento para el cierre del servidor
process.on('SIGINT', () => {
    console.log('Servidor finalizado');
    // Cerrar la conexión con la base de datos
    db.close();
    process.exit(0);
});
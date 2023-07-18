const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const readline = require('readline');

// Crear una nueva instancia de la aplicación Express
const app = express();
app.use(express.json());

// Configurar la conexión a la base de datos SQLite
const db = new sqlite3.Database('db/database.sqlite3');

// Crear las tablas en la base de datos
db.serialize(() => {
    db.run('CREATE TABLE IF NOT EXISTS nodos (id INTEGER PRIMARY KEY, coordenada_x INTEGER, coordenada_y INTEGER)');
    db.run('CREATE TABLE IF NOT EXISTS distancias (id_nodo1 INTEGER, id_nodo2 INTEGER, distancia REAL)');
});

// Función para insertar los datos en la base de datos
async function createDatabase() {
    //Metodo para insertar datos
    var insertData = (RL, table, columns) => {
        var //splitter = 0,
            columnsParsed = columns.join(","),
            values = "?".repeat(columns.length).split("").join(",");
        console.log(`Insertando ${table}...`)
        console.log("Begin transaction")
        db.run('BEGIN TRANSACTION');
        db.serialize(() => {
            RL.on('line', (linea) => {
                db.run(`INSERT INTO ${table} (${columnsParsed}) VALUES (${values})`, linea.trim().split(' '), (err) => { if (err && err.errno != 19) console.log(err) });
            });
        })
        return new Promise((resolve, reject) => {
            RL.on('close', () => {
                console.log("End commit")
                resolve()
                db.run('COMMIT', (err) => {
                    if (err) {
                        console.error(`Error al insertar ${table}:`, err);
                        reject(err);
                    } else {
                        console.log(`Inserción de ${table} completada.`);
                        resolve();
                    }
                });
            });
        });
    }

    // Ruta de los archivos de datos
    const coordenadasFile = './resources/coordenadas';
    const distanciasFile = './resources/distancias';

    // Leer el archivo de coordenadas
    const coordenadasStream = fs.createReadStream(coordenadasFile);
    const coordenadasRl = readline.createInterface({
        input: coordenadasStream,
        crlfDelay: Infinity
    });
    await insertData(coordenadasRl, "nodos", ['id', 'coordenada_x', 'coordenada_y']);

    // Leer el archivo de distancias
    const distanciasStream = fs.createReadStream(distanciasFile);
    const distanciasRl = readline.createInterface({
        input: distanciasStream,
        crlfDelay: Infinity
    });
    await insertData(distanciasRl, "distancias", ['id_nodo1', 'id_nodo2', 'distancia']);
}

// Verifica si la tabla 'nodos' existe
db.get("SELECT COUNT(*) AS count FROM distancias", (error, row) => {
    if (error) {
        console.error('Error al verificar la existencia de la base de datos:', error);
        return;
    }

    if (row.count) {
        console.log('La base de datos existe');
    } else {
        console.log('La base de datos no existe, se genera.');
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
            });

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
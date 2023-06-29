-- Crear la tabla "nodos"
CREATE TABLE nodos (
  id INTEGER PRIMARY KEY,
  coordenada_x INTEGER,
  coordenada_y INTEGER
);

-- Insertar los datos de nodos
INSERT INTO nodos (id, coordenada_x, coordenada_y)
VALUES
  (1, -73530767, 41085396),
  (2, -73530538, 41086098),
  (3, -73519366, 41048796),
  (4, -73519377, 41048654),
  (5, -73524567, 41093796),
  (6, -73525490, 41093834),
  (7, -73531927, 41110484),
  (8, -73530106, 41110611);

-- Crear la tabla "distancias"
CREATE TABLE distancias (
  id_nodo1 INTEGER,
  id_nodo2 INTEGER,
  distancia INTEGER,
  PRIMARY KEY (id_nodo1, id_nodo2)
);

-- Insertar los datos de distancias
INSERT INTO distancias (id_nodo1, id_nodo2, distancia)
VALUES
  (1, 2, 803),
  (2, 1, 803),
  (3, 4, 158),
  (4, 3, 158),
  (5, 6, 774),
  (6, 5, 774),
  (7, 8, 1531),
  (8, 7, 1531);

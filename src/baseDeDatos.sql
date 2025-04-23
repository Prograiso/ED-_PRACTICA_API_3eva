
CREATE TABLE coche (
    matricula TEXT PRIMARY KEY,
    marca TEXT,
    modelo TEXT,
    color TEXT,
    precio REAL,
    stock INTEGER,
    kilometros INTEGER
);


INSERT INTO coche (matricula, marca, modelo, color, precio, stock, kilometros) VALUES
('ABC1234', 'Toyota', 'Corolla', 'Blanco', 22500, 15, 32000),
('DEF5678', 'Ford', 'Mustang', 'Rojo', 36000, 5, 18500),
('GHI9012', 'Honda', 'Civic', 'Gris', 24000, 10, 27200),
('JKL3456', 'Chevrolet', 'Camaro', 'Negro', 40500, 3, 15000),
('MNO7890', 'Nissan', 'Sentra', 'Azul', 21000, 12, 34800),
('PQR2345', 'BMW', 'Serie 3', 'Plata', 45000, 4, 22300),
('STU6789', 'Audi', 'A4', 'Blanco', 47000, 6, 19900),
('VWX0123', 'Hyundai', 'Elantra', 'Rojo', 20000, 20, 41600),
('YZA4567', 'Kia', 'Forte', 'Azul', 19500, 18, 38700),
('BCD8901', 'Volkswagen', 'Jetta', 'Negro', 23000, 9, 29400);

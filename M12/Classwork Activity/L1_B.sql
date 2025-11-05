CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_ID TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commission REAL
);

INSERT INTO Salesman (Salesman_ID, name, city, commission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'Paris', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12);

SELECT * FROM Salesman;

SELECT * FROM Salesman
WHERE city == "Paris";

CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('70001', 150.5, '2012-10-05', '3005', '5002'),
('70009', 270.65, '2012-09-10', '3001', '5005'),
('70002', 65.26, '2012-10-05', '3002', '5001'),
('70004', 110.5, '2012-08-17', '3004', '5003'),
('70007', 948.5, '2012-09-10', '3007', '5002');

SELECT * FROM Orders;

SELECT name, commission FROM Salesman;

SELECT * FROM Salesman
WHERE commission < 0.14 AND commission > 0.11 AND city == "Paris";

SELECT * FROM Salesman
WHERE NOT name LIKE "%A%";
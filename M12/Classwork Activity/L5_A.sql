CREATE TABLE IF NOT EXISTS Salesman (
    SALESMAN_ID TEXT PRIMARY KEY,
    NAME TEXT,
    CITY TEXT,
    COMMISSION REAL
);

INSERT INTO Salesman (SALESMAN_ID, NAME, CITY, COMMISSION) VALUES
    ('5001', 'James Hoog', 'New York', 0.15),
    ('5002', 'Nail Knite', 'Paris', 0.13),
    ('5005', 'Pit Alex', 'London', 0.11),
    ('5006', 'Mc Lyon', 'Paris', 0.14),
    ('5007', 'Paul Adam', 'Rome', 0.13),
    ('5003', 'LauSon Hen', 'San Jose', 0.12);

CREATE TABLE IF NOT EXISTS Customer (
    CUSTOMER_ID TEXT,
    CUST_NAME TEXT PRIMARY KEY,
    CITY TEXT,
    GRADE INTEGER,
    SALESMAN_ID TEXT,
    FOREIGN KEY (SALESMAN_ID) REFERENCES Salesman(SALESMAN_ID)
);

INSERT INTO Customer (CUSTOMER_ID, CUST_NAME, CITY, GRADE, SALESMAN_ID) VALUES
    ('3002', 'nick rimando', 'New York', 100, '5001'),
    ('3007', 'brad davis', 'New York', 200, '5001'),
    ('3005', 'graham zusi', 'California', 200, '5002'),
    ('3008', 'julian green', 'London', 300, '5004'),
    ('3004', 'fabian johnson', 'Paris', 300, '5006'),
    ('3009', 'geoff cameron', 'Berlin', 100, '5003'),
    ('3003', 'jozy altidor', 'Moscow', 200, '5007'),
    ('3001', 'brad guzan', 'London', NULL, '5005');

CREATE TABLE IF NOT EXISTS Orders (
    ORDER_NUM TEXT PRIMARY KEY,
    PURCHASE_AMOUNT REAL,
    ORDER_DATE TEXT,
    CUSTOMER_ID TEXT,
    SALESMAN_ID TEXT,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID),
    FOREIGN KEY (SALESMAN_ID) REFERENCES Salesman(SALESMAN_ID)
);

INSERT INTO Orders (ORDER_NUM, PURCHASE_AMOUNT, ORDER_DATE, CUSTOMER_ID, SALESMAN_ID) VALUES
    ('70001', 150.5, '2012-10-05', '3005', '5002'),
    ('70009', 270.65, '2012-09-10', '3001', '5001'),
    ('70002', 65.26, '2012-10-05', '3002', '5003'),
    ('70004', 110.5, '2012-08-17', '3009', '5007'),
    ('70007', 948.5, '2012-09-10', '3005', '5005'),
    ('70005', 2400.6, '2012-07-27', '3007', '5006');
  

SELECT * FROM Customer;
SELECT * FROM Salesman;
SELECT * FROM Orders;

SELECT Customer.CUST_NAME, Salesman.NAME, Salesman.CITY
FROM Customer
JOIN Salesman ON Customer.CITY = Salesman.CITY;

SELECT Customer.CUST_NAME, Salesman.NAME
FROM Customer
LEFT JOIN Salesman ON Customer.SALESMAN_ID = Salesman.SALESMAN_ID;

SELECT Orders.ORDER_NUM, Customer.CUST_NAME, Orders.CUSTOMER_ID, Orders.SALESMAN_ID
FROM Orders
JOIN Customer ON Orders.CUSTOMER_ID = Customer.CUSTOMER_ID
JOIN Salesman ON Orders.SALESMAN_ID = Salesman.SALESMAN_ID
WHERE Customer.CITY <> Salesman.CITY;

SELECT Orders.ORDER_NUM, Customer.CUST_NAME
FROM Orders
JOIN Customer ON Orders.CUSTOMER_ID = Customer.CUSTOMER_ID;

SELECT Customer.CUST_NAME AS "Customer", Customer.GRADE AS "Grade"
FROM Orders
JOIN Salesman ON Orders.SALESMAN_ID = Salesman.SALESMAN_ID
JOIN Customer ON Orders.CUSTOMER_ID = Customer.CUSTOMER_ID
WHERE Customer.GRADE IS NOT NULL;

SELECT Customer.CUST_NAME AS "Customer",
Customer.CITY AS "City",
Salesman.NAME AS "Salesman",
Salesman.COMMISSION
FROM Customer
JOIN Salesman ON Customer.SALESMAN_ID = Salesman.SALESMAN_ID
WHERE Salesman.COMMISSION BETWEEN 0.12 AND 0.14;

SELECT Orders.ORDER_NUM, Customer.CUST_NAME, Salesman.COMMISSION AS "Commission%",
Orders.PURCHASE_AMOUNT * Salesman.COMMISSION AS "Commission"
FROM Orders
JOIN Customer ON Orders.SALESMAN_ID = Salesman.SALESMAN_ID
JOIN Salesman ON Orders.CUSTOMER_ID = Customer.CUSTOMER_ID
WHERE Customer.GRADE >= 200;

SELECT *
FROM Customer
JOIN Orders ON Customer.CUSTOMER_ID = Orders.CUSTOMER_ID
WHERE Orders.ORDER_DATE = '2012-10-05';
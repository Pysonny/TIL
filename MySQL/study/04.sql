CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userID INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
	users(name)
VALUES
	('권미자'),
    ('류준하'),
    ('정영식');

INSERT INTO
	articles(title,content,userId)
VALUES
	('제목1','내용1',1),
    ('제목2','내용2',2),
    ('제목3','내용3',4);

SELECT
	title,content,name
FROM
	articles
INNER JOIN
	users
ON
	articles.userId = users.id;

SELECT
	productCode,productName,textDescripsion
FROM
	products
INNER JOIN
	productlines
ON
	products.productLine = productlines.productLine;

SELECT
	orders.orderNumber, status, sum(quantityOrdered * priceEach) AS totalSales
FROM
	orders
INNER JOIN
	orderdetails
ON
	orders.orderNumber=orderdetails.orderNumber
GROUP BY
	orders.orderNumber;
    
SELECT
	*
FROM
	articles
LEFT JOIN users
	ON articles.userId = users.id;
    
SELECT
	contactFirstName,orderNumber,status
FROM
	customers

LEFT JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber IS NULL;

SELECT
	employeeNumber,firstName, customerNumber,contactFirstName
FROM
	customers
RIGHT JOIN employees
ON employees.employeeNumber = customers.salesRepEmployeeNumber
WHERE 
	customerNumber IS NULL;

SELECT * FROM users;
SELECT * FROM articles;
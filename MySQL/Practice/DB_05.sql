# 문제 1
# 테이블 employees 과 테이블 offices 를 officeCode 기준으로 INNER JOIN 한 데이터를 조회하시오.


SELECT
	employeeNumber,lastName,firstName,city
FROM
	employees
INNER JOIN
	offices
On
	offices.officeCode = employees.officeCode
ORDER BY
	employeeNumber;
    
    
# 문제 2
# 테이블 customers 와 테이블 offices 를 city 기준으로 LEFT JOIN 한 데이터를 조회하시오.

SELECT
	customerNumber , officeCode, customers.city,offices.city
FROM
	customers
LEFT JOIN
	offices
ON
	 customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
    
# 문제 3
# 테이블 customers 와 테이블 offices 를 city 기준으로 RIGHT JOIN 한 데이터를 조회하시오.

SELECT
	customerNumber,officeCode, customers.city , offices.city
FROM
	customers
RIGHT JOIN
	offices
ON
	customers.city = offices.city
ORDER BY
	customerNumber DESC;
    

# 문제 4
# 테이블 customers 와 테이블 offices 를 city 기준으로 INNER JOIN 한 데이터를 조회하시오.

SELECT
	customerNumber,officeCode,customers.city , offices.city
FROM
	customers
INNER JOIN
	offices
ON
	customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
# 문제 5
# 문제 2, 문제 3, 문제 4 의 조회 결과가 다른 이유를 작성하시오.

## customers = A , offices = B 일 때,
## 2번은 A 와 A와B가 겹치는 부분을 포함하여 보여주고
## 3번은 B 와 B와A가 겹치는 부분을 포함하여 보여주고
## 4번은 A와 B의 교집합을 보여준다

# 문제 6
# 테이블 customers 와 테이블 offices 를 city 기준으로 FULL OUTER JOIN 한 데이터를 조회하시오.

SELECT
	customerNumber,officeCode,customers.city , offices.city
FROM
	customers
LEFT JOIN
	offices
ON
	 customers.city = offices.city
UNION
SELECT
	customerNumber,officeCode, customers.city , offices.city
FROM
	customers
RIGHT JOIN
	offices
ON
	customers.city = offices.city
ORDER BY
	customerNumber DESC;


# 문제 7 
# 테이블 orderdetails 와 테이블 orders 를 INNER JOIN 한 데이터를 조회하시오.
SELECT 
	orders.orderNumber,orders.orderDate
FROM
	orderdetails
INNER JOIN
	orders
ON
	orders.orderNumber = orderdetails.orderNumber
ORDER BY
	orderNumber ;
    
SELECT * FROM orderdetails;
SELECT * FROM products;


# 문제 8
# 테이블 orderdetails 와 테이블 products 을 INNER JOIN 한 데이터를 조회하시오.

SELECT
	orderdetails.orderNumber , products.productCode , products.productName
FROM
	orderdetails
INNER JOIN
	products
ON
	products.productCode = orderdetails.productCode
ORDER BY
	orderNumber;
    

# 문제 9
# 테이블 orderdetails , 테이블 orders , 테이블 products 를 INNER JOIN 한 데이터를 조회하시오.

SELECT
	orders.orderNumber,
    products.productCode,
    orders.orderDate,
    products.productName
FROM
	orderdetails,orders,products
WHERE 
	orders.orderNumber = orderdetails.orderNumber AND
    orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;
    
    
SELECT * FROM orderdetails;
SELECT * FROM products;
SELECT * FROM orders;
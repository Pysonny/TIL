
# 문제 1
# 테이블 products 에서 평균 MSRP 보다 큰 product 의 productCode , productName , MSRP 를 조회하시오.
# 단, MSRP 기준 오름차순으로 정렬하세요.

SELECT
	productCode,productName,MSRP
FROM
	products
WHERE MSRP > (
    SELECT
		AVG(MSRP)
	FROM
		products
)
ORDER BY
	MSRP;


# 문제 2
# 테이블 customers 에서 2003년 1월 6일과 2003년 3월 26일 사이에 주문(order)을 한 고객의 customerNumber, customerName 를 조회하시오.

	## customerNumber 가 동일하네
SELECT
    customerNumber,customerName #4. customerNumber 랑 customerName 을 보여줘라
FROM 
	customers       	#3. customers 안에 있는
WHERE					#2. 중에서
	customerNumber IN ( #1. orders 안에 있는 customerNumber 중 지정된 날짜 안에 있는 것들
    SELECT
		customerNumber
	FROM
		orders
    WHERE
		orderDate BETWEEN '2003-01-06' AND '2003-03-26'
	)
ORDER BY
	customerNumber;

    
SELECT * FROM orders;
SELECT * FROM customers;


# 문제 3
# 테이블 customers 에서 2003년 1월 6일과 2003년 3월 26일 사이에 주문(order)을 한 고객의 customerNumber, customerName 를 조회하시오.

SELECT
	productCode,productName,productLine,MSRP # 3. 조회할 항목들을 출력해준다
FROM
	products			#2. products 안에서 
WHERE MSRP = (			#1. productLine 이름이 Classic cars 인 제품 중에서 MSRP 가 제일 큰 것을
	SELECT
		MAX(MSRP)
	FROM
		products
	WHERE
		productLine = 'Classic Cars'
);
		


SELECT * FROM products;
SELECT * FROM productLines;


# 문제 4
# 가장 많은 고객(customer)이 사는 나라(country)의 customerNumber , customerName , country 를 조회하시오.
# 단, customerNumber 기준 오름차순으로 정렬하세요

SELECT 
	customerNumber , customerName , country  #3. 조회할 목록을 골라 출력시킨다
FROM
	customers 			#2. 고객중에서 
WHERE 
	country = (			#1. 고객 중에서 제일 많은 나라가 가장 많은 고객이 사는 나라 임으로
						#	내림차순하고 제일 위에 것을 빼면 사람이 제일 많은 나라가 나온다
    SELECT
		MAX(country)
	FROM
		customers
	GROUP BY
		country
	ORDER BY
		country DESC
	LIMIT 1
)
ORDER BY
	customerNumber;
    
SELECT * FROM orders;
SELECT * FROM customers;
# 문제 5
# 가장 많은 주문(order)을 한 고객(customer)의 customerNumber , customerName , 주문 수(order_count) 를 조회하시오.
# 고객 데이터는 customers 테이블, 주문 테이블은 orders 테이블을 활용합니다.

# order_count 는 테이블 안에 없다

SELECT
	customerNumber, customerName, order_count
FROM
	customers
INNER JOIN (
	SELECT
		customerNumber, COUNT(customerNumber) AS order_count
	FROM
		orders
	GROUP BY
		customerNUmber
    ORDER BY
		order_count DESC
	LIMIT 1 
) AS sub
USING 
	(customerNumber)
ORDER BY
	order_count DESC
;

SELECT * FROM orders;
SELECT * FROM orderdetails; # orderNumber 로 
SELECT * FROM products; # prodectCode 로
# 문제 6
# 주문 날짜(orderDate)가 2004년인 주문(orderdetail) 제품(product)의 productCode , productName 를 조회하시오.
# 주문 날짜 데이터는 orders 테이블, 주문 - 제품 데이터는 orderdetails 테이블, 제품 데이터는 products 테이블을 활용합니다.
# 단, productCode 기준 내림차순으로 정렬하세요.

SELECT DISTINCT
	productCode, productName
FROM
	orders
INNER JOIN orderdetails USING (orderNumber)
INNER JOIN products USING (productCode)
WHERE 
	orderDate LIKE '2004%'
ORDER BY
	productCode DESC;
		
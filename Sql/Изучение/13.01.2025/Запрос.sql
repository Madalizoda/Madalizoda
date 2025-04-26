SELECT 
	p.title,
	dt,
	dt + INTERVAL 10 MINUTE ,
	CURDATE(),
	DATEDIFF(CURDATE(),dt)
FROM income i INNER JOIN product p 
ON i.product_id = p.id
WHERE p.title = "Зикруллохон"


SELECT * 
FROM category c 
WHERE c.title = "Хлебобулочные изделия"


SELECT 
	p.id ,
	p.title product_title,
	dt,
	i.price ,
	i.amount ,
	i.price * i.amount AS cost,
	p.ctgry_id,
	c.title category_title
FROM income i 
INNER JOIN product p 
	ON i.product_id = p.id
INNER JOIN category c 
	ON p.ctgry_id = c.id
WHERE c.title = "Хлебобулочные изделия"
ORDER BY i.product_id 



SELECT 
	c.title category_title,
	sum(i.price * i.amount) AS cost	
FROM income i 
INNER JOIN product p 
	ON i.product_id = p.id
INNER JOIN category c 
	ON p.ctgry_id = c.id
WHERE c.title = "Хлебобулочные изделия"
GROUP BY c.title

SELECT SUM(amount*price) AS income_sum
FROM product AS a
INNER JOIN income AS b 
ON a.id = b.product_id 
WHERE ctgry_id = (SELECT id FROM category WHERE title = "Хлебобулочные изделия")




SELECT i.product_id FROM income i 
UNION 
SELECT o.product_id FROM outcome o;


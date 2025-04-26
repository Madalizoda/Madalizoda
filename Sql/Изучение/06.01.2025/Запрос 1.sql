SELECT 
	p.title, 
	LEFT(p.title,3) AS LEFT3, 
	RIGHT(p.title,3) AS RIGHT3 
FROM product p 
ORDER BY p.title

SELECT 
	p.title, 
	LEFT(p.title,3) AS LEFT3, 
	RIGHT(p.title,3) AS RIGHT3, 
	CONCAT(LEFT(p.title,3),  ' | ' , RIGHT(p.title,3)) left_right 
FROM product p 
ORDER BY p.title


SELECT 
	c.title ctgr_name,
	p.title prdct_name,
	CONCAT(c.title, ' | ', p.title) ctgr_prdc
FROM product p , category c
WHERE p.ctgry_id = c.id 
ORDER BY c.title, p.title

SELECT 
	p.title,
	UPPER(p.title) AS ALL_upper,
	LOWER(p.title) AS ALL_LOWER
FROM product p
ORDER BY p.title


SELECT 
	c.title ctgr_name,
	p.title prdc_name
FROM category c , product p
WHERE c.id = p.ctgry_id
AND UPPER(LEFT(c.title,3)) = UPPER(LEFT(p.title,3))



SELECT 
	upper(CONCAT(LEFT(c.title,4), '_', LEFT(p.title,4)))
FROM category c, product p
WHERE c.id = p.ctgry_id



SELECT 
	p.title,
	length(p.title),
	CHAR_LENGTH(p.title)
FROM product p


SELECT CURDATE(), CURTIME(), NOW()


SELECT dt, TIME(dt), YEAR(dt), MONTH(dt), DAY(dt)
FROM income


SELECT 
	dt,
	DATE_ADD(dt, INTERVAL 29 DAY),
	DATE_SUB(dt, INTERVAL 3 MONTH),
	DATE_SUB(DATE_ADD(dt,INTERVAL 3 MONTH), INTERVAL 1 DAY)

FROM income

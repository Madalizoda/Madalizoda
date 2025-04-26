SELECT
	dt,
	CURDATE(),
	DATEDIFF(CURDATE(), dt)
FROM income


SELECT
	p.title,
	i.dt,
	DATEDIFF(CURDATE(), i.dt)
FROM income i, product p
WHERE i.product_id = p.id AND i.product_id = 12


SELECT CURDATE(), "2025-12-12"
SELECT DATE_ADD("2024-12-14",INTERVAL 28 DAY)

SELECT 
	CURtime(), 
	CURTIME() + INTERVAL 10 MINUTE AS add_10_min,
	CURTIME() + INTERVAL 100 HOUR AS add_100_hour,
	CURTIME() - INTERVAL 10 MINUTE AS sub_10_min,
	CURTIME() - INTERVAL 100 HOUR AS sub_100_hour,
	now() + INTERVAL 10 MINUTE AS add_10_min,
	now() + INTERVAL 100 HOUR AS add_100_hour,
	now() - INTERVAL 10 MINUTE AS sub_10_min,
	now() - INTERVAL 100 HOUR AS sub_100_hour
		
		

SELECT *
FROM income i
WHERE  month(i.dt) = 6



SELECT *, day(i.dt) AS day
FROM income i
WHERE  day(i.dt) <= 10
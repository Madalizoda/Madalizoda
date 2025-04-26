SELECT * FROM income
SELECT product_id FROM income
SELECT DISTINCT product_id FROM income
SELECT DISTINCT product_id FROM income ORDER BY product_id
SELECT DISTINCT product_id FROM income ORDER BY product_id desc

SELECT product_id FROM income GROUP BY product_id

SELECT * FROM income ORDER BY price


SELECT * FROM income 
SELECT * FROM income ORDER BY dt, price DESC
SELECT * FROM income ORDER BY dt DESC, price

SELECT * FROM income WHERE amount > 200
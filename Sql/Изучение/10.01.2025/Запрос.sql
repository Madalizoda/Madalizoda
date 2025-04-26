CREATE DATABASE shop_online


CREATE TABLE if NOT EXISTS `category` (
`id` INT(11) NOT NULL AUTO_INCREMENT, 
`title` VARCHAR(30) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE = INNODB DEFAULT CHARSET = UTF8;


INSERT INTO category SET title = 'Бытовая химия'
-- INSERT INTO `category` (`title`) VALUES (`Бытовая химия`)
INSERT INTO category SET title = 'Дум шурбо'

UPDATE category SET title = 'Бытовая техника' WHERE id= 3;
COMMIT;


DELETE FROM category WHERE id = 3


DELETE category

TRUNCATE TABLE category

DROP TABLE category
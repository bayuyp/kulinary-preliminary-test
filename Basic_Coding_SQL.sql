create table user_review (
id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
order_id VARCHAR(15),
product_id VARCHAR(15),
user_id VARCHAR(15),
rating FLOAT(2,1),
review TEXT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
);

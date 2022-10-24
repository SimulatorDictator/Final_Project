CREATE TABLE IF NOT EXISTS Games (
        gid INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(30) 
);
CREATE TABLE IF NOT EXISTS Customers (
        cid INT PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(30),
        table INT,
        fk_gid INT, 
        FOREIGN KEY (fk_gid) REFERENCES Games(id)
);

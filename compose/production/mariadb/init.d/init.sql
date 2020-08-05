CREATE DATABASE IF NOT EXISTS blog
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

# use blog;
#
# CREATE TABLE IF NOT EXISTS tasks
# (
#     task_id     INT AUTO_INCREMENT PRIMARY KEY,
#     title       VARCHAR(255) NOT NULL,
#     start_date  DATE,
#     due_date    DATE,
#     status      TINYINT      NOT NULL,
#     priority    TINYINT      NOT NULL,
#     description TEXT,
#     created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# ) ENGINE = INNODB;
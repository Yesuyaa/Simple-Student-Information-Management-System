USE studentInfoM;

-- 删除已存在的表
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS user;

-- 创建学生表
CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(80) NOT NULL,
    age INT,
    gender VARCHAR(10),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME
) COMMENT='学生信息表';

-- 创建用户表
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(120) NOT NULL
) COMMENT='用户表';

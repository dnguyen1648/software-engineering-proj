DROP DATABASE IF EXISTS EncryptionDatabase;
CREATE DATABASE EncryptionDatabase;

DROP TABLE IF EXISTS Company;
CREATE TABLE Company (
    companyID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	companyName VARCHAR(100),
    companyPublicKey VARCHAR(100) UNIQUE,
    FOREIGN KEY (SettingsID)
        REFERENCES Settings (SettingsID)
);

DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
    employeeID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	firstName VARCHAR(100),
	lastName VARCHAR(100),
    email VARCHAR(100),
    hashedPassword VARCHAR(100),
    FOREIGN KEY (companyID)
        REFERENCES Company (comapnyID)
);

DROP TABLE IF EXISTS Admins;
CREATE TABLE Admins (
    adminID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    hashedPassword VARCHAR(100),
    FOREIGN KEY (companyID)
        REFERENCES Company (comapnyID)
);

DROP TABLE IF EXISTS Settings;
CREATE TABLE Settings (
    settingsID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	keySize INT,
    passwordLength INT,
    daysUntilPublicKeyRefereshes INT
);






CREATE TABLE IF NOT EXISTS `financial_data` (
    `Company_Name` VARCHAR(255),
    `Company_Website` VARCHAR(255),
    `Exchange_Ticker` VARCHAR(10),
    `HQ_Country` VARCHAR(50),
    `HQ_State` VARCHAR(50),
    `HQ_City` VARCHAR(50),
    `HQ_Address` VARCHAR(255),
    `Industry_Category` VARCHAR(255),
    `Market_Cap_Billion` DECIMAL(18, 2),
    `Net_Income_Billion` DECIMAL(18, 2),
    `Number_of_Employees` INT,
    `Sales_Billion` DECIMAL(18, 2),
    `Sector` VARCHAR(255),
    `Ticker` VARCHAR(10),
    `Market_Cap_Billion_Dollars` DECIMAL(18, 2),
    `Net_Income_Billion_Dollars` DECIMAL(18, 2),
    `Sales_Billion_Dollars` DECIMAL(18, 2)
) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE company_table (id SERIAL PRIMARY KEY, company_name VARCHAR(255),
                            company_sector VARCHAR(255));

CREATE TABLE employee_table (id SERIAL PRIMARY KEY,
                             first_name VARCHAR(255),
                             last_name VARCHAR(255),
                             company VARCHAR(255),
                             title VARCHAR(255),
                             salary NUMERIC(100,2));

INSERT INTO company_table (company_name, company_sector)
     VALUES ('Valero Energy Corporation', 'Oil & Gas Refining & Marketing'),
            ('The Home Depot', 'Home Improvement Stores'), ('Wal-Mart Stores', 'Discount'),
            ('Alphabet', 'Internet Information Providers');

INSERT INTO employee_table (first_name, last_name, company, title, salary)
     VALUES ('Bob', 'Ross', 'Valero Energy Corporation', 'Benefits Officer', 134567.95),
            ('Jim', 'Clark', 'The Home Depot', 'Sales Representitive', 25678.53),
            ('Susan', 'Tilly', 'Valero Energy Corporation', 'Cheif Financial Officer', 1875478.78),
            ('Chuck', 'Wallace', 'Wal-Mart Stores', 'Overnight Stocker', 89478.02),
            ('Mark', 'Freeman', 'Wal-Mart Stores', 'Store Manager', 356873.23),
            ('Larry', 'Page', 'Alpabet', 'Cheif Executive Officer', 29234596536.84);

SELECT (et.id, et.first_name, et.last_name, et.company, ct.company_industry, et.title, et.salary)
  FROM company_table ct, employee_table et
 WHERE ct.company_name = et.company;


employee_id, employee_firstname, employee_lastname, company_name, company_industry, title, salary

(3,Susan,Tilly,"Valero Energy Corporation","Oil & Gas Refining & Marketing","Cheif Financial Officer",1875478.78)
(1,Bob,Ross,"Valero Energy Corporation","Oil & Gas Refining & Marketing","Benefits Officer",134567.95)
(2,Jim,Clark,"The Home Depot","Home Improvement Stores","Sales Representitive",25678.53)
(5,Mark,Freeman,"Wal-Mart Stores",Discount,"Store Manager",356873.23)
(4,Chuck,Wallace,"Wal-Mart Stores",Discount,"Overnight Stocker",89478.02)

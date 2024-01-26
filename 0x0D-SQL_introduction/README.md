Introduction to database management.

learning SQL - mysql


------CONCEPT------
disadvantage of storing data in application is data dies when server stops.

features of a solid database
A- atomicity
C- Consistency
I- Isolation
D- Durability


A database should allow all these four;
C: Create some data
R: Read some data
U: Update some data
D: Destroy some data


--------SQL--------
Sql stands for structured query lamguage and it is the query for most relational databases like mysql and oracle


SQL statements are divided into two major categories:
- data definition language (DDL)
- data manipulation language (DML).

..........DDL..........
- DDL statements are used to build and modify the structure of your tables and other objects in the database. when you execute a DDL command, it takes effect immediately.

*****example: to create a table:
	CREATE TABLE <table name> (attribute name 1> <data type 1), 
	...
	<attribute name n> <data type n>);

- data types: VARCHAR, CHAR, NUMBER, INTEGER, DATE.

*****example: alter table:
	ALTER TABLE <table name>
	ADD CONSTRAINT <constraint name> PRIMARY KEY (<attribute list>);


	ALTER TABLE <table name>
	ADD CONSTRAINT <constraint name> FOREIGN KEY (<attribute list>)
	REFERENCES <parent table name> (<attribute list>);

	DROP TABLE <table name>;

	ALTER TABLE <table name>
	DROP CONSTRAINT <constraint namr>;



.............DML.............
DML statements are used to work with the data in tables. 


- SELECT;

- insert statement:
	INSERT INTO <table name>
	VALUES (<value 1>, ... <value n>);

- update statement:
	UPDATE <table name>
	SET <attribute> = <expression>
	WHERE <condition>;

- delete statement:
	DELETE FROM <table name>
	WHERE <condition>;


- ROLLBACK; (only works before you COMMIT;)


______________RETRIEVING DATA FROM ONE TABLE______________

- SELECT - To retrieve data stored in our tables.
(syntax):
	SELECT {attribute}+
	FROM {table}+
	[ WHERE {boolean predicate to pick rows} ]
	[ ORDER BY {attribute}+ ];



############TECHNIQUE: SUBQUERIES#########
	SELECT cFirstName, cLastName
	FROM customers
	WHERE cZipCode =
	 (SELECT cZipCode
	  FROM customers
	  WHERE cFirstName = 'Wayne' AND cLastname = 'Dick') 
A subquery that returns only one column and one row can be used any time that we need a single value.



############TECHNIQUE: FUNCTIONS#############
Computed Columns: We can values from information that is in a table simply by showing the computation in the SELECT clause.

	SELECT custID, orderDate, UPC, unitSalePrice * quantity
	FROM orderlines;
- We can create our own column heading or alias using the keyword `AS`
	SELECT custID, orderDate, UPC,
	  unitSalePRice * quantity AS subtotal
	FROM orderlines;

-- AGGREGATE FUNCTIONS --
SQL aggregate functions let us compute values based on multiple rows in our tables. They are also used as part of the SELECT clause, and also create new columns in the output.
- SUM
	SELECT SUM( unitSalePrice * quantity) AS totalsales
	FROM orderllines;
- GROOUP BY
	SELECT custID, orderDate, SUM(uniSalePRice * quantity) AS total
	FROM orderlines
	GROUP BY custID, orderDate;
- MIN - Minimum value of those in the grouping
- MAX - Maximum value of thosse in the grouping
- AVG - Average value of those in the grouping
- COUNT - Returns number of rows in a grouping.
	SELECT COUNT(*)
	FROM orders;
- HAVING
	SELECT prodname AS "product name",
	  COUNT(prodname) AS "times ordered"
	FROM products NATURAL JOIN orderlines
	GROUP BY prodname
	HAVING COUNT(prodname) > 1;

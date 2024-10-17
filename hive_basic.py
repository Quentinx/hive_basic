(base) [train@trainvm ~]$ docker exec -it cluster-master bash
root@cluster-master:/dataops# $HIVE_HOME/bin/beeline -u jdbc:hive2://localhost:10000
0: jdbc:hive2://localhost:10000> create database hive_odev;
0: jdbc:hive2://localhost:10000> USE hive_odev;
CREATE TABLE wine (
  Alcohol FLOAT,
  Malic_Acid FLOAT,
  Ash FLOAT,
  Alcalinity_Of_Ash FLOAT,
  Magnesium INT,
  Total_Phenols FLOAT,
  Flavanoids FLOAT,
  Nonflavanoid_Phenols FLOAT,
  Proanthocyanins FLOAT,
  Color_Intensity FLOAT,
  Hue FLOAT,
  OD280_OD315 FLOAT,
  Proline INT
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
0: jdbc:hive2://localhost:10000> SHOW TABLES;
INFO  : Compiling command(queryId=root_20241003184636_db9fe030-39a7-48ba-bfb5-59f8fb5297b8): SHOW TABLES
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=root_20241003184636_db9fe030-39a7-48ba-bfb5-59f8fb5297b8); Time taken: 0.014 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=root_20241003184636_db9fe030-39a7-48ba-bfb5-59f8fb5297b8): SHOW TABLES
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=root_20241003184636_db9fe030-39a7-48ba-bfb5-59f8fb5297b8); Time taken: 0.006 seconds
INFO  : OK
INFO  : Concurrency mode is disabled, not creating a lock manager
+-----------+
| tab_name  |
+-----------+
| wine      |
+-----------+
1 row selected (0.035 seconds)
0: jdbc:hive2://localhost:10000>
0: jdbc:hive2://localhost:10000> LOAD DATA LOCAL INPATH '/home/train/Wine.csv' INTO TABLE wine;
SELECT * FROM wine LIMIT 10;
0: jdbc:hive2://localhost:10000> CREATE TABLE wine_alc_gt_13 AS
. . . . . . . . . . . . . . . .> SELECT * FROM wine WHERE Alcohol > 13.00;
0: jdbc:hive2://localhost:10000> SELECT * FROM wine_alc_gt_13 LIMIT 10;
0: jdbc:hive2://localhost:10000> DROP DATABASE hive_odev CASCADE;
0: jdbc:hive2://localhost:10000> CREATE DATABASE company;
0: jdbc:hive2://localhost:10000> USE company;
0: jdbc:hive2://localhost:10000> CREATE TABLE employee (
. . . . . . . . . . . . . . . .>   Employee_ID INT,
. . . . . . . . . . . . . . . .>   Name STRING,
. . . . . . . . . . . . . . . .>   Department STRING,
. . . . . . . . . . . . . . . .>   Skill STRING,
. . . . . . . . . . . . . . . .>   Python_Skill INT
. . . . . . . . . . . . . . . .> ) ROW FORMAT DELIMITED
. . . . . . . . . . . . . . . .> FIELDS TERMINATED BY ','
. . . . . . . . . . . . . . . .> STORED AS TEXTFILE;
0: jdbc:hive2://localhost:10000> LOAD DATA LOCAL INPATH '/home/train/employee.txt' INTO TABLE employee;
0: jdbc:hive2://localhost:10000> SELECT * FROM employee LIMIT 10;
0: jdbc:hive2://localhost:10000> SELECT * FROM employee WHERE Python_Skill > 70;





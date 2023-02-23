# MySQL in Mac OS

## MySQL
1. install
   1. open terminal

   2. input code
   ```
   brew install mysql
   ```
   3. check mysql is installed
   ```
   mysql --version
   ``` 
2. start
   1. input code
   ```
   mysql.server start
   ```

3. security settings
   1. input code
   ```
   mysql_secure_installation
   ```

   2. strong or easy passwords ?

        > Press y|Y for Yes, any other key for No: `n`
  
   3. user setting

        > Remove anonymous users? (Press y|Y for Yes, any other key for No) : `y`

   4. root login remote
        
        > Disallow root login remotely? (Press y|Y for Yes, any other key for No) : `n`
   
   5. test database
        
        > Remove test database and access to it? (Press y|Y for Yes, any other key for No) : `y`

   6. allow privilege tables
        > Reload privilege tables now? (Press y|Y for Yes, any other key for No) : `y`

## MySQL Workbench

1. install
   1. [download link](https://downloads.mysql.com/archives/workbench/)
   2. version
      1. 8.0.31
      2. macOS

2. start `[ after MySQL start ]`
   ![start image](images/Mysql%20Connetion.png)

3. settings
    ![set](images/image%20(1).png)
   
   1. SQL Editor > Query Editor
      1. check
         1. Use UPPERCASE keywords
         2. Change keywords to UPPER CASE


## Use MySQL

1. connect to local data
   1. Administration → Data Import/Restore
   2. `check` Import from Self-Contained File
   3. `click` " . "
   4. `check` file
   5. Start Import
2. check database
   1. Schemas
   2. `click` refresh button
   3. `check` classicmodels
3. Query
   1. `double click` classicmodels
   2. `click` Query edditor
   3. input
      1. ```
         SELECT * FROM customers;
         ```
4. Korean Setting

![korea](images/image%20(2).png)
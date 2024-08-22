SELECT 
    GRANTEE AS 'User',
    TABLE_CATALOG AS 'Catalog',
    PRIVILEGE_TYPE AS 'Privilege'
FROM 
    information_schema.SCHEMA_PRIVILEGES
WHERE 
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");

SELECT 
    GRANTEE AS 'User',
    TABLE_CATALOG AS 'Catalog',
    PRIVILEGE_TYPE AS 'Privilege'
FROM 
    information_schema.TABLE_PRIVILEGES
WHERE 
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");

SELECT 
    GRANTEE AS 'User',
    PRIVILEGE_TYPE AS 'Privilege'
FROM 
    information_schema.USER_PRIVILEGES
WHERE 
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");

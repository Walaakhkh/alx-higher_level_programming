-- This script lists all privileges of the users 'user_0d_1' and 'user_0d_2'

-- Check if 'user_0d_1' and 'user_0d_2' have any schema-level privileges
SELECT 
    GRANTEE AS 'User',
    'SCHEMA_PRIVILEGES' AS 'Privilege Type',
    PRIVILEGE_TYPE AS 'Privilege'
FROM 
    information_schema.SCHEMA_PRIVILEGES
WHERE 
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'")
UNION ALL

-- Check if 'user_0d_1' and 'user_0d_2' have any table-level privileges
SELECT 
    GRANTEE AS 'User',
    'TABLE_PRIVILEGES' AS 'Privilege Type',
    PRIVILEGE_TYPE AS 'Privilege'
FROM 
    information_schema.TABLE_PRIVILEGES
WHERE 
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'")
UNION ALL

-- Check if 'user_0d_1' and 'user_0d_2' have any global user privileges
SELECT 
    GRANTEE AS 'User',
    'USER_PRIVILEGES' AS 'Privilege Type',
    PRIVILEGE_TYPE AS 'Privilege'
FROM 
    information_schema.USER_PRIVILEGES
WHERE 
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");

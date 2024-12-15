-- STEP 1: First connect to PostgreSQL via psql or preferred GUI client
-- STEP 2: Create a new database with UTF-8 encoding
-- This is required to support special characters and various alphabets

-- In psql use the command:
CREATE DATABASE Fleetmanager
    WITH
    OWNER = a516095
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- STEP 3: Connect to the newly created database
-- In psql use the command:
-- \c match_score_db

-- STEP 4: Create UUID extension
-- This is needed to generate unique identifiers for the records
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- STEP 5: Set the timezone for the database
-- Important for correct date and time handling
ALTER DATABASE Fleetmanager SET timezone TO 'Europe/Sofia';

-- After executing these commands, the database is ready for table creation
-- through the main migration file from the API
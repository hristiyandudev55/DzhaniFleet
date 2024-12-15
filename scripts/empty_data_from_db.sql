-- ------------------ locally ------------------
-- DO $$
-- BEGIN
--  -- Disable triggers and constraints
--  EXECUTE 'ALTER TABLE #tablename DISABLE TRIGGER ALL';


--  -- Truncate all tables
--  EXECUTE 'TRUNCATE TABLE #tablename CASCADE';


--  -- Re-enable triggers and constraints
--  EXECUTE 'ALTER TABLE #tablename ENABLE TRIGGER ALL';

-- END $$;



-- ------------------ public ------------------

-- DO $$
-- BEGIN
--     TRUNCATE TABLE ; # tables to be truncated

-- END $$;
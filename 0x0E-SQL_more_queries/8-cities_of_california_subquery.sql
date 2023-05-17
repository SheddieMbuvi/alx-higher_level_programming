-- a sql script to select some cities
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id ASC;

/*
 * SQLite CREATE TABLE in DATABASE.
*/

--
-- regions
--
CREATE TABLE regions(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    region_name TEXT
);

--
-- cities
--
CREATE TABLE cities(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    region_id INTEGER NOT NULL,
    city_name TEXT,
    FOREIGN KEY (region_id) REFERENCES regions(id)
);

--
-- users
--
CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    second_name TEXT,
    first_name TEXT,
    patronymic TEXT,
    region_id INTEGER,
    city_id INTEGER,
    phone TEXT,
    email TEXT,
    FOREIGN KEY (city_id) REFERENCES cities(id),
    FOREIGN KEY (region_id) REFERENCES regions(id)
);

/*
 * SQLite insert data.
*/

--
-- regions
--
INSERT INTO regions VALUES (0, 'Краснодарский край');
INSERT INTO regions VALUES (1, 'Ростовская область');
INSERT INTO regions VALUES (2, 'Ставропольский край');

--
-- cities
--
INSERT INTO cities VALUES (0, 0, 'Краснодар');
INSERT INTO cities VALUES (1, 0, 'Кропоткин');
INSERT INTO cities VALUES (2, 0, 'Славянск');
INSERT INTO cities VALUES (3, 1, 'Ростов');
INSERT INTO cities VALUES (4, 1, 'Шахты');
INSERT INTO cities VALUES (5, 1, 'Батайск');
INSERT INTO cities VALUES (6, 2, 'Ставрополь');
INSERT INTO cities VALUES (7, 2, 'Пятигорск');
INSERT INTO cities VALUES (8, 2, 'Кисловодск');

CREATE TABLE parasha(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	isPublic BOOLEAN,
    nroParasha INT,
    nameParasha VARCHAR(255),
    signParasha VARCHAR(255),
	section1 VARCHAR(255),
	section2 VARCHAR(255),
	section3 VARCHAR(255),
	section4 VARCHAR(255),
	section5 VARCHAR(255),
	section6 VARCHAR(255),
	section7 VARCHAR(255),
    aliya1 TEXT,
    aliya2 TEXT,
    aliya3 TEXT,
    aliya4 TEXT,
    aliya5 TEXT,
    aliya6 TEXT,
    aliya7 TEXT,
    titleReflection1 VARCHAR(255),
    titleReflection2 VARCHAR(255),
    titleReflection3 VARCHAR(255),
    titleReflection4 VARCHAR(255),
    titleReflection5 VARCHAR(255),
    titleReflection6 VARCHAR(255),
    titleReflection7 VARCHAR(255),
    reflection1 TEXT,
    reflection2 TEXT,
    reflection3 TEXT,
    reflection4 TEXT,
    reflection5 TEXT,
    reflection6 TEXT,
    reflection7 TEXT,
    sectionHaftara VARCHAR(255),
    haftara TEXT,
    verso1 TEXT,
    verso2 TEXT,
    verso3 TEXT,
    verso4 TEXT,
    verso5 TEXT,
    verso6 TEXT,
    verso7 TEXT
);


-- actualizar parasha isPublic
UPDATE parasha
SET isPublic = CASE
                WHEN id = 11 THEN 1  -- Actualiza el campo id = " " a true
                ELSE 0
              END
WHERE id = 1 OR id NOT IN (SELECT id FROM parasha WHERE id = 1);

UPDATE parasha SET isPublic = CASE WHEN nroParasha = 11 THEN 1 ELSE 0 END WHERE nroParasha = 1 OR nroParasha NOT IN (SELECT nroParasha FROM parasha WHERE nroParasha = 1);


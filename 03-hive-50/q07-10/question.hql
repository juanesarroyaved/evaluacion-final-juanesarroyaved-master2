-- 
-- Pregunta
-- ===========================================================================
--
-- Escriba una consulta que retorne para cada valor único de la columna `t0.c2`, 
-- los valores correspondientes de la columna `t0.c1`. 
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
DROP TABLE IF EXISTS tbl0;
CREATE TABLE tbl0 (
    c1 INT,
    c2 STRING,
    c3 INT,
    c4 DATE,
    c5 ARRAY<CHAR(1)>, 
    c6 MAP<STRING, INT>
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY ':'
MAP KEYS TERMINATED BY '#'
LINES TERMINATED BY '\n';
LOAD DATA LOCAL INPATH 'tbl0.csv' INTO TABLE tbl0;
--
DROP TABLE IF EXISTS tbl1;
CREATE TABLE tbl1 (
    c1 INT,
    c2 INT,
    c3 STRING,
    c4 MAP<STRING, INT>
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY ':'
MAP KEYS TERMINATED BY '#'
LINES TERMINATED BY '\n';
LOAD DATA LOCAL INPATH 'tbl1.csv' INTO TABLE tbl1;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

DROP TABLE IF EXISTS tabla1;
DROP TABLE IF EXISTS result;

CREATE TABLE tabla1
AS
    SELECT
        c2 AS letra,
        collect_set(cast(c1 as string)) AS num
    FROM
        tbl0
GROUP BY
    c2
ORDER BY
    c2;
    
CREATE TABLE result
AS
    SELECT
        letra,
        concat_ws(':',num)
    FROM
        tabla1;

INSERT OVERWRITE DIRECTORY '/tmp/output'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM result;

!hdfs dfs -copyToLocal /tmp/output output
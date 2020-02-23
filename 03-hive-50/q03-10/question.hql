-- 
-- Pregunta
-- ===========================================================================
--
-- Para resolver esta pregunta use el archivo `data.tsv`.
--
-- Escriba una consulta que devuelva los cinco valores diferentes más pequeños 
-- de la tercera columna.
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
DROP TABLE IF EXISTS data;
DROP TABLE IF EXISTS tabla1;

CREATE TABLE data (
    c1 STRING,
    c2 STRING,
    c3 INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';
LOAD DATA LOCAL INPATH 'data.tsv' INTO TABLE data;

CREATE TABLE tabla1
AS
    SELECT DISTINCT c3 FROM data
ORDER BY
    c3 ASC
LIMIT
    5;
    
INSERT OVERWRITE DIRECTORY '/tmp/output'
-- ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT * FROM tabla1;

!hdfs dfs -copyToLocal /tmp/output output
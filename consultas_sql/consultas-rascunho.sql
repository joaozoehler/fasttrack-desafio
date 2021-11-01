# USE desafio_pagseguro;

# SELECT * FROM transactions GROUP BY gender;

# SELECT * FROM transactions GROUP BY gender;

# SELECT * FROM transactions ORDER BY amount ASC;

# SELECT count(*) FROM transactions WHERE mes = 5 ORDER BY ID DESC;

# SELECT count(*) FROM transactions WHERE (step > 120) AND (step < 151) ORDER BY ID DESC;

# SELECT * FROM transactions WHERE age = 'U';

# SELECT count(*) FROM transactions WHERE age = 'U';

# SELECT count(*) FROM transactions;

/* SELECT *,
	(CASE
		WHEN (step < 31) THEN "1"
        WHEN (step > 30) AND (step < 61) THEN "2"
        WHEN (step > 60) AND (step < 91) THEN "3"
        WHEN (step > 90) AND (step < 121) THEN "4"
        WHEN (step > 120) AND (step < 151) THEN "5"
        WHEN (step > 150) AND (step < 181) THEN "6"
        ELSE "Algo está errado"
	END) AS Mês
FROM transactions; */

# UPDATE transactions SET mes = 1 WHERE step < 31;

/* UPDATE transactions
	SET mes = CASE
				WHEN (step < 31) THEN 1
                WHEN (step > 30) AND (step < 61) THEN 2
                WHEN (step > 60) AND (step < 91) THEN 3
                WHEN (step > 90) AND (step < 121) THEN 4
                WHEN (step > 120) AND (step < 151) THEN 5
                WHEN (step > 150) AND (step < 181) THEN 6
			END; */

# SELECT * FROM transactions ORDER BY amount ASC;

# UPDATE transactions SET amount = NULL WHERE amount = 0;

# UPDATE transactions SET age = NULL WHERE age = "U";

UPDATE transactions
	SET gender = CASE
		WHEN gender = "E" THEN NULL
        WHEN gender = "U" THEN NULL
	END;

# ALTER TABLE transactions ADD id INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST;

# ALTER TABLE transactions ADD ano SMALLINT DEFAULT 2021;

# ALTER TABLE transactions ADD dia SMALLINT DEFAULT 1;

# ALTER TABLE transactions ADD mes SMALLINT AFTER ano;

/* |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| */
/* EXPERIMENTAÇÕES DAQUI PARA BAIXO */
/* |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| */

# ALTER TABLE transactions ADD data VARCHAR(255) DEFAULT (CONCAT(ano, "-", mes, "-", dia));

/* ALTER TABLE transactions (
	ADD mes SMALLINT AS (
		(CASE
			WHEN (step < 31) THEN "1"
			WHEN (step > 30) AND (step < 61) THEN "2"
			WHEN (step > 60) AND (step < 91) THEN "3"
			WHEN (step > 90) AND (step < 121) THEN "4"
			WHEN (step > 120) AND (step < 151) THEN "5"
			WHEN (step > 150) AND (step < 181) THEN "6"
			ELSE "Algo está errado"
		END)
		STORED
    ); */
		
/* ALTER TABLE NOMEDATABELA
ADD dia SMALLINT DEFAULT 1;
CREATE TABLE tbl_Vendas (
	Preco_Total DECIMAL(6,2) AS (Preco_Produto * Qtde * (1 - Desconto / 100)) STORED
	); */

# ALTER TABLE transactions ADD id INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST;
# ALTER TABLE transactions ADD ano SMALLINT DEFAULT 2021;
# ALTER TABLE transactions ADD dia SMALLINT DEFAULT 1;

# ALTER TABLE transactions DROP COLUMN ID;

# DROP SCHEMA desafio_pagseguro;
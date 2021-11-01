CREATE SCHEMA analytic;
USE analytic;

# fact_merchant_kpi
CREATE TABLE fact_merchant_kpi
#INSERT INTO fact_merchant_kpi
	SELECT CONCAT(t.ano, "-", t.mes, "-", t.dia) AS data, t.merchant, SUM(t.amount) AS TPV, COUNT(DISTINCT t.id) AS qtd_transacoes
    FROM desafio_pagseguro.transactions AS t
    GROUP BY t.merchant
    ORDER BY t.merchant;

SELECT * FROM fact_merchant_kpi;

# fact_customer_kpi
CREATE TABLE fact_customer_kpi
	SELECT CONCAT(t.ano, "-", t.mes, "-", t.dia) AS data, t.merchant, t.customer, SUM(t.amount) AS TPV, COUNT(DISTINCT t.id) as qtde_transacoes
    FROM desafio_pagseguro.transactions AS t
    GROUP BY t.customer
    ORDER BY CONCAT(t.ano, "-", t.mes, "-", t.dia);

SELECT * FROM fact_customer_kpi;

# dim_merchant_category
CREATE TABLE dim_merchant_category
	SELECT t.merchant, t.category
    FROM desafio_pagseguro.transactions AS t
    GROUP BY t.merchant
    ORDER BY t.category;

SELECT * FROM dim_merchant_category;
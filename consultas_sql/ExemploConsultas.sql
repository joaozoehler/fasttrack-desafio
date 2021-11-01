# Mostra schemas
SHOW SCHEMAS;

# Seleciona bd base para uso
USE desafio_pagseguro;

# Seleção simples para conferência
SELECT * FROM transactions LIMIT 5;

# Seleção para conferir os valores em AGE após conversão de U = NULL
SELECT * FROM transactions GROUP BY age;

# Seleção para conferir os valores em GENDER após conversão de E AND U = NULL
SELECT * FROM transactions GROUP BY gender;

# Seleção para contabilizar o total arrecadado por categoria
SELECT category, SUM(amount) AS amount_total FROM transactions GROUP BY category ORDER BY category;

# Seleciona schema de análise
USE analytic;

# Mostra tabelas
SHOW TABLES;

SELECT * FROM dim_merchant_category;

SELECT * FROM fact_customer_kpi;

SELECT * FROM fact_merchant_kpi;
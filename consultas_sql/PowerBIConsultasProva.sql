USE desafio_pagseguro;

SELECT id, customer, amount FROM transactions WHERE customer = 'C995844287';

SELECT customer, SUM(amount) FROM transactions WHERE customer = 'C995844287';

SELECT customer, COUNT(DISTINCT id) FROM transactions WHERE customer = 'C995844287';

-- Vendedores organizados segundo a quantidade de transações
SELECT merchant as Vendedor, COUNT(DISTINCT id) AS Transações FROM transactions GROUP BY merchant ORDER BY COUNT(DISTINCT id) DESC;

-- Vendedores ordenados por ticket médio (TPV/qtd_transacoes)
SELECT merchant, (SUM(amount) / COUNT(DISTINCT id)) AS ticket_medio FROM transactions GROUP BY merchant ORDER BY (SUM(amount) / COUNT(DISTINCT id)) DESC;

-- Consumidores organizados conforme a quantidade de transações
SELECT customer, COUNT(DISTINCT id) AS transacoes FROM transactions GROUP BY customer ORDER BY COUNT(DISTINCT id) DESC LIMIT 10;

-- Consumidores ordenados por ticket médio (TPV/qtd_transacoes)
SELECT customer, (SUM(amount) / COUNT(DISTINCT id)) AS ticket_medio FROM transactions GROUP BY customer ORDER BY (SUM(amount) / COUNT(DISTINCT id)) DESC;

-- Categorias ordenadas por ticket médio (TPV/qtd_transacoes)
SELECT category, (SUM(amount) / COUNT(DISTINCT id)) AS ticket_medio FROM transactions GROUP BY category ORDER BY (SUM(amount) / COUNT(DISTINCT id)) DESC;

-- Categorias ordenadas por quantidade de transações
SELECT category, COUNT(DISTINCT id) as transações FROM transactions GROUP BY category ORDER BY COUNT(DISTINCT id) DESC;

-- Quantidade de vendedores (merchant) distintos
SELECT COUNT(DISTINCT merchant) FROM transactions;

-- Ticket médio por mês (data, afinal, apenas o mês é que muda na formação da data)
SELECT `data`, (SUM(amount) / COUNT(DISTINCT id)) AS ticket_medio FROM transactions GROUP BY `data` ORDER BY (SUM(amount) / COUNT(DISTINCT id)) DESC;

-- Ticket médio no mês de abril
SELECT (SUM(amount) / COUNT(DISTINCT id)) FROM transactions WHERE `data` = '2021-4-1';

-- Ticket médio geral
SELECT (SUM(amount) / COUNT(DISTINCT id)) AS ticket_medio FROM transactions;

SELECT (SUM(amount) / COUNT(DISTINCT id)) AS ticket_medio FROM transactions GROUP BY `data`;

-- Ticket médio do cliente C995844287
SELECT customer, (SUM(amount) / COUNT(DISTINCT id)) AS ticket_medio FROM transactions WHERE customer = 'C995844287';

/* |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| */

USE analytic;

SELECT customer, ((SUM(TPV)) / (SUM(qtd_transacoes))) AS ticket_medio FROM fact_customer_kpi GROUP BY customer ORDER BY ((SUM(TPV)) / (SUM(qtd_transacoes))) DESC;

SELECT `data`, ((SUM(TPV)) / (SUM(qtd_transacoes))) AS ticket_medio FROM  fact_merchant_kpi GROUP BY `data`ORDER BY `data`;

SELECT customer, ((SUM(TPV)) / (SUM(qtd_transacoes))) AS ticket_medio FROM fact_customer_kpi GROUP BY customer ORDER BY ticket_medio DESC;

SELECT customer, SUM(TPV/qtd_transacoes) as TICKET FROM fact_customer_kpi GROUP BY customer ORDER BY TICKET DESC LIMIT 10;

SELECT * FROM fact_customer_kpi ORDER BY `data`, customer;

/* |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| */
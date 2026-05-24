SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = "Yes" THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        AVG(CASE WHEN Churn = "Yes" THEN 1 ELSE 0 END)*100,
        2
        ) AS churn_rate
FROM customers;
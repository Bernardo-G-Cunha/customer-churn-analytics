SELECT
    TechSupport,
    COUNT(*) AS customers,
    ROUND(
        AVG(
            CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100,
        2
    ) AS churn_rate
FROM customers
GROUP BY TechSupport
ORDER BY churn_rate DESC;
username=a
SELECT Symbol, COUNT(Symbol),SUM(ExecQty) AS 'TotalQty' FROM executions GROUP BY Symbol
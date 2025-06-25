-- select w.id as Id
-- from Weather w
-- join Weather w1 on w1.id = w.id - 1
-- where w.temperature > w1.temperature

SELECT id as Id
FROM (
    SELECT id, temperature, recordDate,
           LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
           LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
) AS sub
WHERE temperature > prev_temp
  AND DATEDIFF(recordDate, prev_date) = 1;


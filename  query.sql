SELECT name,
         (hour(cast(ts AS timestamp))-4),
         max(high) max_high
FROM "01"
GROUP BY  name,hour(cast(ts AS timestamp))
ORDER BY  hour(cast(ts AS timestamp));
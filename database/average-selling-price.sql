# Write your MySQL query statement below

select P.product_id, ROUND(
        COALESCE(SUM(p.price * u.units) / SUM(u.units), 0),
        2
    ) AS average_price from Prices P left join UnitsSold U on P.product_id = U.product_id and U.purchase_date between P.start_date and P.end_date group by product_id;
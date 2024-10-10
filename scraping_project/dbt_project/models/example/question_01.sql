-- Which customers have placed an order, and what is the total order amount for each customer?

select
distinct c.customer_name
from customers c
join orders o
on c.customer_id = o.customer_id

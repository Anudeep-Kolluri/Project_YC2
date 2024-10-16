-- Extacts batch number form tags

with cte as (
    select id, split(tags, ',')[0]::string as batch
    from companies
)
select * from cte
with cte as (
    select id, split(location, ',') as location
    from companies
),
cte2 as (
    select cte.id,
        case
            when array_size(cte.location) = 3 then cte.location
            when array_size(cte.location) = 2 then array_insert(cte.location, 0, NULL)
            when array_size(cte.location) = 1  and cte.location[0] != '' then array_cat(array_construct(NULL, NULL), cte.location)
            else array_construct(NULL, NULL, NULL)
        end as location
    from cte
)
select
    cte2.id,
    cte2.location[0] as city,
    cte2.location[1] as state,
    cte2.location[2] as country
from cte2

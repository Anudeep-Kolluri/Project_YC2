with cte as (
    select id, split(tags, ',') as tags
    from companies
), 
cte2 as (
    select cte.id,
        case
            when cte.tags[1] = 'B2B'
            then array_slice(cte.tags, 2, array_size(cte.tags))
            else array_slice(cte.tags, 1, array_size(cte.tags))
        end as tags
    from cte
)

select cte2.id, c.value::string as tag
from cte, cte2, lateral flatten(cte2.tags) c
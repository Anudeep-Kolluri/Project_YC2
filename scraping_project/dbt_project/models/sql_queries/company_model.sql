-- Extracts 'B2B' companies

select id,
    case
        when split(tags, ',')[1] = 'B2B'
        then 'B2B'
        else NULL
    end as company_model
from companies
where company_model is not NULL
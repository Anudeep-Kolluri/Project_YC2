select
    co.id, 
    co.name, 
    co.description, 
    cloc.city, 
    cloc.state, 
    cloc.country,
    cbat.batch,
    cmod.company_model
from
    companies co
join
    {{ ref('company_location') }} cloc on
    cloc.id = co.id
join
    {{ ref('company_batch') }} cbat on
    cbat.id = co.id
left join
    {{ ref('company_model') }} cmod on
    cmod.id = co.id
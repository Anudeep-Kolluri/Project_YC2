from dagster import Definitions, load_assets_from_modules

from .assets import \
    scrape,\
    save2db,\
    check_db

from .resources import dbt_resource, duckdb_resource, snowflake_resource # import the dbt resource


# python_assets = load_assets_from_modules(modules=[assets])
# dbt_analytics_assets = load_assets_from_modules(modules=[dbt]) # Load the assets from the file

all_assets = load_assets_from_modules(modules=[scrape, save2db, check_db])


defs = Definitions(
    assets=[*all_assets],
    resources={
        "dbt": dbt_resource,
        "ddb": duckdb_resource,
        "snowflake": snowflake_resource
    },
)

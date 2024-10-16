from .assets import \
    scrape,\
    save2db,\
    check_db,\
    ingest,\
    dbt

from .resources import dbt_resource, duckdb_resource, snowflake_resource # import the dbt resource

from dagster import Definitions, load_assets_from_modules, define_asset_job

# python_assets = load_assets_from_modules(modules=[assets])
dbt_assets = load_assets_from_modules(modules=[dbt])

all_assets = load_assets_from_modules(modules=[scrape, save2db, check_db, ingest])

all_assets_job = define_asset_job(name="all_assets_job")

defs = Definitions(
    assets=[*all_assets, *dbt_assets],
    resources={
        "dbt": dbt_resource,
        "ddb": duckdb_resource,
        "snowflake": snowflake_resource
    },
    jobs=[all_assets_job]
)

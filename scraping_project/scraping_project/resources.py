from .project import dbt_project_path


from dagster_dbt import DbtCliResource
from dagster_duckdb import DuckDBResource
from dagster_snowflake import SnowflakeResource

from dagster import EnvVar


# this can be defined anywhere below the imports
dbt_resource = DbtCliResource(
    project_dir=dbt_project_path,
)


duckdb_resource = DuckDBResource(
    database = EnvVar("DUCKDB_DATABASE")
)


snowflake_resource = SnowflakeResource(
    account=EnvVar("SNOWFLAKE_ACCOUNT"),  
    user=EnvVar("SNOWFLAKE_USER"),  
    password=EnvVar("SNOWFLAKE_PASSWORD"),  
    warehouse="COMPUTE_WH",
    database="SCRAPE_DB",
    schema="SCRAPE_SCHEMA",
    role="ACCOUNTADMIN"
)

from dagster import AssetExecutionContext
from dagster_dbt import dbt_assets, DbtCliResource

from ..project import dbt_project_path


@dbt_assets(
    manifest=dbt_project_path.manifest_path,
)
def dbt_analytics(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["run"], context=context).stream()
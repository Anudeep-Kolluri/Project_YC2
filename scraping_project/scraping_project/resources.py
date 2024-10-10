from dagster_dbt import DbtCliResource

from .project import dbt_project_path
# the import lines go at the top of the file

# this can be defined anywhere below the imports
dbt_resource = DbtCliResource(
    project_dir=dbt_project_path,
)

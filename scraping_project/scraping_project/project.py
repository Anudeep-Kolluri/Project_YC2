from pathlib import Path

from dagster_dbt import DbtProject

# print(Path(__file__).joinpath("..", "..", "dbt_project").resolve())

dbt_project_path = DbtProject(
  project_dir=Path(__file__).joinpath("..", "..", "dbt_project").resolve(),
)

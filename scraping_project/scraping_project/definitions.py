from dagster import Definitions, load_assets_from_modules

from .assets import dbt, assets # Import the dbt assets
from .resources import dbt_resource # import the dbt resource


python_assets = load_assets_from_modules(modules=[assets])
dbt_analytics_assets = load_assets_from_modules(modules=[dbt]) # Load the assets from the file


defs = Definitions(
    assets=[*dbt_analytics_assets, *python_assets],
    resources={
        "dbt": dbt_resource
    },
)

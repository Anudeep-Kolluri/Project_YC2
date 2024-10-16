from .save2db import save2db

from dagster import asset
from dagster_snowflake import SnowflakeResource
from dagster_duckdb import DuckDBResource


@asset(deps=[save2db])
def ingest(ddb: DuckDBResource, snowflake: SnowflakeResource):
    """
    Sending data from duckdb to snowflake
    """

    # FILE_PATH = '/workspaces/Project_YC2/scraping_project/data/scraped_data.duckdb'
    OUTPUT_PATH = 'output.csv'

    query = f"copy companies to {OUTPUT_PATH} (HEADER FALSE, DELIMITER ',');"

    

    with ddb.get_connection() as duck, snowflake.get_connection() as snow:
        duck.execute(
            """
            copy companies to 'companies.csv' (HEADER FALSE, DELIMITED ',');
            """
        )

        snow_cur = snow.cursor()

        print("Checking for existing .csv files")
        files = snow_cur.execute(
            """
            list @scrape_stage;
            """
        ).fetchall()

        if files:
            print("Found existing files, removing them")
            snow_cur.execute(
                """
                remove @scrape_stage/companies.csv.gz;
                """
            )

            print("Successfully removed")

        else:
            print("Nothing found")




        snow_cur.execute(
            """
            put 'file://companies.csv' @SCRAPE_STAGE;
            """
        )

        snow_cur.execute(
            """
            copy into companies from @scrape_stage;
            """
        )
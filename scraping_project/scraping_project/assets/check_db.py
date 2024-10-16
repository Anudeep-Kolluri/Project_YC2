from .scrape import scrape


from dagster import asset, AssetIn
from dagster_duckdb import DuckDBResource
from typing import List


@asset(
    ins={
        "scraped_data" : AssetIn(key="scrape")
    }
)
def check_db(ddb: DuckDBResource, scraped_data: List) -> List:
    """
    Check if table schema exists in duckdb
    """

    query = """
                show tables;
            """

    with ddb.get_connection() as conn:
        results = conn.execute(query).fetchall()

    # print(results)

    if ('companies',) not in results:
        table_query = """
             create table companies (
                Id int,
                Name varchar,
                Description varchar,
                Location varchar,
                Tags varchar) ;
        """
        with ddb.get_connection() as conn:
            conn.execute(table_query)
            print("table created successfully")
    else:
        print("table already exists")

    return scraped_data

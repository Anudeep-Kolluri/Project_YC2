from typing import List
from dagster import asset, AssetIn
from dagster_duckdb import DuckDBResource


@asset(
    ins={
        "scraped_data" : AssetIn(key="check_db")
    }
)
def save2db(ddb: DuckDBResource, scraped_data: List):
    """
    Create duckdb connection and store data into duckdb
    """

    
    print("executing query to insert values")
    with ddb.get_connection() as conn:
        for row in scraped_data:
            conn.execute("INSERT INTO companies VALUES (?, ?, ?, ?)", row)
    
    print("finished query execution")

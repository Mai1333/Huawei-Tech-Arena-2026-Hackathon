# Polars/DuckDB parsers for CSV & JSON history
import polars as pl # Polars library for DataFrame operations
import json # JSON library for parsing JSON files

def load_data(filepath: str) -> pl.DataFrame: # Load CSV/JSON data into a Polars DataFrame
    # Read CSV treating opaque IDs as String/Categorical
    df = pl.read_csv( # Load CSV with specified schema overrides
        filepath, # Path to the CSV file to load
        schema_overrides={
            "user_id": pl.Utf8, # Treat user_id as string
            "item_id": pl.Utf8, # Treat item_id as string
            "rowid": pl.Utf8, # Treat rowid as string
            "event_id": pl.Utf8 # Treat event_id as string
        }
    )
    return df # Return the loaded DataFrame
from typing import List, Generator

from src.constants import BASE_SCHEMA
import pyarrow.json as pj
import pyarrow as pa
import pandas as pd
import emoji


def build_pa_schema(selected_cols: List[str]):
    return pa.schema([BASE_SCHEMA[field] for field in selected_cols])


def build_dataframe_time(file_path: str, selected_cols: List[str]):
    """
    Build dataframe using a subset of columns from json located in the given path.
    
    :param file_path: Path of Json file
    :type file_path: str
    :param selected_cols: List of columns to be filtered
    :type selected_cols: List[str]
    """
    pa_schema = build_pa_schema(selected_cols)
    parse_options = pj.ParseOptions(explicit_schema=pa_schema, unexpected_field_behavior="ignore")
    table = pj.read_json(file_path, parse_options=parse_options)
    return table.to_pandas()


def build_dataframe_chunks(file_path: str, selected_cols: List[str], block_size: int = 1000000) -> Generator[pd.DataFrame, None, None]:
    """
    Build dataframe in chunks using a subset of columns from a JSON file.
    
    :param file_path: Path of Json file
    :param selected_cols: List of columns to be filtered
    :param block_size: Size of the chunks in bytes (default ~1MB)
    :yield: A pandas DataFrame chunk
    """
    pa_schema = build_pa_schema(selected_cols)
    
    parse_options = pj.ParseOptions(explicit_schema=pa_schema, unexpected_field_behavior="ignore")
    read_options = pj.ReadOptions(block_size=block_size)

    with pj.open_json(file_path, read_options=read_options, parse_options=parse_options) as reader:
        for batch in reader:
            # Convert each RecordBatch to a pandas DataFrame
            yield batch.to_pandas()


def extract_emojis(text: str) -> List[str]:
    """Extracts all emojis from a given string."""
    if not text:
        return []
    # emoji_list returns a list of dictionaries with emoji information
    return [item['emoji'] for item in emoji.emoji_list(text)]
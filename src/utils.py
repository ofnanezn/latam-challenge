from typing import List

from src.constants import BASE_SCHEMA
import pyarrow.json as pj
import pyarrow as pa


def build_pa_schema(selected_cols: List[str]):
    return pa.schema([BASE_SCHEMA[field] for field in selected_cols])


def build_dataframe(file_path: str, selected_cols: List[str]):
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

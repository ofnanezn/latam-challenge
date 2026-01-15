from typing import List, Tuple

from src.utils import build_dataframe
from datetime import datetime
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Assuming beforehand we know the columns we need for the exercise 
    required_cols = ['date', 'user']
    df = build_dataframe(file_path, required_cols)
    return df
    
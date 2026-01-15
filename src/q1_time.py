from typing import List, Tuple

from src.utils import build_dataframe_time
from datetime import datetime
import pandas as pd

def q1_time(file_path: str, chunk_size: int = 100) -> List[Tuple[datetime.date, str]]:
    # Assuming beforehand we know the columns we need for the exercise 
    required_cols = ['date', 'user']
    df = build_dataframe_time(file_path, required_cols)
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['counts'] = df.groupby('date')['date'].transform('count')
    df['rank'] = df['counts'].rank(ascending=False, method='dense')
    df = df[df['rank'] <= 10]
    df['username'] = df['user'].str['username']
    username_counts = df.groupby(['date', 'rank'])['username'].value_counts()
    result = username_counts.groupby(level=0).head(1).reset_index().sort_values(by='rank')
    return list(result[['date', 'username']].itertuples(index=False, name=None))
    
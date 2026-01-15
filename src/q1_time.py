from typing import List, Tuple

from src.utils import build_dataframe_time
from datetime import datetime
import pandas as pd

def q1_time(file_path: str, chunk_size: int = 100) -> List[Tuple[datetime.date, str]]:
    # Assuming beforehand we know the columns we need for the exercise 
    required_cols = ['date', 'user']

    df = build_dataframe_time(file_path, required_cols)
    
    df['date'] = pd.to_datetime(df['date']).dt.date # Truncate date
    df['counts'] = df.groupby('date')['date'].transform('count') # Count dates, but preserve dimensions
    df['rank'] = df['counts'].rank(ascending=False, method='dense') # Get ranks of count
    df = df[df['rank'] <= 10] # Get top 10 ranking
    df['username'] = df['user'].str['username'] # Extract username from user struct
    
    username_counts = df.groupby(['date', 'rank'])['username'].value_counts() # Get count of username tweets per date (rank preserved to sort values later)
    
    # Group by date (level 0) and select first element (ordered by value_counts), finally sort results by rank
    result = username_counts.groupby(level=0).head(1).reset_index().sort_values(by='rank')
    # Return in the required format
    return list(result[['date', 'username']].itertuples(index=False, name=None))
    
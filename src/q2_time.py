from typing import List, Tuple

from src.utils import build_dataframe_time, extract_emojis

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Assuming beforehand we know the columns we need for the exercise 
    required_cols = ['content']
    
    df = build_dataframe_time(file_path, required_cols)
    
    df['content'] = df['content'].apply(extract_emojis) # Get a list of emojis per content 
    df = df.explode('content') # Flatmap operation for the list of emojis   
    top_emojis = df.value_counts().sort_values(ascending=False).head(10) # Get top 10 used emojis 

    # return in the required format
    return list(top_emojis.reset_index().itertuples(index=None, name=None))

from typing import List, Tuple

from src.utils import build_dataframe_time

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Assuming beforehand we know the columns we need for the exercise 
    required_cols = ["mentionedUsers"]

    df = build_dataframe_time(file_path, required_cols)

    df = df.explode('mentionedUsers') # Flatmap operation on the list of mentioned users
    df['mentionedUsers'] = df['mentionedUsers'].str['username'] # Get username from user struct 

    top_users = df.value_counts().sort_values(ascending=False).head(10) # Count user mentions and get top 10

    # Return in the required format
    return list(top_users.reset_index().itertuples(index=None, name=None))


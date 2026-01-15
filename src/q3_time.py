from typing import List, Tuple

from src.utils import build_dataframe_time

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    required_cols = ["mentionedUsers"]

    df = build_dataframe_time(file_path, required_cols)

    df = df.explode('mentionedUsers')
    df['mentionedUsers'] = df['mentionedUsers'].str['username']

    top_users = df.value_counts().sort_values(ascending=False).head(10)

    return list(top_users.reset_index().itertuples(index=None, name=None))


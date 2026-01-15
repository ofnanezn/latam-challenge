from typing import List, Tuple

from src.utils import build_dataframe_chunks
from collections import Counter


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    total_users_counter = {}
    required_cols = ["mentionedUsers"]
    
    for chunk in build_dataframe_chunks(file_path, required_cols):
        chunk = chunk.explode('mentionedUsers')
        chunk['mentionedUsers'] = chunk['mentionedUsers'].str['username']
        
        count_users = chunk.value_counts()
        count_users.index = count_users.index.get_level_values(0)
        count_users_dict = count_users.to_dict()

        total_users_counter = dict(Counter(total_users_counter) + Counter(count_users_dict))

    sorted_users = sorted(total_users_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_users[:10]
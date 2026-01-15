from typing import List, Tuple

from src.utils import build_dataframe_chunks
from collections import Counter


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    total_users_counter = {} # Keep track of total user mentions
    required_cols = ["mentionedUsers"]
    
    for chunk in build_dataframe_chunks(file_path, required_cols):
        chunk = chunk.explode('mentionedUsers') # Flatmap operation on the list of mentioned users
        chunk['mentionedUsers'] = chunk['mentionedUsers'].str['username'] # Get username from user struct 
        
        # Count mentions and transform to a dictionary user: count
        count_users = chunk.value_counts()
        count_users.index = count_users.index.get_level_values(0)
        count_users_dict = count_users.to_dict()

        # Sum counts to the total tracker
        total_users_counter = dict(Counter(total_users_counter) + Counter(count_users_dict))

    # Sort based on count and get top 10 users mentioned
    sorted_users = sorted(total_users_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_users[:10]
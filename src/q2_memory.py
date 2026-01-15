from typing import List, Tuple

from src.utils import build_dataframe_chunks, extract_emojis
from collections import Counter


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    total_emojis_counter = {} # Keep track of total count of emojis
    required_cols = ['content']
    
    # Load dataframe in chunks
    for chunk in build_dataframe_chunks(file_path, required_cols):
        chunk['content'] = chunk['content'].apply(extract_emojis) # Get a list of emojis per content 
        chunk = chunk.explode('content') # Flatmap operation for the list of emojis 
        
        # Count emojis and transform to a dictionary emoji: count
        count_emojis = chunk.value_counts()
        count_emojis.index = count_emojis.index.get_level_values(0)
        count_emojis_dict = count_emojis.to_dict()

        # Sum counts to the total tracker
        total_emojis_counter = dict(Counter(total_emojis_counter) + Counter(count_emojis_dict))

    # Sort based on count and get top 10 emojis
    sorted_emojis = sorted(total_emojis_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_emojis[:10]





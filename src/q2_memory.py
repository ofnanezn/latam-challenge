from typing import List, Tuple

from src.utils import build_dataframe_chunks, extract_emojis
from collections import Counter


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    total_emojis_counter = {}
    required_cols = ['content']
    
    for chunk in build_dataframe_chunks(file_path, required_cols):
        chunk['content'] = chunk['content'].apply(extract_emojis)
        chunk = chunk.explode('content')   
        
        count_emojis = chunk.value_counts()
        count_emojis.index = count_emojis.index.get_level_values(0)
        count_emojis_dict = count_emojis.to_dict()

        total_emojis_counter = dict(Counter(total_emojis_counter) + Counter(count_emojis_dict))

    sorted_emojis = sorted(total_emojis_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_emojis[:10]





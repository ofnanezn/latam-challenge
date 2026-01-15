from typing import List, Tuple

from src.utils import build_dataframe_chunks
from datetime import datetime
import pandas as pd


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    daily_tweet_totals = {} # Keep track of total tweets per date
    daily_user_counts = {} # Keep track of total tweets per user per date
    required_cols = ['date', 'user']
    
    # Load dataframe in chunks
    for chunk in build_dataframe_chunks(file_path, required_cols):
        chunk['date'] = pd.to_datetime(chunk['date']).dt.date
        chunk['username'] = chunk['user'].str['username']

        chunk_daily_totals = chunk['date'].value_counts() # Count tweets per date
        # Sum tweets count to the total tracker
        for date, count in chunk_daily_totals.items():
            daily_tweet_totals[date] = daily_tweet_totals.get(date, 0) + count

        chunk_user_counts = chunk.groupby(['date', 'username']).size() # Count tweets per date per user
        # Sum count per user/date to the total tracker 
        for (date, user), count in chunk_user_counts.items():
            if date not in daily_user_counts:
                daily_user_counts[date] = {}
            daily_user_counts[date][user] = daily_user_counts[date].get(user, 0) + count

    # Get rank of count of tweets per date and filter top 10
    date_series = pd.Series(daily_tweet_totals)
    top_10_dates = date_series.rank(ascending=False, method='dense').sort_values()
    top_10_dates = top_10_dates[top_10_dates <= 10].index.tolist()

    # For each date get the user with max count of tweets
    final_results = []
    for date in top_10_dates:
        users_that_day = daily_user_counts[date]
        top_user = max(users_that_day, key=users_that_day.get)
        final_results.append((date, top_user))

    return final_results
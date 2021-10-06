import pandas as pd

record = pd.Series(listed_item, index=listed_item_df.columns)
listed_item_df = listed_item_df.append(record, ignore_index=True)
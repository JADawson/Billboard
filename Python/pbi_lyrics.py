# 'dataset' holds the input data for this script
import pandas as pd
from better_profanity import profanity

profanity.load_censor_words()

dataset['SplitLyrics'] = dataset['Lyrics'].str.split()

lyric_melt = dataset.SplitLyrics.apply(pd.Series) \
    .merge(dataset, right_index = True, left_index = True) \
    .drop(['SplitLyrics', 'Lyrics', 'Source','Song','Artist'], axis = 1) \
    .melt(id_vars=['Rank', 'Year'],
        value_name='LyricWord') \
    .dropna()

lyric_melt['Profanity'] = lyric_melt['LyricWord'].apply(profanity.contains_profanity)
lyric_melt['CensoredWork'] = lyric_melt['LyricWord'].apply(profanity.censor)



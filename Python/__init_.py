import pandas as pd
from better_profanity import profanity


profanity.load_censor_words()



data_url = 'https://raw.githubusercontent.com/walkerkq/musiclyrics/master/billboard_lyrics_1964-2015.csv'

dataset = pd.read_csv(data_url, encoding='iso-8859-1')

dataset['SplitLyrics'] = dataset['Lyrics'].str.split()
dataset['SongCensored'] = dataset['Song'].apply(profanity.censor)

lyric_melt = dataset.SplitLyrics.apply(pd.Series) \
    .merge(dataset, right_index = True, left_index = True) \
    .drop(['SplitLyrics', 'Lyrics', 'Source','Song','Artist'], axis = 1) \
    .melt(id_vars=['Rank', 'Year'],
        value_name='LyricWord') \
    .dropna()

lyric_melt['Profanity'] = lyric_melt['LyricWord'].apply(profanity.contains_profanity)
lyric_melt['CensoredWord'] = lyric_melt['LyricWord'].apply(profanity.censor)


##############

import pandas as pd
from better_profanity import profanity
profanity.load_censor_words()

dataset['SongCensored'] = dataset['Song'].apply(profanity.censor)
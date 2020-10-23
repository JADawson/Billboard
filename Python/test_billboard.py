import pandas as pd
from better_profanity import profanity

data_url = 'https://raw.githubusercontent.com/walkerkq/musiclyrics/master/billboard_lyrics_1964-2015.csv'

dataset = pd.read_csv(data_url, encoding='iso-8859-1')

profanity.load_censor_words()

dataset['SongCensored'] = dataset['Song'].apply(profanity.censor)
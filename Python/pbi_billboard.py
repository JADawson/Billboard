# 'dataset' holds the input data for this script
import pandas as pd
from better_profanity import profanity

profanity.load_censor_words()

dataset['SongCensored'] = dataset['Song'].apply(profanity.censor)

dataset['LyricsCensored'] = dataset['Lyrics'].apply(profanity.censor)
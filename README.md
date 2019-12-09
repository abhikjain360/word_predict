# word_predict

This is a simple word predictor. Run words_predict.py using a Python 3.6 or above to use it.

## The Database
The database which has all words arranged in decreasing frequency of their usage, along with whether they are nouns, or adjectives. This is build using sqlite3 as it can easily be used in python, and is in words.db.

The database has been taken in .csv form from https://www.kaggle.com/rtatman/english-word-frequency and is distributed under MIT license. The data was then converted to a table in the database by simply using csv and sqlite3 libraries available as standard libraries in python. This dataset includes 333,333 most commonly used single words on the English language web. 

Then used http://www.ashley-bovan.co.uk/words/partsofspeech.html to get txt list of nouns and adjectives to sort words accordingly. 

The table in the database is named as unigram_freq. it has 5 columns: sno, text, count, noun & adj. Columns count countains the number of times word occured in the text used to genereate the dataset, sno is simply the index of words and noun & adj are columns which countain 0 or 1 corresponding to whether the word in a noun or adjective

Though the fact that we have words sorted in nouns and adjectives (and maybe add verbs in future), I don't use it to make better predictions of the text, yet, as it wil involve more complex algorithm, and maybe even machine learning.

In future I might also use index of the predictions to get faster predictions, and also remove the one character lag while giving predictions. I also plan to add punctuations in the prediction.

## word_predict.py
The python file which has all the code. It uses tkinter to render it's GUI and sqlite3 library to read from words.db
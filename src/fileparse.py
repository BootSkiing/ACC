"""
filename: backend.py
purpose: This file is meant to use the training set to come up
with sentiments for the real data.
author: Ayobami(Emmanuel) Adewale
"""

import pandas
from textblob import TextBlob
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Reading the training set file
location = "../data/training_set_rel3.tsv"
file = pandas.read_csv(location, sep="\t", encoding='latin1')
#
important_colum = ['essay', 'domain1_score']
filter_data = file[important_colum]

df = pandas.DataFrame(filter_data)


#
# An essay can be graded on the basis of these factors:
# Grammatical errors in essay
# Number of words an essay has
# Number of sentence an essay has
# Sentiment of essay
# average length of essay

# TODO: PUT IN THE ORIGINAL DATASET

def wordCounting(x):
    return len(TextBlob(x).words)


# Adding a new column for word_count
df['word_count'] = filter_data['essay'].apply(wordCounting)


def sentence_counting(x):
    sentence_len = len([len(sentence.split(' ')) for sentence in TextBlob(x).sentences])
    return sentence_len


df['sentence_count'] = filter_data['essay'].apply(sentence_counting)


def avgLengthWord(x):
    word_len = [len(word) for word in TextBlob(x).words]
    return sum(word_len) / len(word_len)


df['avg_word'] = filter_data['essay'].apply(avgLengthWord)


def avgSentiment(x):
    sentiment = TextBlob(x).sentiment.polarity
    return sentiment


df['avg_sentiment'] = filter_data['essay'].apply(avgSentiment)

# Having problems installing the module that does Grammer check
# so skip for now.
# def grammerCheck(x):

# Convert our new data to csv
df.to_csv('../data/clear_data.csv', sep="\t")

# Fixing dataset to be between range -1 to 1

# Read new Data
new_data = pandas.read_csv('../data/clear_data.csv', sep="\t")
remove_essay = new_data.drop('essay', axis=1)

scaler = preprocessing.MinMaxScaler()
scale = scaler.fit_transform(new_data.drop('essay', axis=1))
normalizer = pandas.DataFrame(scale,
                              columns=['test', 'score', 'word_count', 'sentence_count', 'avg_word', 'avg_sentiment'])
remove_test = normalizer.drop('test', axis=1)
x = remove_test['score']
y = remove_test.drop('score', axis=1)
print(y.head(5))

# The actual machine learningish part I think.
# I'm too stupid to know the differences.(Emmanuel)

x_train, x_test, y_train, y_test = train_test_split(y, x, test_size=0.25, random_state=42)
result = []
classifiers = [
    svm.SVR(),
    linear_model.SGDRegressor(),
    linear_model.BayesianRidge(),
    linear_model.LassoLars(),
    DecisionTreeRegressor(random_state=0),
    RandomForestRegressor(random_state=0, n_estimators=100),
    linear_model.PassiveAggressiveRegressor(),
    linear_model.TheilSenRegressor(),
    linear_model.LinearRegression(),
    linear_model.Ridge(alpha=1.0),
    linear_model.ElasticNet(random_state=23)
]

for item in classifiers:
    # print(item)
    clf = item
    clf.fit(x_train, y_train)
    #     print(clf.predict(predictionData),'\n')
    a = [item.__class__.__name__, clf.score(x_test, y_test, sample_weight=None)]
    # print(item, ':    ', a[1])
    result.append(a)

# print(result)

model = RandomForestRegressor(random_state=0,n_estimators=100)
model.fit(x_train, y_train)
import pandas
from textblob import TextBlob

# Reading the training set file
location = "/Users/ayo/PycharmProjects/ACC/data/training_set_rel3.tsv"
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
df.to_csv('/Users/ayo/PycharmProjects/ACC/data/clear_data.csv', sep="\t")


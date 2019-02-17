import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

new_data = pd.read_csv('../data/clear_data.csv', sep='\t')

# sns.countplot(x=new_data['domain1_score'])


def classify_score(x):
    if x >= 0 and x < 10:
        return '<10'
    elif x >= 10 and x < 20:
        return '10To20'
    elif x >= 20 and x < 30:
        return '20To30'
    elif x >= 30 and x < 40:
        return '30To40'
    else:
        return '40To50'

# TODO: GRAPH NOT SHOWING CORRECTLY
#
# new_data['score_class'] = new_data['domain1_score'].apply(classify_score)
#
# a = new_data['score_class'].value_counts()
# b = a.tolist()
# plt.figure(figsize=(8, 6))
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# label = ['<10', '10T020', '20To30', '30To40', '40To50']
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
# plt.pie(a, explode=explode, colors=colors, labels=label, autopct='%1.1f%%', shadow=True, startangle=140)
#
# plt.axis('equal')
# plt.show()

# plt.figure()
# filter_data.hist()
# plt.show()

# sns.countplot(x=filter_data['domain1_score'], data=filter_data)
# se.countplot(x=filter_data['domain1_score'])
# se.violinplot()

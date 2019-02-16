
import pandas as pd

#get the file
loc=r"C:\Users\Devansh\Desktop\Projects\Patient_Characteristics_Survey__PCS___2015.csv"
data=pd.read_csv(loc)
a=data.shape
columns=a[0]
rows=a[1]
l=list()
p=0
for val in data.columns:
    for i in range(rows):
        for a in data.iloc[i:,p]:
            if not a in l:
                l.append(a)
    print(val+":")
    print(l)
    l=list()
    p=p+1
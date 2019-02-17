
import pandas as pd
from sklearn.naive_bayes import GaussianNB

def create_arr(answers,data,rows,columns):
    gnb=GaussianNB()
    person=[]
    y=[]
    for i in range(rows):
        for val in range (columns-1):
            if(val!="Serious Mental Illness"):
                person.append(data.iat[val,i])
        answers.append(person)
        person=[]
    for val in (data["Serious Mental Illness"]):
        y.append(val)
    print(answers[0])
    print(len(answers))
    training_number=int(len(answers)*0.75)
    testing_number=int(len(answers)*0.25)
    print()
    x_train=answers[:training_number]
    y_train=y[:training_number]
    x_test=answers[training_number:]
    y_test=y[training_number:]
    for test in range (testing_number):
        gnb.fit([x_train[test]],[y_train[test]])
    ytrue=0
    yfalse=0
    for test in range (testing_number):
        prediction=gnb.predict([x_train[test]])==y_test[test]
        if(prediction):
            ytrue+=1
        else:
            yfalse+=1
    
    print("True:", ytrue)
    print("False:", yfalse)
     

    
def main():
    #get the file
    loc=r"num.csv"
    data=pd.read_csv(loc)
    a=data.shape
    columns=a[0]
    rows=a[1]
    create_arr([],data,rows,columns) 
       

main()
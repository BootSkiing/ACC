
import pandas as pd

#get the file
loc=r"patients.csv"
# data=pd.read_csv(loc)
# a=data.shape
# columns=a[0]
# rows=a[1]
# l=list()
# p=0
# for val in data.columns:
#     for i in range(rows):
#         for a in data.iloc[i:,p]:
#             if not a in l:
#                 l.append(a)
#     print(val+":")
#     print(l)
#     l=list()
#     p=p+1

names = ['Age Group','Sex','Transgender','Sexual Orientation','Hispanic Ethnicity','Race','Living Situation',
         'Household Composition','Veteran Status','Employment Status','Number Of Hours Worked Each Week',
         'Education Status','Special Education Services','Mental Illness','Intellectual Disability','Autism Spectrum',
         'Other Developmental Disability','Alcohol Related Disorder','Drug Substance Disorder',
         'Mobility Impairment Disorder','Hearing Visual Impairment','Hyperlipidemia','High Blood Pressure','Diabetes',
         'Obesity','Heart Attack','Stroke','Other Cardiac','Pulmonary Asthma','Alzheimer or Dementia','Kidney Disease',
         'Liver Disease','Endocrine Condition','Neurological Condition','Traumatic Brain Injury','Joint Disease',
         'Cancer','Other Chronic Med Condition','No Chronic Med Condition','Unknown Chronic Med Condition','Smokes',
         'Received Smoking Medication','Received Smoking Counseling','Serious Mental Illness','Principal Diagnosis Class',
         'Additional Diagnosis Class','SSI Cash Assistance','SSDI Cash Assistance','Veterans Disability Benefits',
         'Veterans Cash Assistance','Public Assistance Cash Program','Other Cash Benefits','Medicaid and Medicare Insurance',
         'No Insurance','Unknown Insurance Coverage','Medicaid Insurance','Medicaid Managed Insurance','Medicare Insurance',
         'Private Insurance','Child Health Plus Insurance','Other Insurance','Criminal Justice Status',
         'Three Digit Residence Zip Code']

data=pd.read_csv(loc, names=names)

corr = data.corr(method='pearson')
print(corr)


#Imports
import pandas as pd

#Parameters
filelocation = 'C:/datasets'

#Getting Data
train = pd.read_csv(filelocation+'/train.csv')
print(train.shape)
print(train.head(5))

#Data transformation

#Model

#Model Evaluation

#Export results to submission file
#submission = test[['key_id', 'word']]
#submission.to_csv('first_submission.csv', index=False)
#submission.head()

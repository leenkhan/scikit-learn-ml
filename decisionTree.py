import pandas as pd

def read_dataset(fname):
    data = pd.read_csv(fname, index_col=0)
    data.drop(['Name','Ticket','Cabin'], axis=1, inplace=True)
    data['Sex']=(data['Sex']=='male').astype('int')
    labels=data['Embarked'].unique().tolist()
    data['Embarked']=data['Embarked'].apply(lambda n: labels.index(n))
    data = data.fillna(0)
    return data
train = read_dataset('datasets/titanic/train.csv')
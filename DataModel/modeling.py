import pandas as pd

df=pd.read_csv('cardio_train.csv',sep=';')

# Systolic blood pressure 수축기 혈압
# Diastolic blood pressure 이완기 혈압
# Glucose 포도당

df=df.dropna()

if 'id' in df.columns:
  df.drop('id',axis=1,inplace=True)

df.to_json("cardio.json", orient = "records")


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

train, test = train_test_split(df, test_size=0.2, train_size=0.8, random_state=2)
train, val = train_test_split(train, test_size=0.2, train_size=0.8, random_state=2)

test.to_json("metabase.json", orient = "records")

target='cardio'

X_train=train.drop(columns=target)
y_train=train[target]

X_val=val.drop(columns=target)
y_val=val[target]

X_test=test.drop(columns=target)
y_test=test[target]

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print(f'검증세트 정확도 {model.score(X_val, y_val):.3f}')

print(f'테스트세트 정확도 {model.score(X_test, y_test):.3f}')

import pickle

with open('model.pkl','wb') as pickle_model:
    pickle.dump(model, pickle_model)
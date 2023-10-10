import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("<file name>.csv")

label_encoder = LabelEncoder()
df['Job Location - Int'] = label_encoder.fit_transform(df['Job Location'])
model = IsolationForest(n_estimators=50, max_samples='auto', contamination=float(0.1),max_features=1.0)
model.fit(df[['Lower Salary', 'Upper Salary', 'Avg Salary(K)', 'Job Location - Int']])

df['scores']=model.decision_function(df[['Lower Salary', 'Upper Salary', 'Avg Salary(K)', 'Job Location - Int']])
df['anomaly']=model.predict(df[['Lower Salary', 'Upper Salary', 'Avg Salary(K)', 'Job Location - Int']])
print('Anomalies are :')
print(df.loc[df['anomaly'] == -1, ['Lower Salary', 'Upper Salary', 'Avg Salary(K)', 'Job Location']])
df.loc[df['anomaly'] == -1].to_csv('<output_file>.csv', encoding='utf-8', index=False)
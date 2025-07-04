# %%
import pandas as pd

# %%
data_path = '/home/medeiros/Área de trabalho/TrilhaML/9_Machine_Learning_2025/machine-learning-2025/datas/Dados Comunidade (respostas) - dados.csv'
df = pd.read_csv(data_path)
df.head()

# %%
df['Estado que mora atualmente'].unique()

# %%
df = df.replace({
   "Não": 0,
   "Sim": 1
})

# %%
dummy_vars = df.select_dtypes(include=['object']).columns.tolist()# %%
dummy_vars = [var for var in dummy_vars if var not in ['Carimbo de data/hora']]

df_analisys = pd.get_dummies(df[dummy_vars]).astype(int)

num_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()
num_vars = [var for var in num_vars if var not in ['Você se considera uma pessoa feliz?']]

df_analisys[num_vars] = df[num_vars].copy()

df_analisys['Pessoa Feliz'] = df['Você se considera uma pessoa feliz?']
df_analisys

# %%
features = df_analisys.columns.tolist()[:-1]
X = df_analisys[features]
y = df_analisys['Pessoa Feliz'] 

# %%
from sklearn import tree

tdc_model = tree.DecisionTreeClassifier(
   random_state=42,
   min_samples_leaf=5,
)

tdc_model.fit(X, y)

tdc_predict = tdc_model.predict(X)
tdc_proba = tdc_model.predict_proba(X)[:,1]

 # %%
from sklearn import metrics

tdc_acc = metrics.accuracy_score(df_predict['Pessoa Feliz'], tdc_predict)
tdc_precisao = metrics.precision_score(df_predict['Pessoa Feliz'], tdc_predict)
tdc_model_recall = metrics.recall_score(df_predict['Pessoa Feliz'], tdc_predict)

# %%
tdc_roc = metrics.roc_curve(df_predict['Pessoa Feliz'], tdc_proba)
tdc_roc

import matplotlib.pyplot as plt
plt.plot(tdc_roc[0], tdc_roc[1], 'o-')

# %%
from sklearn import naive_bayes

nb = naive_bayes.GaussianNB()
nb.fit(X, y)

nb_predict = nb.predict(X)
nb_proba = nb.predict_proba(X)[:,1]

# %%
nb_acc = metrics.accuracy_score(df_predict['Pessoa Feliz'], nb_predict)
nb_precisao = metrics.precision_score(df_predict['Pessoa Feliz'], nb_predict)
nb_model_recall = metrics.recall_score(df_predict['Pessoa Feliz'], nb_predict)

# %%
nb_roc = metrics.roc_curve(df_predict['Pessoa Feliz'], nb_proba)

import matplotlib.pyplot as plt
plt.plot(nb_roc[0], nb_roc[1], 'o-')

# %%
from sklearn import linear_model

rlog_model = linear_model.LogisticRegression(
   max_iter=10000,
   penalty=None,
   fit_intercept=True
)

rlog_model.fit(X, y)

rlog_predict = rlog_model.predict(X)
rlog_proba = rlog_model.predict_proba(X)[:,1]

rlog_acc = metrics.accuracy_score(df_predict['Pessoa Feliz'], rlog_predict)
rlog_recall = metrics.recall_score(df_predict['Pessoa Feliz'], rlog_predict)
rlog_precision = metrics.precision_score(df_predict['Pessoa Feliz'], rlog_predict)

# %%
rlog_roc = metrics.roc_curve(df_predict['Pessoa Feliz'], rlog_proba)

import matplotlib.pyplot as plt
plt.plot(rlog_roc[0], rlog_roc[1], 'o-')

# %%
pd.Series({
   'model': rlog_model,
   'features': features,
}).to_pickle('model_feliz.pkl')

# %%
dummy_vars

# %%
df_analisys.columns.tolist()
# %%
dummy_vars
# %%

# %%
import pandas as pd

# %%
data_path = '/home/medeiros/Área de trabalho/TrilhaML/9_Machine_Learning_2025/machine-learning-2025/datas/Dados Comunidade (respostas) - dados.csv'
df = pd.read_csv(data_path)
df.head()

# %%
df.shape

# %%
df.columns.tolist()

# %%
df = df.replace({
   "Não": 0,
   "Sim": 1
})

df
# %%
dummy_vars = df.select_dtypes(include=['object']).columns.tolist()

# %%
for col in dummy_vars:
   print(f'{df[[col]].value_counts()}\n')

# %%
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

arvore = tree.DecisionTreeClassifier(
   random_state=42,
   min_samples_leaf=5,
)

arvore.fit(X, y)

# %%
arvore_predict = arvore.predict(X)


# %%

df_predict = df_analisys[['Pessoa Feliz']]
df_predict['Predict'] = arvore_predict

df_predict
# %%
df_predict['Fator'] = df_predict['Pessoa Feliz'] == df_predict['Predict']
df_predict

# %%
print(len(df_predict['Fator']))
print(df_predict['Fator'].sum())
print(df_predict['Fator'].mean())

# %%
pd.crosstab(df_predict['Pessoa Feliz'], df_predict['Predict'])

# %%
print(f'{(16/(16+19))*100:.2f}%')

# %%
arvore.predict_proba(X)[:,1]

# %%
df_predict['Proba'] = arvore.predict_proba(X)[:,1]
# %%
df_predict

# %%
from sklearn import metrics

acc_arvore = metrics.accuracy_score(df_predict['Pessoa Feliz'], df_predict['Predict'])
acc_arvore

# %%
arvore_precisao = metrics.precision_score(df_predict['Pessoa Feliz'], df_predict['Predict'])
arvore_precisao

# %%
arvore_recall = metrics.recall_score(df_predict['Pessoa Feliz'], df_predict['Predict'])
arvore_recall

# %%
roc = metrics.roc_curve(df_predict['Pessoa Feliz'], df_predict['Proba'])
roc

# %%
len(roc)

# %%
roc[0]

# %%
roc[1]

# %%
import matplotlib.pyplot as plt
plt.plot(roc[0], roc[1], 'o-')

# %%
roc[2]

# %%
auc = metrics.roc_auc_score(df_predict['Pessoa Feliz'], df_predict['Proba'])
auc

# %%
df_predict['Proba'].value_counts()

# %%
from sklearn import naive_bayes

nb = naive_bayes.GaussianNB()
nb.fit(X, y)

# %%
nb_predict = nb.predict(X)
nb_predict

# %%
nb_precision = metrics.precision_score(df_predict['Pessoa Feliz'], nb_predict)
nb_precision

# %%

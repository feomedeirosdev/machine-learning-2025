import streamlit as st
import pandas as pd

model = pd.read_pickle('model_feliz.pkl')

st.markdown('# Descubra a Felicidade')

redes = ['LinkedIn', 'Twitch', 'YouTube', 'Instagram', 'Amigos', 'Twitter / X', 'Outra rede social']
cursos = ['0', '1', '2', '3', 'Mais que 3']
estado = ['AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MT', 'PA', 'PB', 'PE', 'PR', 'RJ', 'RN', 'RS', 'SC', 'SP']
formacao = ['Exatas', 'Biológicas', 'Humanas']
tempo = ['Não atuo', 'De 0 a 6 meses','De 6 meses a 1 ano','De 1 ano a 2 anos','de 2 anos a 4 anos','Mais de 4 anos']
carreira = ['Iniciante','Júnior','Pleno','Sênior','Especialista','Coordenação','Gerência','Diretoria','C-Level']

# Coleta das respostas
qtd_cursos = st.selectbox('Quantos cursos acompanhou do Téo Me Why?', options=cursos)
como_conheceu = st.selectbox('Como conheceu o Téo Me Why?', options=redes)

col1, col2, col3 = st.columns(3)
with col1: 
    video_game = st.radio('Curte games?', ['Sim', 'Não'])
    futebol = st.radio('Curte futebol?', ['Sim', 'Não'])

with col2: 
    livros = st.radio('Curte livros?', ['Sim', 'Não'])
    tabuleiro = st.radio('Curte jogos de tabuleiro?', ['Sim', 'Não'])

with col3: 
    f1 = st.radio('Curte jogos de fórmula 1?', ['Sim', 'Não'])
    mma = st.radio('Curte jogos de MMA?', ['Sim', 'Não'])

col1, col2, col3 = st.columns(3)
with col1:
    idade = st.number_input('Qual sua Idade:', 18, 100)
    tempo_atuacao = st.selectbox('Tempo que atua na área de dados', options=tempo)
   
with col2:
    estado_mora = st.selectbox('Estado que mora atualmente', options=estado)
    senioridade = st.selectbox('Posição da cadeira (senioridade)', options=carreira)

with col3:
    formacao_area = st.selectbox('Área de Formação', options=formacao)

# Montagem do dicionário com os valores selecionados
data = {
    'Como conheceu o Téo Me Why?': como_conheceu,
    'Quantos cursos acompanhou do Téo Me Why?': qtd_cursos,
    'Curte games?': video_game,
    'Curte futebol?': futebol,
    'Curte livros?': livros,
    'Curte jogos de tabuleiro?': tabuleiro,
    'Curte jogos de fórmula 1?': f1,
    'Curte jogos de MMA?': mma,
    'Idade': idade,
    'Estado que mora atualmente': estado_mora,
    'Área de Formação': formacao_area,
    'Tempo que atua na área de dados': tempo_atuacao,
    'Posição da cadeira (senioridade)': senioridade
}

# Criação do DataFrame
df = pd.DataFrame([data]).replace({'Não': 0, 'Sim': 1})

# Variáveis categóricas para dummificação
dummy_vars = [
    'Como conheceu o Téo Me Why?',
    'Quantos cursos acompanhou do Téo Me Why?',
    'Estado que mora atualmente',
    'Área de Formação',
    'Tempo que atua na área de dados',
    'Posição da cadeira (senioridade)'
]

# One-hot encoding
df = pd.get_dummies(df, columns=dummy_vars).astype(int)

# Template fixo com todas as colunas esperadas (caso alguma categoria não apareça)
df_columns = [
    'Como conheceu o Téo Me Why?_Amigos',
    'Como conheceu o Téo Me Why?_Instagram',
    'Como conheceu o Téo Me Why?_LinkedIn',
    'Como conheceu o Téo Me Why?_Outra rede social',
    'Como conheceu o Téo Me Why?_Twitch',
    'Como conheceu o Téo Me Why?_Twitter / X',
    'Como conheceu o Téo Me Why?_YouTube',
    'Quantos cursos acompanhou do Téo Me Why?_0',
    'Quantos cursos acompanhou do Téo Me Why?_1',
    'Quantos cursos acompanhou do Téo Me Why?_2',
    'Quantos cursos acompanhou do Téo Me Why?_3',
    'Quantos cursos acompanhou do Téo Me Why?_Mais que 3',
    'Estado que mora atualmente_AM',
    'Estado que mora atualmente_BA',
    'Estado que mora atualmente_CE',
    'Estado que mora atualmente_DF',
    'Estado que mora atualmente_ES',
    'Estado que mora atualmente_GO',
    'Estado que mora atualmente_MA',
    'Estado que mora atualmente_MG',
    'Estado que mora atualmente_MT',
    'Estado que mora atualmente_PA',
    'Estado que mora atualmente_PB',
    'Estado que mora atualmente_PE',
    'Estado que mora atualmente_PR',
    'Estado que mora atualmente_RJ',
    'Estado que mora atualmente_RN',
    'Estado que mora atualmente_RS',
    'Estado que mora atualmente_SC',
    'Estado que mora atualmente_SP',
    'Área de Formação_Biológicas',
    'Área de Formação_Exatas',
    'Área de Formação_Humanas',
    'Tempo que atua na área de dados_De 0 a 6 meses',
    'Tempo que atua na área de dados_De 1 ano a 2 anos',
    'Tempo que atua na área de dados_De 6 meses a 1 ano',
    'Tempo que atua na área de dados_Mais de 4 anos',
    'Tempo que atua na área de dados_Não atuo',
    'Tempo que atua na área de dados_de 2 anos a 4 anos',
    'Posição da cadeira (senioridade)_C-Level',
    'Posição da cadeira (senioridade)_Coordenação',
    'Posição da cadeira (senioridade)_Diretoria',
    'Posição da cadeira (senioridade)_Especialista',
    'Posição da cadeira (senioridade)_Gerência',
    'Posição da cadeira (senioridade)_Iniciante',
    'Posição da cadeira (senioridade)_Júnior',
    'Posição da cadeira (senioridade)_Pleno',
    'Posição da cadeira (senioridade)_Sênior',
    'Curte games?',
    'Curte futebol?',
    'Curte livros?',
    'Curte jogos de tabuleiro?',
    'Curte jogos de fórmula 1?',
    'Curte jogos de MMA?',
    'Idade'
]

# Garantindo que todas as colunas existam
df_template = pd.DataFrame(columns=df_columns).fillna(0).astype(int)
df = pd.concat([df_template, df]).fillna(0).astype(int)

proba = model['model'].predict_proba(df[model['features']])[:,1][0]

# Mostra a probabilidade final
if proba > 0.7:
   st.success(f"Você é uma pessoa Feliz, Aproveite a Vida!!! ({proba*100:.2f}%)")
elif proba > 0.4:
   st.warning(f"Você é uma pessoa meio Feliz, Aproveite mais a Vida!!! ({proba*100:.2f}%)")
else:
   st.error(f"Você é uma pessoa Triste, procure se cuidar ({proba*100:.2f}%)")

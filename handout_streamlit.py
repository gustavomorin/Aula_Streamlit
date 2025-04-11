# GUIA COMPLETO DE STREAMLIT - DO ZERO AO AVANÇADO 💻
# Inclui exemplos de todos os comandos, blocos com código visível, e aplicações avançadas reais

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import datetime
import os
import pydeck as pdk
from PIL import Image
import time

st.set_page_config(page_title="Guia Completo de Streamlit", layout="wide")

pagina = st.sidebar.selectbox(
    "📚 Navegue pelo conteúdo",
    [
        "1. Introdução ao Streamlit",
        "2. Elementos Básicos",
        "3. Interações com o Usuário",
        "4. Upload e Visualização de Dados",
        "5. Gráficos com Matplotlib e Plotly",
        "6. Data e Hora",
        "7. Layouts e Containers",
        "8. Mapas com Pydeck",
        "9. Session State",
        "10. Upload de Imagem",
        "11. Barra de Progresso e Espera",
        "12. KPIs com st.metric",
        "13. Projeto Final: Dashboard PVCP",
        "14. Deploy com Streamlit Cloud",
        "15. Projeto: Web Scraping de Notícias",
        "16. Projeto: Dashboard Financeiro",
        "17. Projeto: Predição com ML (Iris Dataset)",
        "18. Projeto Final da Trilha"
    ]
)

# PÁGINA 1 - Introdução
if pagina == "1. Introdução ao Streamlit":
    st.title("🚀 Bem-vindo ao Guia Interativo de Streamlit!")
    st.markdown("""
Este app ensina **do zero ao avançado** como usar o [Streamlit](https://streamlit.io/).

Você verá:
- Como construir apps com elementos visuais
- Como interagir com usuários
- Como visualizar e manipular dados
- Como persistir estado e usar arquivos
- Como publicar seu app online
    """)
    st.code("""
import streamlit as st
st.write("Olá mundo!")
""")
    st.write("Olá mundo!")

# PÁGINA 2 - Elementos Básicos
elif pagina == "2. Elementos Básicos":
    st.header("🧱 Elementos Básicos")
    st.title("Título Principal")
    st.code("st.title(\"Título Principal\")")
    st.header("Header")
    st.code("st.header(\"Header\")")
    st.subheader("Subheader")
    st.code("st.subheader(\"Subheader\")")
    st.text("Texto simples")
    st.code("st.text(\"Texto simples\")")
    st.markdown("Texto com **formatação** em Markdown")
    st.code("st.markdown(\"Texto com **formatação** em Markdown\")")
    st.latex(r"e^{i\pi} + 1 = 0")
    st.code("st.latex(r\"e^{i\\pi} + 1 = 0\")")
    st.caption("Este é um caption")
    st.code("st.caption(\"Este é um caption\")")

# PÁGINA 3 - Interações
elif pagina == "3. Interações com o Usuário":
    st.header("🎛️ Inputs e Interações")
    nome = st.text_input("Seu nome")
    st.code("nome = st.text_input(\"Seu nome\")")
    idade = st.slider("Sua idade", 0, 120, 25)
    st.code("idade = st.slider(\"Sua idade\", 0, 120, 25)")
    sexo = st.radio("Sexo", ["Masculino", "Feminino", "Outro"])
    st.code("sexo = st.radio(\"Sexo\", [\"Masculino\", \"Feminino\", \"Outro\"])" )
    profissao = st.selectbox("Profissão", ["Engenheiro", "Arquiteto", "Designer", "Outro"])
    st.code("profissao = st.selectbox(\"Profissão\", [...])")
    hobbies = st.multiselect("Escolha hobbies", ["Leitura", "Esportes", "Música", "Viagens"])
    st.code("hobbies = st.multiselect(\"Escolha hobbies\", [...])")
    aceitar = st.checkbox("Aceito os termos")
    st.code("aceitar = st.checkbox(\"Aceito os termos\")")
    if st.button("Enviar"):
        st.success(f"Bem-vindo, {nome}! Você tem {idade} anos, é {sexo.lower()} e trabalha como {profissao}.")

# PÁGINA 4 - Upload e Visualização de Dados
elif pagina == "4. Upload e Visualização de Dados":
    st.header("📂 Upload de Arquivos")
    arquivo = st.file_uploader("Envie um CSV")
    st.code("arquivo = st.file_uploader(\"Envie um CSV\")")
    if arquivo:
        df = pd.read_csv(arquivo)
        st.dataframe(df)
        st.code("df = pd.read_csv(arquivo); st.dataframe(df)")

# PÁGINA 5 - Gráficos
elif pagina == "5. Gráficos com Matplotlib e Plotly":
    st.header("📊 Gráficos")
    df = pd.DataFrame({"Ano": [2020, 2021, 2022], "Vendas": [100, 250, 175]})
    st.line_chart(df.set_index("Ano"))
    st.code("st.line_chart(df.set_index(\"Ano\"))")
    fig = px.bar(df, x="Ano", y="Vendas", title="Vendas por Ano")
    st.plotly_chart(fig)
    st.code("fig = px.bar(...); st.plotly_chart(fig)")

# PÁGINA 6 - Datas
elif pagina == "6. Data e Hora":
    st.header("📅 Inputs de Data")
    data = st.date_input("Selecione uma data")
    st.code("data = st.date_input(\"Selecione uma data\")")
    hora = st.time_input("Selecione um horário")
    st.code("hora = st.time_input(\"Selecione um horário\")")

# PÁGINA 7 - Layout
elif pagina == "7. Layouts e Containers":
    st.header("📐 Layouts")
    with st.container():
        st.write("Este é um container")
        st.code("with st.container(): ...")
    col1, col2 = st.columns(2)
    col1.write("Coluna 1")
    col2.write("Coluna 2")
    st.code("col1, col2 = st.columns(2)")

# PÁGINA 8 - Pydeck
elif pagina == "8. Mapas com Pydeck":
    st.header("🗺️ Mapa Interativo")
    df = pd.DataFrame({"lat": [-23.56], "lon": [-46.63]})
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(latitude=-23.56, longitude=-46.63, zoom=11),
        layers=[pdk.Layer("ScatterplotLayer", data=df, get_position='[lon, lat]', get_color='[0, 100, 255, 160]', get_radius=100)]
    ))
    st.code("st.pydeck_chart(...) com ScatterplotLayer")

# PÁGINA 9 - Session State
elif pagina == "9. Session State":
    st.header("💾 Memória de Sessão")
    if "count" not in st.session_state:
        st.session_state.count = 0
    if st.button("Somar"):
        st.session_state.count += 1
    st.write("Contador:", st.session_state.count)
    st.code("st.session_state['count'] += 1")

# PÁGINA 10 - Upload de Imagem
elif pagina == "10. Upload de Imagem":
    st.header("🖼️ Upload de Imagem")
    img_file = st.file_uploader("Envie uma imagem", type=["png", "jpg"])
    if img_file:
        img = Image.open(img_file)
        st.image(img, use_column_width=True)
        st.code("img = Image.open(img_file); st.image(img)")

# PÁGINA 11 - Progresso
elif pagina == "11. Barra de Progresso e Espera":
    st.header("⏳ Barra de Progresso")
    progresso = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progresso.progress(i + 1)
    st.success("Concluído!")
    st.code("progresso = st.progress(0); progresso.progress(i)")

# PÁGINA 12 - Métricas
elif pagina == "12. KPIs com st.metric":
    st.header("📈 KPIs")
    col1, col2, col3 = st.columns(3)
    col1.metric("Vendas", "$500K", "+5%")
    col2.metric("Lucro", "$120K", "+2%")
    col3.metric("Conversão", "3.2%", "-0.5%")
    st.code("st.metric(...) para KPIs")

# (código anterior permanece inalterado)

# PÁGINA 13 - Projeto PVCP
elif pagina == "13. Projeto Final: Dashboard PVCP":
    st.header("🏗️ Projeto Final: Dashboard de Produtividade - PVCP")
    st.markdown("""
    O objetivo deste projeto é visualizar os dados de produtividade de colaboradores em projetos reais da PVCP. Você poderá:
    - Filtrar por colaborador, projeto e intervalo de datas
    - Ver métricas agregadas de produtividade
    - Gerar gráficos por categoria
    - Analisar a base detalhadamente
    """)

    path = "pvcp_horas.csv"
    if os.path.exists(path):
        df = pd.read_csv(path, parse_dates=["Data"])
        st.write("### Visualização Inicial da Base")
        st.dataframe(df.head())
        st.code("df = pd.read_csv('pvcp_horas.csv', parse_dates=['Data'])")

        st.sidebar.subheader("🎛️ Filtros")
        data_ini = st.sidebar.date_input("Data inicial", df["Data"].min().date())
        data_fim = st.sidebar.date_input("Data final", df["Data"].max().date())
        projetos = st.sidebar.multiselect("Projetos", df["Projeto"].unique(), default=list(df["Projeto"].unique()))
        colabs = st.sidebar.multiselect("Colaboradores", df["Colaborador"].unique(), default=list(df["Colaborador"].unique()))

        df_filt = df[
            (df["Data"] >= pd.to_datetime(data_ini)) &
            (df["Data"] <= pd.to_datetime(data_fim)) &
            (df["Projeto"].isin(projetos)) &
            (df["Colaborador"].isin(colabs))
        ]

        st.code("""
df_filt = df[
    (df["Data"] >= pd.to_datetime(data_ini)) &
    (df["Data"] <= pd.to_datetime(data_fim)) &
    (df["Projeto"].isin(projetos)) &
    (df["Colaborador"].isin(colabs))
]
""")

        st.subheader("📊 KPIs Gerais")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Horas", f"{df_filt['Horas'].sum():.1f} h")
        col2.metric("Média por Registro", f"{df_filt['Horas'].mean():.1f} h")
        col3.metric("Número de Registros", len(df_filt))
        st.code("st.metric(...) para KPIs")

        st.subheader("📌 Horas por Projeto")
        st.bar_chart(df_filt.groupby("Projeto")["Horas"].sum())
        st.code("st.bar_chart(df_filt.groupby('Projeto')['Horas'].sum())")

        st.subheader("👥 Horas por Colaborador")
        st.bar_chart(df_filt.groupby("Colaborador")["Horas"].sum())

        st.subheader("⚙️ Horas por Atividade")
        st.bar_chart(df_filt.groupby("Atividade")["Horas"].sum())

        st.subheader("📋 Tabela Detalhada")
        st.dataframe(df_filt)
        st.code("st.dataframe(df_filt)")
    else:
        st.warning("O arquivo 'pvcp_horas.csv' não foi encontrado na pasta atual. Por favor, coloque-o ao lado do arquivo .py.")

# (código anterior permanece igual)

# PROJETO 15 - Web Scraping (expandido)
if pagina == "15. Projeto: Web Scraping de Notícias":
    st.header("🌐 Web Scraping de Notícias (G1)")
    qtd = st.slider("Quantas manchetes mostrar?", min_value=1, max_value=15, value=5)
    palavra_chave = st.text_input("Filtrar manchetes por palavra-chave (opcional)")
    try:
        import requests
        from bs4 import BeautifulSoup
        url = "https://g1.globo.com"
        st.code("url = 'https://g1.globo.com'")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = [h.text.strip() for h in soup.find_all('a', class_='feed-post-link') if h.text.strip() != ""]
        if palavra_chave:
            headlines = [h for h in headlines if palavra_chave.lower() in h.lower()]
        st.subheader("📰 Manchetes:")
        for i, h in enumerate(headlines[:qtd]):
            st.markdown(f"**{i+1}. {h}**")
        if len(headlines) == 0:
            st.warning("Nenhuma manchete encontrada com essa palavra.")
    except:
        st.warning("Erro ao carregar dados. Biblioteca requests ou bs4 não instalada.")

# PROJETO 16 - Dashboard Financeiro (expandido)
elif pagina == "16. Projeto: Dashboard Financeiro":
    st.header("💰 Dashboard Financeiro Interativo")
    st.markdown("Faça simulações alterando as variáveis de receita e lucro.")

    anos = list(range(2019, 2025))
    receita_base = st.number_input("Receita inicial (2019)", value=50000, step=5000)
    crescimento = st.slider("Crescimento percentual ao ano (%)", 0, 30, 10)
    margem_lucro = st.slider("Margem de lucro (%)", 0, 100, 20)

    receita = [receita_base * ((1 + crescimento/100)**i) for i in range(len(anos))]
    lucro = [r * margem_lucro / 100 for r in receita]
    df = pd.DataFrame({"Ano": anos, "Receita": receita, "Lucro": lucro})
    df["Margem %"] = df["Lucro"] / df["Receita"] * 100

    st.dataframe(df)
    fig = px.area(df, x="Ano", y=["Receita", "Lucro"], markers=True, title="Simulação Financeira")
    st.plotly_chart(fig)
    st.code("df = DataFrame com Receita simulada * crescimento, Lucro = Receita * margem")

# PROJETO 17 - Machine Learning (expandido)
elif pagina == "17. Projeto: Predição com ML (Iris Dataset)":
    st.header("🤖 Classificação de Espécies de Flores (Iris Dataset)")
    st.markdown("Ajuste os parâmetros e veja a predição ao vivo. Também visualize as probabilidades para cada classe!")

    from sklearn.datasets import load_iris
    from sklearn.ensemble import RandomForestClassifier

    data = load_iris()
    clf = RandomForestClassifier()
    clf.fit(data.data, data.target)

    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.slider("Comprimento da sépala", 4.0, 8.0, 5.0, 0.1)
        sepal_width = st.slider("Largura da sépala", 2.0, 5.0, 3.0, 0.1)
    with col2:
        petal_length = st.slider("Comprimento da pétala", 1.0, 7.0, 3.5, 0.1)
        petal_width = st.slider("Largura da pétala", 0.1, 2.5, 1.0, 0.1)

    amostra = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = clf.predict(amostra)[0]
    prob = clf.predict_proba(amostra)[0]

    st.success(f"🌸 A flor com essas medidas é da espécie: **{data.target_names[pred]}**")

    st.markdown("### 🔍 Probabilidades para cada espécie:")
    prob_df = pd.DataFrame({"Espécie": data.target_names, "Probabilidade": prob})
    st.bar_chart(prob_df.set_index("Espécie"))

# (continuação do código anterior)

elif pagina == "18. Projeto Final da Trilha":
    st.header("🎓 Projeto Final da Trilha de Desenvolvimento Web")
    st.markdown("""
Parabéns por chegarem até aqui! Após idealizar o seu e-commerce no Figma e construir os primeiros componentes interativos com Streamlit, chegou a hora de consolidar tudo em uma entrega de alto impacto: **o dashboard financeiro final da sua loja virtual**. 🧠💼

### 🧩 Integração Total
O projeto final deve se basear em **tudo o que foi construído até agora**:
- Produto escolhido na primeira aula
- Identidade visual definida
- Layout e lógica de negócios
- Funcionalidades interativas desenvolvidas ao longo do handout

### 🎯 Objetivo do Entregável
Você deve construir um dashboard completo e interativo que simule o desempenho financeiro do seu e-commerce. Esse painel deve permitir ao usuário:
- Filtrar produtos e períodos de tempo
- Simular crescimento de vendas e variação de custos
- Visualizar KPIs e gráficos como:
    - Receita e lucro por mês
    - Margem de lucro
    - Comparação entre produtos
    - Análise por canal de venda (se quiser incrementar)

### 🛠️ Funcionalidades esperadas:
- Sliders e caixas numéricas para modificar inputs (crescimento, margem, preço médio, etc.)
- Filtros por data e produto
- Uso de `st.metric`, `plotly`, `dataframe`, `st.tabs`, `st.sidebar`, etc.
- Visualização bonita, clara e organizada
- Paleta de cores e identidade visual coerente com o protótipo do Figma

### 💡 Criatividade e Integração
Quanto mais **funcional**, **criativo** e **integrado ao projeto original**, melhor será sua entrega. Use tudo que aprendeu até aqui para construir algo que realmente pareça um painel real de gestão de um e-commerce. Não precisa usar dados reais — você pode gerar valores aleatórios ou estimados com `np.random`, desde que faça sentido.

---

Essa é sua **última chance de não ficar careca**. Capriche. ✂️🧑‍🦲
    """)

# PÁGINA 14 - Deploy
elif pagina == "14. Deploy com Streamlit Cloud":
    st.header("🚀 Deploy")
    st.markdown("""
1. Crie um repositório no GitHub
2. Suba seu `.py` e `requirements.txt`
3. Acesse [streamlit.io/cloud](https://streamlit.io/cloud)
4. Clique em **New app**
5. Escolha o repo, branch e arquivo, e clique em Deploy
    """)

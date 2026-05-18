# 🎧 Spotify Artist Word Cloud

Projeto em Python que gera uma **nuvem de palavras** e gráficos com os artistas e gêneros mais ouvidos no Spotify, usando a API oficial.

## 🚀 Tecnologias
- Python
- Spotipy
- WordCloud
- Matplotlib

## 📊 Funcionalidades

- ☁️ WordCloud dos artistas mais ouvidos
- 📈 Popularidade global dos top artistas
- 🎵 Distribuição dos gêneros musicais
- 🧠 Análise automática do perfil musical
- 💾 Exportação do dashboard em imagem

## 🎨 Resultado
<p align="center">
  <img src="grafico_spotify.png" width="500">
</p>



## 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
SPOTIPY_CLIENT_ID=seu_client_id
SPOTIPY_CLIENT_SECRET=seu_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

## ▶️ Instalação

```bash
pip install -r requirements.txt
```

## ▶️ Executando

```bash
python main.py
```

## 📌 Objetivo

Projeto desenvolvido para praticar:
- consumo de APIs
- visualização de dados
- manipulação de dados em Python
- geração de dashboards
- integração com IA
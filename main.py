import os
from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
scope = 'user-top-read'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope)
)

results = sp.current_user_top_artists(
    limit=20,
    time_range="short_term" 
)

artists = {}
for artist in results["items"]:
    name = artist["name"]
    artists[name] = artists.get(name, 0) + 1

wc = WordCloud( 
    width=1600, 
    height=1000, 
    background_color="white" 
    ).generate_from_frequencies(artists)

artists_popularity = {}

for artist in results["items"][:5]:
    name = artist["name"]
    pop = artist["popularity"]
    artists_popularity[name] = pop

names = list(artists_popularity.keys())
values = list(artists_popularity.values())

genres = {}
for artist in results["items"]:
    for genre in artist["genres"]:
        genres[genre] = genres.get(genre, 0) + 1


names_genres = list(genres.keys())[:10]
values_genres = list(genres.values())[:10]

top_genres = dict(
    sorted(genres.items(), key=lambda x: x[1], reverse=True)[:7]
)

top_names = list(top_genres.keys())
top_values = list(top_genres.values())

prompt = f"""
Analise o perfil musical abaixo.

Top artistas:
{list(artists.keys())}

Top gêneros:
{top_names}

Popularidade dos artistas:
{artists_popularity}

Faça uma análise:
- divertida
- inteligente
- parecendo um app premium de música
- em português

Fale sobre:
- personalidade musical
- energia das músicas
- padrão de escuta
- possíveis moods
"""

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    analysis = response.text

except Exception:
    analysis = f"""
Seu perfil musical mostra forte presença de {top_names[0]}
e {top_names[1]}, indicando preferência por músicas intensas
e emocionalmente marcantes. Seus artistas mais ouvidos possuem
alta popularidade global e sugerem um gosto moderno, energético
e bastante conectado às tendências atuais.
"""

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 1
axs[0, 0].imshow(wc)
axs[0, 0].axis("off")
axs[0, 0].set_title("Top Artistas")

#  2
axs[0, 1].barh(names, values)
axs[0, 1].set_title("Popularidade Global")

# 3
axs[1, 0].pie(values_genres, labels=names_genres)
axs[1, 0].set_title("Gêneros")

# 4
axs[1, 1].axis("off")
axs[1, 1].text(
    0.5,
    0.5,
    analysis,
    fontsize=13,
    ha="center",
    va="center",
    wrap=True,
    bbox=dict(
        alpha=0.5,
        boxstyle="round,pad=1"
    )
)
axs[1, 1].set_title("Análise musical")

plt.tight_layout()
plt.savefig("grafico_spotify.png", dpi=300)
plt.show()
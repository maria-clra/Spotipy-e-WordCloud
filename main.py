import os
from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Top artistas
#Popularidade
#Gêneros
#Comparação (tempo curto vs longo)

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


names_genres = list(genres.keys())
values_genres = list(genres.values())

top_genres = dict(
    sorted(genres.items(), key=lambda x: x[1], reverse=True)[:7]
)

top_names = list(top_genres.keys())
top_values = list(top_genres.values())

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
axs[1, 1].plot(top_names, top_values)
axs[1, 1].set_title("Top 7 Gêneros")

plt.tight_layout()
plt.savefig("grafico_spotify.png", dpi=300)
plt.show()
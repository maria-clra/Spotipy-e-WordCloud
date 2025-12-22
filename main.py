import os
from dotenv import load_dotenv
load_dotenv(".env")
import spotipy
import sys
from spotipy.oauth2 import SpotifyOAuth
from wordcloud import WordCloud
import matplotlib.pyplot as plt


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

plt.imshow(wc)
plt.axis("off")
plt.show()
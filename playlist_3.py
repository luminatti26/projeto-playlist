import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

#Inputs para logar

username = 'lu.minatti'
client_id = '659c88a0051543a3a98493fb5a6a9649'
client_secret = '1bb5305b39824f4eb3f7eb7d38af9106'
scope = 'playlist-modify-public'

#este será o "cursor"

token = SpotifyOAuth(client_id,
                     client_secret,
                     redirect_uri='http://localhost:8080/callback', 
                     scope=scope,
                     username=username)

spotify = spotipy.Spotify(auth_manager=token)

#Criar e nomear a playlist

playlist_nome = input("Digite o nome da sua playlist: ")
Playlist_descr = input("Digite uma descrição para a sua playlist: ")

spotify.user_playlist_create(user=username,
                             name=playlist_nome,
                             public=True,
                             collaborative=False,
                             description=Playlist_descr)

print('Playlist criada!')

lista_artista = []

lista_musicas = []

#selecionar os artistas

for index in range(0, 3, 1):
    resultado = input("Digite até 3 artista para adcionar a playlist: ")
    lista_artista.append(resultado)
    
#filtrar as musicas

for index in range(0, len(lista_artista), 1):
    resultado = spotify.search(q=lista_artista[index], limit=5)
    for i, t in enumerate(resultado['tracks']['items']):
        lista_musicas.append(str(t['id'].strip( 'u' )))
        print("adicionando a musica", t['id'], t['name'])

    
pre_playlist = spotify.user_playlists(user=username, )
playlist = pre_playlist['items'][0]['id']

#adicionar musicas a playlist

spotify.user_playlist_add_tracks(user=username,playlist_id=playlist, tracks=lista_musicas)

print('Musicas adicionadas!')
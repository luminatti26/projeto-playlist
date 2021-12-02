import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
#Inputs para logar
scope = 'playlist-modify-public'
username = input("Digite username: ")
client_id = input("Digite client_id: ")
client_secret = input("Digite client_secret: ")

token = SpotifyOAuth(client_id,
                     client_secret,
                     redirect_uri='http://localhost:8080/callback', 
                     scope=scope, 
                     username=username)
#este será o "cursor"

spotify_object = spotipy.Spotify(auth_manager=token)

#Criar e nomear a playlist

playlist_nome = input("Digite o nome da sua playlist: ")
Playlist_descr = input("Digite uma descrição para a sua playlist: ")

spotify_object.user_playlist_create(user=username,
                                    name=playlist_nome,
                                    public=True,
                                    collaborative=False,
                                    description=Playlist_descr)

print('Playlist criada!')
#Adicionando musicas a playlist    
#                                
user_input = input("digite o nome da musica que deseja: ")

lista_musicas = []

while user_input != 'sair':
    resultado = spotify_object.search(q=user_input)
    '''print(json.dumps(resultado, sort_keys=4, indent=4))'''
    lista_musicas.append(resultado['tracks']['items'][0]['uri'])
    user_input = input("digite o nome da musica que deseja: ")

pre_playlist = spotify_object.user_playlists(user=username, )
playlist = pre_playlist['items'][0]['id']

spotify_object.user_playlist_add_tracks(user=username,playlist_id=playlist, tracks=lista_musicas)

print('Musicas adicionadas!')
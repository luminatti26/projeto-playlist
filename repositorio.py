import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json



def get_token(client_id, client_secret, username):
    scope = 'playlist-modify-public'

    token = SpotifyOAuth(client_id,
                         client_secret,
                         redirect_uri='http://127.0.0.1:5000', 
                         scope=scope, 
                         username=username)

    spotify = spotipy.Spotify(auth_manager=token)

    return spotify


def criar_playlist(spotify):
    playlist_nome = input("Digite o nome da sua playlist: ")
    Playlist_descr = input("Digite uma descrição para a sua playlist: ")

    spotify.user_playlist_create(user=username,
                             name=playlist_nome,
                             public=True,
                             collaborative=False,
                             description=Playlist_descr)

    return print('Playlist criada!')


def criar_lista_artista():
    lista_artista = []
    for index in range(0, 3, 1):
        resultado = input("Digite até 3 artista para adcionar a playlist: ")
        lista_artista.append(resultado)
    print("artistas adicinionados")
    return lista_artista    


def criar_lista_musica(spotify, lista_artista):
    lista_musicas = []
    for index in range(0, len(lista_artista), 1):
        resultado = spotify.search(q=lista_artista[index], limit=5)
    for i, t in enumerate(resultado['tracks']['items']):
        lista_musicas.append(str(t['id'].strip( 'u' )))
        print("adicionando a musica", t['id'], t['name'])

    return lista_musicas


def finalizar_playlist(spotify, lista_musicas):
    pre_playlist = spotify.user_playlists(user=username, )
    playlist = pre_playlist['items'][0]['id']

    spotify.user_playlist_add_tracks(user=username,playlist_id=playlist, tracks=lista_musicas)

    print('Musicas adicionadas!')

    



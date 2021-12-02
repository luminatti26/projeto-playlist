import sys
import spotipy
import spotipy.util as util

artistasFile = open('artistas.txt', 'r')
artista = [x.strip('\n') for x in artistasFile.readlines()]

tracks = []

numeroArtistas = len(artista)

username = 'lu.minatti'
scope = 'playlist-modify-public'
playlist_id = '1VJlojEG4FBrkM4r24GbqN'


token = util.prompt_for_user_token(username,
                                   scope,
                                   client_id='659c88a0051543a3a98493fb5a6a9649',
                                   client_secret='1bb5305b39824f4eb3f7eb7d38af9106',
                                   redirect_uri='http://localhost:8080/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    for x in range(0, numeroArtistas):
        result = sp.search(artista[x], limit=4)
        for i, t in enumerate(result['tracks']['items']):
            tracks.append(str(t['id'].strip( 'u' )))
            print("adicionando a track", t['id'], t['name'])
    while tracks:
        try:
            result = sp.user_playlist_add_tracks(username, playlist_id, tracks[:1])
        except:
            print("erro")
        tracks = tracks[1:]
    
else:
    print("Can't get token for", username)

  
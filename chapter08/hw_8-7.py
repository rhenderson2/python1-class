# homework assignment section 8-7
def make_album(artist_name, album_title, tracks=None):
    album = {'name': artist_name, 'title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

album01 = make_album('madona', 'immaculate concpetion')
print(album01)
album02 = make_album('newsboys', 'step up to the microphone')
print(album02)
album03 = make_album('dc talk', 'supernatural')
print(album03)
album04 = make_album('u2', 'boy', 15)
print(album04)


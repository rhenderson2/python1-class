# homework assignment section 8-8
def make_album(artist_name, album_title):
    """Return an artist and album neatly formatted."""
    album = {'name': artist_name, 'title': album_title}
    return album

while True:
    print("\nPlease tell me an artist's name and album title: ")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist's name: ")
    if a_name == 'q':
        break
    a_title = input("Album title: ")
    if a_title == 'q':
        break

    artist_album = make_album(a_name, a_title)
    print(artist_album)


#album01 = make_album('madona', 'immaculate concpetion')
#print(album01)
#album02 = make_album('newsboys', 'step up to the microphone')
#print(album02)

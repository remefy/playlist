from models import ListOfArtists


class ArtistsDBAdapter:
    def __init__(self):
        self.artists = []
        self.last_id = 1

    def prepare(self):
        pass

    def get_all_artists(self):
        return self.artists

    def save_new_artist(self, artist: ListOfArtists):
        artist.id = self.last_id
        self.artists.append(artist)
        self.last_id += 1

    def delete_artist(self, id):
        for artist in self.artists:
            if artist.id == id:
                self.artists.remove(artist)
                break

    def search_artist(self, name):
        for artist in self.artists:
            if artist.songstitle.find(name):
                return artist

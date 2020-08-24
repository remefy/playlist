from models import ListOfSongs


class SongsDBAdapter:
    def __init__(self):
        self.songs = []
        self.last_id = 1

    def prepare(self):
        pass

    def get_all_songs(self):
        return self.songs

    def save_new_song(self, song: ListOfSongs):
        song.id = self.last_id
        self.songs.append(song)
        self.last_id += 1

    def delete_song(self, id):
        for song in self.songs:
            if song.id == id:
                self.songs.remove(song)
                break

    def search_song(self, name):
        for song in self.songs:
            if song.songstitle.find(name):
                return song

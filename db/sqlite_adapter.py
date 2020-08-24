import sqlite3
from db.adapter_for_artists import ArtistsDBAdapter
from db.adapter_for_songs import SongsDBAdapter

from models import *


class SqliteAllDBAdapter(ArtistsDBAdapter, SongsDBAdapter):
    def __init__(self, filename):
        self.filename = filename
        self.connection = None
        super().__init__()

    def prepare(self):
        self.connection = sqlite3.connect(self.filename)
        self._create_tables()

    def _create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS artists(id INTEGER PRIMARY KEY AUTOINCREMENT, name  TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS songs(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, id_artist INTEGER, FOREIGN KEY(id_artist) REFERENCES artists(_id))")

    def get_all_songs(self):
        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT Songs.id, Songs.title, artists.name FROM Songs "
                              "INNER JOIN artists ON Songs.id_artist = artists.id")
        songs = []
        for row in rows:
            song = ListOfSongs(row[1], row[2])
            song.id = int(row[0])
            songs.append(song)
        return songs

    def save_new_song(self, song: ListOfSongs):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Songs(title, id_artist) values(?, ?)", (song.songstitle, song.artistsname))
        self.connection.commit()

    def search_song(self, name):
        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT Songs.id, Songs.title, artists.name FROM Songs "
                             "INNER JOIN artists ON Songs.id_artist = artists.id "
                             )
        songs = []
        if rows is not None:
            for row in rows:
                song = ListOfSongs(row[1], row[2])
                song.id = row[0]
                if name in song.songstitle:
                    songs.append(song)
            return songs
        return None

    def delete_song(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Songs WHERE id=?", [id])
        self.connection.commit()

    def get_all_artists(self):
        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT * FROM Artists")
        artists = []
        for row in rows:
            artist = ListOfArtists(row[1])
            artist.id = int(row[0])
            artists.append(artist)
        return artists

    def save_new_artist(self, artist: ListOfArtists):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Artists(name) values(?)", [artist.artistsname])
        self.connection.commit()

    def search_artist(self, name):
        cursor = self.connection.cursor()
        rows = cursor.execute("SELECT Songs.id, Songs.title, artists.name FROM Songs "
                              "INNER JOIN artists ON Songs.id_artist = artists.id "
                              "WHERE Artists.name=?", [name])
        songs = []
        if rows is not None:
            for row in rows:
                song = ListOfSongs(row[1], row[2])
                song.id = row[0]
                songs.append(song)
            return songs
        return None

    def delete_artist(self, id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Artists WHERE id=?", [id])
        self.connection.commit()

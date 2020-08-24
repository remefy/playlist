class ListOfSongs:
    def __init__(self, songstitle, artistsname):
        self.id = None
        self.songstitle = songstitle
        self.artistsname = artistsname

    def __repr__(self):
        return f"{self.id}. {self.songstitle} {self.artistsname}"


class ListOfArtists:
    def __init__(self, artistsname):
        self.id = None
        self.artistsname = artistsname

    def __repr__(self):
        return f"{self.id}. {self.artistsname}"

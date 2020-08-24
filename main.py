from songs_app import SongsApp
from db.sqlite_adapter import SqliteAllDBAdapter

if __name__ == "__main__":
    adapter = SqliteAllDBAdapter("Myplaylist.db")
    app = SongsApp(adapter)
    app.start()

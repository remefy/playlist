from db.sqlite_adapter import SqliteAllDBAdapter
from models import *


class SongsApp:
    def __init__(self, adapter: SqliteAllDBAdapter):
        self.adapter = adapter

    def start(self):
        self.adapter.prepare()
        self._mainloop()

    def _mainloop(self):
        while True:
            command = input("\n Введите команду или напишите help: \n>>")
            if command == "help":
                print("exit - Выйти из программы")
                print("show all songs - Показать все песни")
                print("show all artists - Показать всех исполнителей")
                print("add song - добавить песню")
                print("add artist - добавить исполнителя")
                print("delete song - Удалить песню")
                print("delete artist - Удалить исполнителя")
                print("search song - Поиск песни по названию")
                print("search artist - Поиск исполнителя по имени")
            elif command == "exit":
                print("Bye!")
                break
            elif command == "add song":
                nameofsong = input("Введите название песни: ")
                id_fartist = int(input("Введите id исполнителя: "))
                song = ListOfSongs(nameofsong, id_fartist)
                self.adapter.save_new_song(song)
                print("Песня успешно добавлена!")
            elif command == "show all songs":
                songs = self.adapter.get_all_songs()
                for song in songs:
                    print(song)
            elif command == "delete song":
                bol = False
                id = int(input("Введите id песни: "))
                songs = self.adapter.get_all_songs()
                for song in songs:
                    if song.id == id:
                        bol = True
                if bol == True:
                    self.adapter.delete_song(id)
                    print("Песня успешно удалена!")
                else:
                    print("Такой песни нет в списке!")
            elif command == "search song":
                name = input("Введите название песни: ")
                songs = self.adapter.search_song(name)
                if songs is not None:
                    for song in songs:
                        print(song)
                else:
                    print("Такой песни нет!")
            elif command == "add artist":
                nameofartist = input("Введите имя исплнителя: ")
                artist = ListOfArtists(nameofartist)
                self.adapter.save_new_artist(artist)
                print("Исполнитель успешно добавлена!")
            elif command == "show all artists":
                artists = self.adapter.get_all_artists()
                for artist in artists:
                    print(artist)
            elif command == "delete artist":
                bol = False
                id = int(input("Введите id песни: "))
                artists = self.adapter.get_all_artists()
                for artist in artists:
                    if artist.id == id:
                        bol = True
                if bol == True:
                    self.adapter.delete_artist(id)
                    print("Исполнитель успешно удален!")
                else:
                    print("Такого исполнителя нет в списке!")
            elif command == "search artist":
                name = input("Введите имя исполнителя: ")
                artist = self.adapter.search_artist(name)
                if artist is not None:
                    for a in artist:
                        print(a)
                else:
                    print("Такого исполнителя нет!")
            else:
                print(f"Команда {command} не найдена")

import time
import json
from tabulate import tabulate


class Song:

    @staticmethod
    def _length_to_sec(split_time):
        if len(split_time) == 2:
            return int(split_time[0]*60 + split_time[1])
        elif len(split_time) == 3:
            return int(split_time[0]*3600 + split_time[1]*60 + split_time[2])

    @staticmethod
    def _length_to_min(split_time):
        if len(split_time) == 2:
            return int(split_time[0] + split_time[1]/60)
        elif len(split_time) == 3:
            return int(split_time[0]*60 + split_time[1] + split_time[2]/60)

    @staticmethod
    def _length_to_hour(split_time):
        if len(split_time) == 2:
            return int(split_time[0]/60 + split_time[1]/3600)
        elif len(split_time) == 3:
            return int(split_time[0] + split_time[1]/60 + split_time[2]/3600)

    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def __str__(self):
        return "{} - {} from {} - {}".\
                 format(self.get_artist(), self.get_title(), self.get_album(), self.length())

    def __eq__(self, other):
        if self.__hash__() == other:
            return True

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return "Song('{}', '{}', '{}', '{}'')".\
           format(self.__title, self.__artist, self.__album, self.__length)

    def length(self, seconds=False, minutes=False, hours=False):
        split_time = [int(x) for x in self.__length.split(":")]
        if seconds:
            return self._length_to_sec(split_time)
        elif minutes:
            return self._length_to_min(split_time)
        elif hours:
            return self._length_to_hour(split_time)
        else:
            return str(self.__length)

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_album(self):
        return self.__album


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.__name = name
        self.__repeat = repeat
        self.__shuffle = shuffle
        self.__Playlist = []
        self.__song_index = 0

    def __repr__(self):
        pass

    def add_song(self, song):
        self.__Playlist.append(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def remove_song(self, song):
        self.__Playlist.remove(song)

    def total_length(self):
        total_len_of_songs = 0
        for song in self.get_songs():
            total_len_of_songs += song.length(seconds=True)

        return time.strftime("%H:%M:%S", time.gmtime(total_len_of_songs))

    def artists(self):
        histogram_of_artists = {}
        count = 0

        for song in self.get_songs():
            current_artist = song.get_artist()
            if current_artist in histogram_of_artists.keys():
                count += 1
                histogram_of_artists[current_artist] += count
            else:
                histogram_of_artists[current_artist] = count

        return histogram_of_artists

    def next_song(self):
        if self.__song_index >= len(self.__Playlist) and self.__repeat:
            self.__song_index = 0

        song = self.__Playlist[self.__song_index]
        self.__song_index += 1

        return song

    def pprint_playlist(self):
        table = []
        for song in self.get_songs():
            table.append([song.get_artist(), song.get_title(), song.length()])
        print(tabulate(table, headers=["Artist", "Song", "Lenght"], tablefmt="grid"))

    def get_songs(self):
        return self.__Playlist

    def get_dict(self):
        dict_of_songs = []
        for song in self.get_songs():
            dict_of_songs.append(song.__dict__)
        result = {
                "name": self.__name,
                "repeat": self.__repeat,
                "shuffle": self.__shuffle,
                "song_index": self.__song_index,
                "songs": dict_of_songs,
        }
        return result

    def save(self, filename):
        with open(filename, 'w') as data:
            json.dump(self.get_dict(), data, indent=4)

    def load_from_dict(self, data_d):
        playlist = Playlist("Name")
        songss = data_d.pop('songs')
        playlist.__dict__ = data_d
        playlist._songs = []
        for song in songss:
            newsong = Song(song["_Song__title"], song["_Song__artist"], song["_Song__album"], song["_Song__length"])
            newsong.__dict__ = song
            playlist.add_song(newsong)
        return playlist

    def load(self, filename):
        with open(filename, 'r') as f:
            data_d = json.load(f)
        return self.load_from_dict(data_d)


def main():
    song1 = Song("Runaway", "Bon Jovi", "Greatest Hilts", "03:51")
    song2 = Song("In and out of love", "Bon Jovi", "Greatest Hilts", "04:26")
    song3 = Song("Lost Highway", "Bon Jovi", "Greatest Hilts", "1:04:13")
    test = []
    test.append(song1)
    test.append(song2)
    play = Playlist("test", repeat=True)
    play.add_songs(test)
    play.add_song(song3)
    play.pprint_playlist()
    play.save("testFile.json")
    play.load('testFile.json')

if __name__ == '__main__':
    main()

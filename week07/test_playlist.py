import unittest
from song import Song, Playlist


class TestPlayList(unittest.TestCase):

    def setUp(self):
        self.song = Song("RAndom", "mr.Random", "the best of Random", "1:30")
        self.song1 = Song("Runaway", "Bon Jovi", "Greatest", "03:51")
        self.song2 = Song("In and out", "Bon Jovi", "Greatest", "04:26")
        self.test_list = []
        self.test_list.append(self.song1)
        self.test_list.append(self.song2)
        self.play_list = Playlist("rrrr")

    def test_add_song(self):
        self.play_list.add_song(self.song)
        self.assertIn(self.song, self.play_list.get_songs())

    def test_add_songs(self):
        self.play_list.add_songs(self.test_list)

        self.assertIn(self.song1, self.play_list.get_songs())
        self.assertIn(self.song2, self.play_list.get_songs())

    def test_remove_song(self):
        self.play_list.add_songs(self.test_list)

        self.play_list.remove_song(self.song2)
        self.assertIsNot(self.song2, self.play_list.get_songs())

    def test_total_length(self):
        self.play_list.add_songs(self.test_list)
        self.play_list.add_song(self.song)
        self.assertEquals(self.play_list.total_length(), "00:09:47")



if __name__ == "__main__":
    unittest.main()

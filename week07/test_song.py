import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        pass

    def test_length_to_sec(self):
        self.song = Song("RAndom", "mr.Random", "the best of Random", "1:30")
        self.assertEqual(self.song.length(seconds=True), 90)

    def test_length_to_min(self):
        self.song = Song("RAndom", "mr.Random", "the best of Random", "41:30")
        self.assertEqual(self.song.length(minutes=True), 41)

    def test_length_to_hour(self):
        self.song = Song("RAndom", "mr.Random", "the best of Random", "1:59:60")
        self.assertEqual(self.song.length(hours=True), 2)

    def test_length_string(self):
        self.song = Song("RAndom", "mr.Random", "the best of Random", "1:30")
        self.assertEquals(self.song.length(), "1:30")


if __name__ == "__main__":
    unittest.main()

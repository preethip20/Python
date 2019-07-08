class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["happy bday to u",
                   "my bday is today",
                   "no not by bday"])
happy_bday.sing_song()

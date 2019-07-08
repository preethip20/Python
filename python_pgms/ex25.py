class song(object):
    def _init_(self,lyrics):
        self.lyrics=lyrics
    def sing_song(self):
        for line in self.lyrics:
            print line
 happy_bday = song(["happy bday to u",
 "preethi's bday",
 "gabbi preethi's bday"])
 belated_bday=song(["happy bday to u",
                    "preethi's bday",
                    "gabbi preethi's bday"])
happy_bday.sing_song()
belated_bday.sing_song()

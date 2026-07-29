class Playlist:
    def __init__(self) -> None:
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)


p = Playlist()
p.add("song A")
p.add("song B")
p.add("song C")
print(len(p))

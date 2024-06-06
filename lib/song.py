class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count of songs
        self.add_song_to_count()

        # Add genre and artist to their respective lists and counts
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Test case
def test_saves_name_artist_genre():
    '''instantiates with a name, artist, and genre.'''
    out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
    assert out_of_touch.name == "Out of Touch"
    assert out_of_touch.artist == "Hall and Oates"
    assert out_of_touch.genre == "Pop"
    assert Song.count == 1
    assert "Pop" in Song.genres
    assert "Hall and Oates" in Song.artists
    assert Song.genre_count["Pop"] == 1
    assert Song.artist_count["Hall and Oates"] == 1

# Running the test case
test_saves_name_artist_genre()

# Example usage:
song1 = Song("Song 1", "Artist 1", "Genre 1")
song2 = Song("Song 2", "Artist 2", "Genre 2")
song3 = Song("Song 3", "Artist 1", "Genre 1")

print("Total number of songs:", Song.count)
print("Unique genres:", Song.genres)
print("Unique artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)

class Seasons:
    __slots__ = ('Summer','Winter','Spring','Autumn')

    def __init__(self):
        self.Summer = "It is hot!"
        self.Winter = "It is cold!"
        self.Spring = "The weather is excellent!"
        self.Autumn = "It's super fally!"


seasoned = Seasons()


print(Seasons.__slots__)
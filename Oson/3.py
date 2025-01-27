class Film:
    def __init__(self, nomi, davomiyligi, reyting):
        self.title = nomi
        self.duration = davomiyligi
        self.reayting = reyting

    def increase_duration(self):
        if self.duration > 150:
            self.reayting -= 0.5
        
        return self.reayting
        
film = Film("Avatarr", 250, 4.8)

print(film.increase_duration())
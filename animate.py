import pygame

class Animation:
    # remember about the namespace problem,
    # move all property initialization to constructor

    def __init__(self,files):
        self.index = 0
        self.files = files
        self.files_len = len(files)
        self.imgs = []
        self.img = None

        for f in files:
            self.imgs.append(pygame.image.load(f))
        
        self.img = self.imgs[self.index]

    def animate(self):
        self.index+=1
        if self.index == self.files_len:
            self.index = 0
            #self.imgs[0] = pygame.image.load(self.files[0])
        
        self.img = self.imgs[self.index]
    
    def reset(self):
        #self.index = 0
        pass


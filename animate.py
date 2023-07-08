# Class yang mengatur animasi
# constructor: meminta parameter list string dari file gambar yang akan di load sebagai animasi
# animate: mengganti gambar secara urutan, Mario.img akan berisi gambar yang berubah-ubah
# reset: mengembalikan index gambar yang ditampilan ke awal (0)

import pygame

class Animation:
    # lesson: remember about the namespace problem,
    # move all property initialization to constructor
    # https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide

    def __init__(self,files):
        self.index = 0
        self.files = files
        self.files_len = len(files)
        self.imgs = []
        self.img = None

        # load gambar
        for f in files:
            self.imgs.append(pygame.image.load(f))
        
        self.img = self.imgs[self.index]

    def animate(self):
        if self.index < self.files_len-1:
            self.index+=1
        else:
            self.index = 0
        self.img = self.imgs[self.index]
    
    def reset(self):
        self.index = 0
        pass


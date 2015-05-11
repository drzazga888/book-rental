import math

class Paginator:
    def __init__(self, site, length, perpage=10):
        self.site = int(site)
        self.length = int(length)
        self.perpage = int(perpage)
        self.pages_length = int(math.ceil(length/float(perpage)))
        if self.site == 1:
            self.before = False
        else:
            self.before = self.site-1
        if self.site == self.pages_length:
            self.next = False
        else:
            self.next = self.site+1
        if self.site+2 <= self.pages_length and self.site >= 3:
            self.pages = (self.site-2, self.site-1, self.site, self.site+1, self.site+2)
        elif self.site+4 <= self.pages_length:
            self.pages = (1,2,3,4,5)
        elif self.site >= 5:
            self.pages = (self.pages_length-4, self.pages_length-3, self.pages_length-2, self.pages_length-1, self.pages_length)
        else:
            self.pages = (1, 2, 3, 4, 5)
            self.pages = self.pages[:self.pages_length]
        self.start = (self.site-1)*self.perpage+1
        self.to = self.site*self.perpage
        if self.to > self.length:
            self.to = self.length
        print self.start
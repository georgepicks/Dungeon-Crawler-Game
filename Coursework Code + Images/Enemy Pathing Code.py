def draw(self, win):
self.moving()
        if self.walk_count  +1>=24:
            self.walk_count = 0
        if self.vel ==3:
                win.blit(self.e_right, (self.x, self.y))
                self.walk_count += 1
        else:
                win.blit(self.e_left, (self.x, self.y))
                self.walk_count += 1
    def moving(self):
        if self.vel == 3:
            if self.x < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        if self.vel !=3:
            if self.x > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

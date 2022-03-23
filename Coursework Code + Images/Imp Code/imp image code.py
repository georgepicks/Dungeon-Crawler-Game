imp_size = random.randint(70, 70)
imp_attack_size = random.randint(120,120)

imp_attack_1 = pygame.image.load("attack2_1.png")
imp_attack_2 = pygame.image.load("attack2_2.png")
imp_attack_3 = pygame.image.load("attack2_3.png")
imp_attack_4 = pygame.image.load("attack2_4.png")
imp_attack_1 = pygame.transform.scale(imp_attack_1, (imp_attack_size, imp_attack_size))
imp_attack_2 = pygame.transform.scale(imp_attack_2, (imp_attack_size, imp_attack_size))
imp_attack_3 = pygame.transform.scale(imp_attack_3, (imp_attack_size, imp_attack_size))
imp_attack_4 = pygame.transform.scale(imp_attack_4, (imp_attack_size, imp_attack_size))

imp_dead_1 = pygame.image.load("fall_back_2.png")
imp_dead_2 = pygame.image.load("fall_back_3.png")
imp_dead_3 = pygame.image.load("fall_back_4.png")
imp_dead_4 = pygame.image.load("fall_back_5.png")
imp_dead_1 = pygame.transform.scale(imp_dead_1, (imp_size, imp_size))
imp_dead_2 = pygame.transform.scale(imp_dead_2, (imp_size, imp_size))
imp_dead_3 = pygame.transform.scale(imp_dead_3, (imp_size, imp_size))
imp_dead_4 = pygame.transform.scale(imp_dead_4, (imp_size, imp_size))

imp1 = pygame.image.load("imp_1.png")
imp2 = pygame.image.load("imp_2.png")
imp3 = pygame.image.load("imp_3.png")
imp4 = pygame.image.load("imp_4.png")
imp5 = pygame.image.load("imp_5.png")
imp6 = pygame.image.load("imp_6.png")
imp1 = pygame.transform.scale(imp1, (imp_size, imp_size))
imp2 = pygame.transform.scale(imp2, (imp_size, imp_size))
imp3 = pygame.transform.scale(imp3, (imp_size, imp_size))
imp4 = pygame.transform.scale(imp4, (imp_size, imp_size))
imp5 = pygame.transform.scale(imp5, (imp_size, imp_size))
imp6 = pygame.transform.scale(imp6, (imp_size, imp_size))

imp_dead = [imp_dead_1, imp_dead_2, imp_dead_3, imp_dead_4]
imp_idle = [imp1, imp2, imp3, imp4,imp5, imp6]
imp_attack = [imp_attack_1, imp_attack_2, imp_attack_3, imp_attack_4]


def draw_imp(self, win):
    if self.idle_count + 1 >= 18:
        self.idle_count = 0
    if self.dead_count >= 10:
        self.dead_count = 10
    if player.x > self.x - 20 and player.x < self.x + 70 and player.y > self.y - 20 and player.y < self.y + 70 and self.health > 0:
        win.blit(imp_attack[self.idle_count // 6], (self.x, self.y))
        self.idle_count += 1
    if self.health > 0:
        win.blit(imp_idle[self.idle_count // 6], (self.x, self.y))
        self.idle_count += 1
    if self.health <= 0:
        win.blit(imp_dead[self.dead_count // 3], (self.x, self.y))
        self.dead_count += 1

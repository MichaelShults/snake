import sys, pygame
# returns touple
def add_pairs(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]
def scale_pair(p, factor1, factor2):
    return factor1 * p[0], factor2 * p[1]
class Snake:
    def __init__(self):
        self.part_list = [(0, 0), (0, 10), (0, 20)]
        self.dir = (0, 10)

    def move(self):
        if len(self.part_list) == 1:
            self.part_list.append(add_pairs(self.part_list[0], dir))
        else:
            last = self.part_list[-1]
            pre_last = self.part_list[-2]
            self.dir = add_pairs(last, scale_pair(pre_last, -1, -1))
            self.part_list.append(add_pairs(last, self.dir))
        self.part_list.pop(0)

class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 320, 240
        self.speed = [1, 1]
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.snake = Snake()
        self.surface = pygame.Surface([10, 10])
        self.surface.fill((20, 20, 20))
        self.surface.fill((244, 244, 244), self.surface.get_rect().inflate(-1, -1))

    def isColliding(self, new_head):
        if new_head[0] + 10 > self.width or new_head[0] < 0 or new_head[1] < 0 or new_head[1] + 10 > self.height:
            return True
        if new_head in self.snake.part_list():
            return True
        else:
            return False

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.black)
            self.snake.move()
            for part in self.snake.part_list:
                self.screen.blit(self.surface, part)
            pygame.display.flip()
            pygame.time.delay(200)


game = Game()
game.play()



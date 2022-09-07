import sys, pygame
class Snake:
    def __init__(self):
        self.part_list = [(0, 0), (0, 10), (0, 20)]
        self.length = 1
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

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.black)
            for part in self.snake.part_list:
                self.screen.blit(self.surface, part)
            pygame.display.flip()
            pygame.time.delay(20)


game = Game()
game.play()



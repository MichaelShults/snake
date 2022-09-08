import sys
import pygame
from enum import Enum
import copy
BLOCK_SIZE = 10

#in place
class NumPair:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def add(self, other):
        self.c1 = self.c1 + other.c1
        self.c2 = self.c2 + other.c2
        return self

    def neg(self):
        self.c1 = -self.c1
        self.c1 = -self.c2
        return self

    def neg_c1(self):
        self.c1 = -self.c1
        return self

    def neg_c2(self):
        self.c2 = -self.c2
        return self

    def return_copy(self):
        return copy.copy(self)

class Direction(Enum):
    LEFT = NumPair(0, -BLOCK_SIZE)
    RIGHT = NumPair(0, BLOCK_SIZE)
    UP = NumPair(-BLOCK_SIZE, 0)
    DOWN = NumPair(BLOCK_SIZE, 0)
class Snake:
    def __init__(self, snake_length):
        self.part_list = [NumPair(0, i * BLOCK_SIZE) for i in range(snake_length)]
        self.dir = Direction.DOWN

class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 320, 240
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(self.size)
        self.snake = Snake()
        self.surface = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        self.surface.fill((20, 20, 20))
        self.surface.fill((244, 244, 244), self.surface.get_rect().inflate(-1, -1))

    def isColliding(self, new_head):
        if new_head[0] + 10 > self.width or new_head[0] < 0 or new_head[1] < 0 or new_head[1] + 10 > self.height:
            return True
        if new_head in self.snake.part_list():
            return True
        else:
            return False

    def MoveSnake(self):
        tail = self.snake.part_list.pop(0)
        if len(self.snake.part_list) == 0:
            tail.add(self.snake.dir)
            if self.isColliding(tail):
                print("Game Over!")
                sys.exit()
            else:
                self.snake.part_list.append(tail)
                return
        second_block = tail
        if len(self.snake.part_list) > 1:
            second_block = self.snake.part_list[-2]
        old_head = self.snake.part_list[-1]
        new_head = old_head.return_copy().add(self.snake.dir.value)
        if self.isColliding(new_head):
            print("Game Over!")
            sys.exit()
        if old_head.c1 > second_block.c1:
            self.snake.dir = Direction.RIGHT
        elif old_head.c1 < second_block.c1:
            self.snake.dir = Direction.LEFT
        elif old_head.c2 > second_block.c2:
            self.snake.dir = Direction.DOWN
        elif old_head.c2 < second_block.c2:
            self.snake.dir = Direction.UP
        self.snake.part_list.append(new_head)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.black)
            self.MoveSnake()
            self.blit()
            pygame.display.flip()
            pygame.time.delay(200)
    def blit(self):
        for part in self.snake.part_list:
            self.screen.blit(self.surface, part)


game = Game()
game.play()



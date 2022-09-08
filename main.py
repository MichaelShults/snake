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

    def tuple(self):
        return self.c1, self.c2

class Direction(Enum):
    LEFT = NumPair(-BLOCK_SIZE, 0)
    RIGHT = NumPair(BLOCK_SIZE, 0)
    UP = NumPair(0, -BLOCK_SIZE)
    DOWN = NumPair(0, BLOCK_SIZE)
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
        self.snake = Snake(3)
        self.surface = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        self.surface.fill((20, 20, 20))
        self.surface.fill((244, 244, 244), self.surface.get_rect().inflate(-1, -1))

    def isColliding(self, new_head):
        if new_head.c1 + 10 > self.width or new_head.c1 < 0 or new_head.c2 < 0 or new_head.c2 + 10 > self.height:
            return True
        if new_head in self.snake.part_list:
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
        self.update_dir(old_head, second_block)
        if self.isColliding(new_head):
            print("Game Over!")
            sys.exit()
        self.snake.part_list.append(new_head)

    def update_dir(self, head, second_to_last):
        if head.c1 > second_to_last.c1:
            self.snake.dir = Direction.RIGHT
        elif head.c1 < second_to_last.c1:
            self.snake.dir = Direction.LEFT
        elif head.c2 > second_to_last.c2:
            self.snake.dir = Direction.DOWN
        elif head.c2 < second_to_last.c2:
            self.snake.dir = Direction.UP

    def blit(self):
        for part in self.snake.part_list:
            self.screen.blit(self.surface, part.tuple())

    def turnSnake(self, keys):
        new_head = self.snake.part_list[-1].return_copy()
        if keys[pygame.K_RIGHT]:
            if self.snake.dir == Direction.UP:
                new_head.add(NumPair(BLOCK_SIZE, BLOCK_SIZE))
            elif self.snake.dir == Direction.DOWN:
                new_head.add(NumPair(BLOCK_SIZE, -BLOCK_SIZE))
            self.snake.dir = Direction.RIGHT
        elif keys[pygame.K_LEFT]:
            if self.snake.dir == Direction.UP:
                new_head.add(NumPair(-BLOCK_SIZE, BLOCK_SIZE))
            elif self.snake.dir == Direction.DOWN:
                new_head.add(NumPair(-BLOCK_SIZE, -BLOCK_SIZE))
            self.snake.dir = Direction.LEFT
        elif keys[pygame.K_UP]:
            if self.snake.dir == Direction.RIGHT:
                new_head.add(NumPair(-BLOCK_SIZE, -BLOCK_SIZE))
            elif self.snake.dir == Direction.LEFT:
                new_head.add(NumPair(-BLOCK_SIZE, BLOCK_SIZE))
            self.snake.dir = Direction.UP
        elif keys[pygame.K_DOWN]:
            if self.snake.dir == Direction.RIGHT:
                new_head.add(NumPair(-BLOCK_SIZE, BLOCK_SIZE))
            elif self.snake.dir == Direction.LEFT:
                new_head.add(NumPair(BLOCK_SIZE, BLOCK_SIZE))
            self.snake.dir = Direction.DOWN
        if self.isColliding(new_head):
            print("Game Over!")
            sys.exit()
        else:
            self.snake.part_list.pop(-1)
            self.snake.part_list.append(new_head)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.black)
            self.turnSnake(pygame.key.get_pressed())
            self.MoveSnake()
            self.blit()
            pygame.display.flip()
            pygame.time.delay(200)





game = Game()
game.play()



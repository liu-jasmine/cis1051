import pygame
import sys
import random

head_color = (242, 70, 181)
body_color = (242, 148, 181)
food_color = (233, 185, 87)
screen_size = (500,500)


def game_start(): 

    # shows loading screen                                                                                     
    display_surface = pygame.display.set_mode(screen_size)                                      
    image = pygame.image.load(r'C:\Users\12677\Desktop\WormGame\wormTitle.jpg') 
    display_surface.blit(image, (0, 0)) 

    # countdown for 3 seconds
    for i in range(3):                                                                             
        pygame.display.set_caption("Worm Game  |  Game starts in " + str(3-i) + " second(s) ...")
        pygame.display.update()
        pygame.time.wait(1000)

    # shows background screen
    image = pygame.image.load(r'C:\Users\12677\Desktop\WormGame\wormBackground.jpg')              
    display_surface.blit(image, (0, 0)) 
    pygame.display.update()

class Snake():
    def __init__(self):
        self.position = [100, 60]
        self.body = [[100, 60], [80, 60], [60, 60]]
        self.direction = "RIGHT"
        self.change_direction_to = self.direction

    # can not move backwards
    def which_direction(self, dir):                                                            
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    # movement of x and y cord
    def move(self, foodPos):                                                               
        if self.direction == "RIGHT":
            self.position[0] += 20
        if self.direction == "LEFT":
            self.position[0] -= 20
        if self.direction == "UP":
            self.position[1] -= 20
        if self.direction == "DOWN":
            self.position[1] += 20
        self.body.insert(0, list(self.position))                                         
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()                                                                 
            return 0                

    # check if x and y are in certain range, and if head is in body
    def collision_with_boundaries(self):                                                   
        if self.position[0] > 480 or self.position[0] < 20:
            return 1
        elif self.position[1] > 480 or self.position[1] < 20:
            return 1
        for bodyPart in self.body[1:]:                                          
            if self.position == bodyPart:
                return 1
        return 0
    
    def get_head_position(self):
        return self.position

    def get_body_position(self):
        return self.body

class FoodSpawer():
    def __init__(self):
        self.position = [random.randrange(1, 24) * 20, random.randrange(1, 24) * 20]            
        self.isFoodOnScreen = True

    # makes food be in the bounds
    def spawn_food(self):
        if self.isFoodOnScreen == False:                                                        
            self.position = [random.randrange(1, 24) * 20, random.randrange(1, 24) * 20]
            self.isFoodOnScreen = True
        return self.position

    def food_boolean(self, b):
        self.isFoodOnScreen = b


def gameOver(score):  
    pygame.display.set_caption("Game Over! | Score: " + str(score) +" | ENTER to play again or ESC to quit ...")
    pygame.display.update()

    # key options
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                elif event.key == pygame.K_RETURN:
                    return

def main():
    game_start()
    window = pygame.display.set_mode(screen_size)
    fps = pygame.time.Clock()

    while True:

        # set up new game
        score = 0
        snake = Snake()
        foodSpawner = FoodSpawer()
        game_over = False

        # game loop
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake.which_direction('RIGHT')
                    if event.key == pygame.K_UP:
                        snake.which_direction('UP')
                    if event.key == pygame.K_DOWN:
                        snake.which_direction('DOWN')
                    if event.key == pygame.K_LEFT:
                        snake.which_direction('LEFT')
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            # spawn new food
            foodPos = foodSpawner.spawn_food()
            
            # true if food is eaten
            if snake.move(foodPos) == 1:
                score += 1
                foodSpawner.food_boolean(False)

            # check for collision
            if snake.collision_with_boundaries() == 1:
                game_over = True

            # draw background, snake and food
            image = pygame.image.load(r'C:\Users\12677\Desktop\WormGame\wormBackground.jpg')                
            window.blit(image, (0, 0)) 
            for pos in snake.get_body_position():
                pygame.draw.rect(window, body_color, pygame.Rect(pos[0], pos[1], 20, 20))
            pygame.draw.rect(window, food_color, pygame.Rect(foodPos[0], foodPos[1], 20, 20))

            pygame.display.set_caption("Worm Game | Score : " + str(score))
            pygame.display.flip()                                                                                       
            fps.tick(10)                                                                                               
        
        # wait for input
        gameOver(score)
main()


# Code References
# Codebasics (November 7, 2020) python_projects/1_snake_game/7_final_code_background_music_image [Code source]. https://github.com/codebasics/python_projects/blob/main/1_snake_game/7_final_code_background_music_image.py
# Kumar, Saurabh (November 7, 2017) Snake Game in Python | Pygame [ Video tutorial ]. https://www.youtube.com/watch?v=V_f07t570pA&ab_channel=SaurabhKumar





# import pygame module in this program
import pygame
import random
import os

#To add Music
pygame.mixer.init()
pygame.init()

# define the RGB value for white, red, black colour .
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Creating Window
screen_width = 600
screen_height = 400
# create the display surface object
# of specific dimension..e(X, Y).
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background Image
bgimg = pygame.image.load("snake.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()  #convert_alpha()- Creates a new copy of the surface with the desired pixel format

# Game Title
pygame.display.set_caption("Snake_by_Sandesh")   #pygame.display.set_caption. — Set the current window caption(name or title)
pygame.display.update()                          #update() to make the display Surface actually appear on the user's monitor.

clock = pygame.time.Clock()               #pygame.time.Clock- This function is used to create a clock object which can be used to keep track of time.
font = pygame.font.SysFont(None, 55)      # You can load fonts from the system by using the pygame.font.SysFont() function

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)       # create a text surface object,on which text is drawn on it.
    gameWindow.blit(screen_text, [x,y])                # copying the text surface object to the display surface object at the center coordinate.

             # pygame.draw.rect(): This function is used to draw a rectangle.
             # It takes the surface, color, and pygame Rect object as an input parameter and draws a rectangle on the surface.
             # [x,y]a are the coordinates at which rectangle will be formed of dimension (snake_size, snake_size)
             # Here we are taking 4 arguments which are required to make a rectangle, iterating snk_list and simply just putting those values in “rect()”.
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False     #Here we are running the exit_game= false loop which means this code will run until exit_game variable become true
    while not exit_game:
        gameWindow.fill((233,221,20))       #completely fill the surface object with some color (I have taken randomly- RGB)
        text_screen("Welcome to Snakes", black, 120, 140)          #Calling text_screen function
        text_screen("Press Space Bar to Play", black, 80, 200)     #Calling text_screen function

        #So for getting all the possible events of pygame we will run the for loop where for any event
        # i.e. mouse-clicking, moving, key pressing etc. will be detected by the program.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    #pygame.QUIT: This is used to terminate the event when we click on the close button at the corner of the window.
                exit_game = True             #In this we first used an “if” statement to check if event’s type is “QUIT” and
                                             # if it’s “QUIT” then exit_game is true. “exit_game” is running the while loop,
                                             # if it’s True then “not” keyword will make it False and the while loop will end automatically!

            if event.type == pygame.KEYDOWN:               #In this we first used “if” statement to check if the user has pressed ANY key.
                if event.key == pygame.K_SPACE:             #If any key is pressed then we are checking if that key is SPACE key
                    pygame.mixer.music.load('backgrd.mp3')   #and if it’s SPACE key then we are saying print this statement,
                    pygame.mixer.music.play()                # or execute the given task (Here, task is to load music after pressing SPACE bar)
                    gameloop()

        pygame.display.update()
        clock.tick(60)

#Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45        #snake_x & snake_y are x and y co-ordinates of our snake’s head in gameWindow
    snake_y = 55
                         # Speed means it is covering distance. In our game distance is in co-ordinates(x and y) which are snake_x and snake_y.
                          # So it just means that we have to keep increasing values of co-ordinates like it’s in a loop.
                          # We already are in a “while” loop so we just have to increment values, but we also have to see how much and in which axis
                           # to increment?
                          # For this we will make two variables: velocity_x & velocity_y
    velocity_x = 0
    velocity_y = 0
                           #Increasing snake length:
                           #We will make two variables “snk_list” and “snk_length”. “snk_list” will be a list of list.
                           # It will have co-ordinates of the snake’s rectangles. “snk_length” will have an integer and
                           # we will increment it’s value everytime our snake eats food. Code below:
    snk_list = []
    snk_length = 1

    # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 15      #“snake_size” is length and breadth of our snake’s head.
    fps = 40

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! ", red, 30, 130)
            text_screen("Press Enter To Continue", red, 30, 180)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                                                     # Here we changed from adding in “snake_x” and “snake_y” to adding in “velocity_x” and
                                                     # “velocity_y”, why? Because at the end we are just adding “snake_x” and “velocity_x”
                                                     # so we change “snake_x” or “velocity_x”, what does it matter? It matters because “snake_x” is co-ordinate,
                                                     # if we set that as say “10”, it will place snake on 10th co-ordinate
                                                     # but that is not the case with “velocity_x”!

               # Making it move straight:
               # Next issue is that it is moving straight and diagonally, we want only straight. There is a simple solution for that,
               # diagonal movement happens when there is more than one force applied. Here are two, “velocity_x” and “velocity_y”
               # so just null the other velocity when one is in play! Code for that:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score+=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
                                                    # We simply saw the difference between snake’s co-ordinates and food’s co-ordinates, if they are lower than 6
                                                    # then it means that they are kinda overlapping and it will add and replot food. In “if” block we will add score
                                                    # and replot food as both things should be done when overlapping happens! “abs” function returns absolute value
                                                    # which in simple term means it will return positive value.
                           #Adding score:
                           # We have already checked if it’s overlapping so we just have to make a variable
                           # and increment it’s value whenever it enters “if” block. Code:
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                                                                          #Getting random number:
                                                                #To get a random number we will use random module’s “randint” function.
                                                                # “rand” stands for random and “int” means integer. It takes a range(start and end) as argument and
                                                                # returns a random number between that range! For example:

                                                                 #random.randint(0,5)
                                                                 #Returns: 2 (random number)
                                        #In our game we want to place food in game window so it should choose random number between 0 and game width and height.
                                        # We made 2 variables for game width and game height, “screen_width” and “screen_height”, so code would be:
                food_x = random.randint(20, screen_width /2)
                food_y = random.randint(20, screen_height /2)      # (food_x, food_y)- these are co-ordinates of our food!
                snk_length += 5        #Incrementing value of snk_length
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + " Hiscore: "+str(hiscore), red, 5, 5)
                                                                                       # For food we are just making a red rectangle like we made black rectangle(snake’s head).
                                                                                       # We already defined red color in blog 9. To make rectangle write below:
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

                                   #Appending in snk_list:
                                   #Now we will make a function called “plot_snake”! We will give it a list of co-ordinates(snk_list) and
                                   # it will simply plot a rectangle on all those co-ordinates which will become our snake.
                                   # With every loop we will keep appending co-ordinates in “snk_list” and all those co-ordinates will be plotted by “plot_snake” function!
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)    #Here we are just appending snake_x and snake_y  in head and then appending head in snk_list. Hence, snk_list is a list of lists!

                       # As you can see from score, snake didn’t become big because of playing and eating food.
                       # It is not deleting old rectangles. To delete old rectangles we just have to keep deleting 0th item of “snk_list”
                       # whenever length of snk_list becomes greater than snk_length! Code below:
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()
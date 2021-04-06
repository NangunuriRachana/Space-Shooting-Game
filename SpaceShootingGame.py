#Space Shooting Game

''' The Pygame is a package that helps to build 2D video games using python '''

#pip install pygame

''' There are a few major parts of the Pygame:
1. Display image(blit,sprite)
2. Animation
3. Physics Engine(collision)
4. Camera
5. Sound,music
6. Game loop '''

''' To keep the element moving and to make things coming one after another,
you will need to run a loop. That loop is called the game loop. The game
loop is a never-ending loop. That keeps the game running forever until the
player wins or fails or forcefully quit the game. The loop looks like this:
keep_alive=True
while keep_alive: '''

import pygame

# set the game window (game screen)
''' A pixel is a very tiny square box on a screen. This is the smallest unit of the screen that has it's one color and you can set a specific color on it. '''
screen_size = [360, 600]  # width,height
''' The screen is part of the Pygame display. To create the screen you will need to call the set_mode (method) on the display (class) of Pygame (module). While calling the set_mode you need to pass the screen_size. '''
''' The set mode means you are setting the mode of the display. For some games, the display could be full screen or resizable. In our case, we are going with 360px width and 600px height. '''
''' Game screen will be changing frequently. For that purpose, you will need to put the screen on a variable. So that you can use it in the future. Hence your display screen will be like '''
screen = pygame.display.set_mode(screen_size)
# create a screen to display a game

#displaying image is in the heart of any game engine
''' To display image, you have to do 2 things-
1. Load image 2. Tell Pygame where to display the image '''
''' If you have image in the same folder where you have the python code, to load the image all you have to do is call image.load on pygame and pass the name of the image. If you want to load bg.png, you will write code like pygame.image.load('bg.png') '''
''' At the time of loading the image, set the image to a variable. This will help you to tell pygame to display the image '''
background = pygame.image.load('background.png')
planets=['one.png','two.png','three.png']
p_index=0
planet = pygame.image.load(planets[p_index])
bullet = pygame.image.load('bullet.png')
spaceship = pygame.image.load('spaceship.png')
''' Do 2 things to load image- 1. use pygame.image.load to load planet image 2. while loading set the loaded image to a variable. '''
''' Displaying an image on screen means transferring the image pixels as a block on the current screen. Transferring an image as a block is called Blit. Here, BL came from block. I came from image and T came from Transfer. Blit means Block Image Transfer. Use blit to display an image. While calling the blit method on the screen, you have to pass 2 things-
1. Name of the image variable(image loaded)
2. Top left corner position of image '''
planet_x=140
move_direction='right'
fired=False
bullet_y=500
keep_alive = True

''' To set frame rate in pygame you have to do 2 things- 1. create a clock 2. set the tick(tick could be considered as frames) '''
''' To create a clock, just call the Clock method on the pygame.time and create a variable named clock '''
clock=pygame.time.Clock()
while keep_alive:
    ''' To access keyboard events you have to call event.get on pygame. Then call get_pressed function on pygame.keys. This will return a list of all the keys. The value of every key will be False. Only the button user pressed will be True. '''
    pygame.event.get()
    keys = pygame.key.get_pressed()  #gives all pressed buttons
    if keys[pygame.K_SPACE] == True:
        fired=True 
        #print('Space key pressed')
    #remember y position is higher at the bottom
    ''' To make the planet moving, you will need to do 3 things- 1. declare planet_x and move_direction variable 2. add move_direction change logic inside game loop 3. at the time of blit of planet image, use planet_x '''
    #a change in position in each iteration creates animation
    if move_direction=='right':
      planet_x+=5
      if planet_x==300:
        move_direction='left'
    else:
      planet_x-=5
      if planet_x==0:
        move_direction='right'

    if fired is True:
      bullet_y-=5
      if bullet_y==50:
        fired=False
        bullet_y=500

    # Our first element to add would be the background image
    screen.blit(background, [0, 0])
    ''' Do 2 things to display image- 1. inside the game loop, blit the image 2. while blit set the left-top corner of image. '''
    ''' You have to do 4 things to display something on screen- 1. create a loop variable 2. create the never-ending while loop (game loop) 3. set the image on screen 4. tell pygame to update the display '''
    
    screen.blit(planet, [planet_x, 50])
    screen.blit(bullet, [180, bullet_y])
    screen.blit(spaceship, [160, 500])

    if bullet_y<80 and planet_x>120 and planet_x<180:
      #print('BOOM')
      p_index+=1
      if p_index<len(planets):
        planet=pygame.image.load(planets[p_index])
        planet_x=10
      else:
        #print('YOU WIN')
        keep_alive=False

    ''' As you may change elements or element position, you will need to tell pygame to update the display. '''
    pygame.display.update()
    clock.tick(60)#to set the frame rate
    ''' This will tell the pygame to run frames and the rate will be at most 60 frames per seconds (fps) '''

#These are the package
import pygame
import random

#Screen
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

#images used
background = pygame.image.load('green-grass-texture-background-seamless-pattern-spring-lawn-new-170941039.jpg')
omkar = pygame.image.load('Picture1.png')
car = pygame.image.load('Picture2.png')


#Score Counter
def display_score(score):
 font = pygame.font.SysFont('Comic Sans MS', 30)
 score_text = 'Score: ' + str(score)
 text_img = font.render(score_text, True, (0, 255, 0))
 screen.blit(text_img, [20, 10])

#Positioning
def random_offset():
    return -1*random.randint(100, 1500)


Car_y = [random_offset(), random_offset(), random_offset()]
user_x = 150
score = 0

#Car Crash Score
def crashed(idx):
    global score
    global keep_alive
    score = score + 10
    Car_y[idx] = random_offset()
    if score < -500:
        keep_alive = False


def update_Car_pos(idx):
    global score
    if Car_y[idx] > 600:
        Car_y[idx] = random_offset()
        score = score - 5
        print('score', score)
    else:
        Car_y[idx] = Car_y[idx] + 5

keep_alive = True

clock = pygame.time.Clock()
while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 280:
        user_x = user_x + 10
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x = user_x - 10

    update_Car_pos(0)
    update_Car_pos(1)
    update_Car_pos(2)

    screen.blit(background, [0, 0])
    screen.blit(omkar, [user_x, 520])
    screen.blit(car, [0, Car_y[0]])
    screen.blit(car, [250, Car_y[1]])
    screen.blit(car, [380, Car_y[2]])

    if Car_y[0] > 500 and user_x < 70:
        crashed(0)

    if Car_y[1] > 500 and user_x > 80 and user_x < 200:
        crashed(1)

    if Car_y[2] > 500 and user_x > 220:
        crashed(2)

    display_score(score)

    pygame.display.update()
    clock.tick(100)

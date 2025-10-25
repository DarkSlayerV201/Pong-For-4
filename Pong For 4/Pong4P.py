
import pygame
from sys import exit
from random import randint


### Pygame initiate ###

pygame.init()


### Screen variales ###

screen_height = 1000
screen_width = 1000
screen = pygame.display.set_mode((screen_height, screen_width))
screen_rect = screen.get_rect()
pygame.display.set_caption("Pong for 4")
#background = pygame.draw.rect(screen, "Black", screen_rect)
instructions_font = pygame.font.Font("Pong For 4/Font/ci-gamedev.ttf", 20)
start_font = pygame.font.Font("Pong For 4/Font/ci-gamedev.ttf", 50)


### Functions ###

def display_score():
        current_time = int((pygame.time.get_ticks() - start_time) / 1000)
        score_surf = start_font.render(f"Score: {current_time}", False, "Grey")
        score_rect = score_surf.get_rect(center = (screen_rect.centerx, screen_rect.centery))
        screen.blit(score_surf, score_rect) #Score_variable
        return current_time

def wins(win_count, round_result):
        rounds_won = win_count + round_result
        return rounds_won

def get_random_int(minimum, maximum):
        getting_number = True
        while getting_number:
                number = randint(minimum, maximum)
                if number == 0: getting_number = True
                else: getting_number = False
        return number

def get_random_float(minimum_int, maximum_int, decimals):
        number = get_random_int(minimum_int, maximum_int)
        float_number = number / decimals
        return float_number

def reset_ball():
        ball.rect.center = screen_rect.center
        ball.initial_speed_x = get_random_int(-5, 5)
        ball.initial_speed_y = get_random_int(-5, 5)
        ball.speed_x = ball.initial_speed_x
        ball.speed_y = ball.initial_speed_y
        ball.acceleration = get_random_float(2, 10, 1000)
        pass



#def player_plays_not(gamer):
#        print(f"{player} ha sido desactivado")
#        pass



### Ball class ###
class moving_object:

        def __init__(self, image, x, y):
                self.surf = pygame.transform.scale((pygame.image.load(image)), (50, 50))
                self.rect = self.surf.get_rect(center = (x, y))
                self.initial_speed_x = get_random_int(-5, 5)
                self.initial_speed_y = get_random_int(-5, 5)
                self.speed_x = self.initial_speed_x
                self.speed_y = self.initial_speed_y
                self.acceleration = get_random_float(2, 10, 1000)
                self.acceleration_x = 0
                self.acceleration_y = 0
                pass

ball = moving_object("Pong For 4/Ball/White ball.png", screen_rect.centerx, screen_rect.centery)


### Player class ###
class player:
        
        def __init__(self, image, x, y, shield, axis, controls, color_value, plays, wins, loses):
                
                self.surf = pygame.transform.scale((pygame.image.load(image).convert_alpha()), (80, 80))
                self.rect = self.surf.get_rect(center = (x, y))

                self.shield_surf = pygame.transform.scale((pygame.image.load(shield)), (20, 240))
                self.death_barrier_surf = pygame.transform.scale((pygame.image.load("Pong For 4/Barriers/Death.png")), (20, screen_rect.width))

                if axis == "left": 
                        self.shield_rect = self.shield_surf.get_rect(midleft = (self.rect.right, y))
                        self.death_barrier_rect = self.death_barrier_surf.get_rect(midleft = (self.rect.right, y))

                elif axis == "right": 
                        self.shield_rect = self.shield_surf.get_rect(midright = (self.rect.left, y))
                        self.death_barrier_rect = self.death_barrier_surf.get_rect(midright = (self.rect.left, y))

                elif axis == "top": 
                        self.shield_surf = pygame.transform.rotate(self.shield_surf, 90)
                        self.death_barrier_surf = pygame.transform.rotate(self.death_barrier_surf, 90)
                        self.shield_rect = self.shield_surf.get_rect(midtop = (x, self.rect.bottom))
                        self.death_barrier_rect = self.death_barrier_surf.get_rect(midtop = (x, self.rect.bottom))

                elif axis == "bottom": 
                        self.shield_surf = pygame.transform.rotate(self.shield_surf, 90)
                        self.death_barrier_surf = pygame.transform.rotate(self.death_barrier_surf, 90)
                        self.shield_rect = self.shield_surf.get_rect(midbottom = (x, self.rect.top))
                        self.death_barrier_rect = self.death_barrier_surf.get_rect(midbottom = (x, self.rect.top))

                else: print("Error al asignar clase") #Error

                self.base_speed = 5
                self.speed = 5
                self.acceleration = 0
                self.plays = plays
                self.alive = self.plays
                self.win_count = wins
                self.lose_count = loses
                self.color = color_value

                self.instructions_surf = instructions_font.render(controls, False, color_value)
                self.instructions_rect = self.instructions_surf.get_rect(center = (x, y))


                pass


### Players
white = player("Pong For 4/Players/White.png", 50, screen_rect.centery, "Pong For 4/Barriers/White.png", "left", "W/S", "White", 1, 0, 0)
green = player("Pong For 4/Players/Green.png", (screen_rect.right - 50), screen_rect.centery, "Pong For 4/Barriers/Green.png", "right", "Num 8/Num 2", "Green", 1, 0, 0)
red = player("Pong For 4/Players/Red.png", screen_rect.centerx, 50, "Pong For 4/Barriers/Red.png", "top", "N/M", "Red", 1, 0, 0)
blue = player("Pong For 4/Players/Blue.png", screen_rect.centerx, (screen_rect.bottom - 50), "Pong For 4/Barriers/Blue.png", "bottom", "Left/Right", "Blue", 1, 0, 0)
player_list = [white, red, green, blue]



### Game variables ###
clock = pygame.time.Clock()
game_active = False
game_start = True
start_time = 0
score = 0

### Main loop ###
while True:

        ## Inputs
        for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                
                #key identifier
                #if event.type == pygame.KEYDOWN:
                        #key_name = pygame.key.name(event.key)
                        #print(key_name)
                        #print(pygame.key.key_code(key_name))

                if event.type == pygame.MOUSEBUTTONDOWN and game_start == True:
                        
                        if white.instructions_rect.collidepoint(event.pos):
                                white.plays = 0
                                white.alive = 0
                                print(white.plays)
                        if red.instructions_rect.collidepoint(event.pos):
                                red.plays = 0
                                red.alive = 0
                        if green.instructions_rect.collidepoint(event.pos): 
                                green.plays = 0
                                green.alive = 0
                        if blue.instructions_rect.collidepoint(event.pos): 
                                blue.plays = 0
                                blue.alive = 0
        
        ## Keyboard and background ##
        keys = pygame.key.get_pressed()
        background = pygame.draw.rect(screen, "Black", screen_rect)
        
        ## Start game
        if game_start and game_active == False:
                screen.blit(white.instructions_surf, white.instructions_rect)
                screen.blit(green.instructions_surf, green.instructions_rect)
                screen.blit(red.instructions_surf, red.instructions_rect)
                screen.blit(blue.instructions_surf, blue.instructions_rect)
                start_surf = start_font.render("Press Space to start", False, "Grey")
                start_rect = start_surf.get_rect(center = (screen_rect.centerx, screen_rect.centery))
                plays_surf = start_font.render("Press players to disable them", False, "Grey")
                plays_rect = plays_surf.get_rect(midtop = (start_rect.centerx, (start_rect.bottom + 20)))
                screen.blit(start_surf, start_rect)
                screen.blit(plays_surf, plays_rect)

                
                if keys[pygame.K_SPACE]: 
                        game_start = False
                        game_active = True
                        start_time = pygame.time.get_ticks()
        
        ## Main game
        if game_active:

                # Variables
                people_playing = white.plays + red.plays + green.plays + blue.plays
                people_alive = white.alive + red.alive + green.alive + blue.alive
                if people_playing == 1: score = display_score()

                # White inputs
                white.acceleration = 0

                if white.alive == 1:

                        if keys[pygame.K_s]: #white down
                                white.rect.y += white.speed
                                white.shield_rect.y += white.speed
                                white.acceleration = 2

                        if keys[pygame.K_w]: #white up
                                white.rect.y -= white.speed
                                white.shield_rect.y -= white.speed
                                white.acceleration = -2
        
                #print(white.alive)

                # Green inputs
                green.acceleration = 0

                if green.alive == 1:

                        if keys[pygame.K_KP2]: #green down
                                green.rect.y += green.speed
                                green.shield_rect.y += green.speed
                                green.acceleration = 2
        
                        if keys[pygame.K_KP8]: #green up
                                green.rect.y -= green.speed
                                green.shield_rect.y -= green.speed
                                green.acceleration = -2

                # Red inputs
                red.acceleration = 0

                if red.alive == 1:

                        if keys[pygame.K_m]:
                                red.rect.x += red.speed
                                red.shield_rect.x += red.speed
                                red.acceleration = 2

                        if keys[pygame.K_n]:
                                red.rect.x -= red.speed
                                red.shield_rect.x -= red.speed
                                red.acceleration = -2

                # Blue inputs
                blue.acceleration = 0

                if blue.alive == 1:

                        if keys[pygame.K_RIGHT]:
                                blue.rect.x += blue.speed
                                blue.shield_rect.x += blue.speed
                                blue.acceleration = 2

                        if keys[pygame.K_LEFT]:
                                blue.rect.x -= blue.speed
                                blue.shield_rect.x -= blue.speed
                                blue.acceleration = -2
                

                # Ball logic #

                # Ball-players collisions
                if green.alive == 1:
                        if ball.rect.colliderect(green.shield_rect): 
                                ball.speed_x = -ball.speed_x
                                ball.speed_y = ball.speed_y + green.acceleration
                                ball.rect.right = green.shield_rect.left

                else:
                        if ball.rect.colliderect(green.death_barrier_rect):
                                ball.speed_x = -ball.speed_x
                                ball.speed_y = ball.speed_y
                                ball.rect.right = green.death_barrier_rect.left

                if white.alive == 1:
                        if ball.rect.colliderect(white.shield_rect):
                                ball.speed_x = -ball.speed_x
                                ball.speed_y = ball.speed_y + white.acceleration
                                ball.rect.left = white.shield_rect.right

                else: 
                        if ball.rect.colliderect(white.death_barrier_rect):
                                ball.speed_x = -ball.speed_x
                                ball.speed_y = ball.speed_y
                                ball.rect.left = white.death_barrier_rect.right
        
                if red.alive == 1:
                        if ball.rect.colliderect(red.shield_rect): 
                                ball.speed_y = -ball.speed_y
                                ball.speed_x = ball.speed_x + red.acceleration
                                ball.rect.top = red.shield_rect.bottom

                else: 
                        if ball.rect.colliderect(red.death_barrier_rect):
                                ball.speed_y = -ball.speed_y
                                ball.speed_x = ball.speed_x 
                                ball.rect.top = red.death_barrier_rect.bottom
        
                if blue.alive == 1:
                        if ball.rect.colliderect(blue.shield_rect): 
                                ball.speed_y = -ball.speed_y
                                ball.speed_x = ball.speed_x + blue.acceleration
                                ball.rect.bottom = blue.shield_rect.top

                else:
                        if ball.rect.colliderect(blue.death_barrier_rect):
                                ball.speed_y = -ball.speed_y
                                ball.speed_x = ball.speed_x 
                                ball.rect.bottom = blue.death_barrier_rect.top

                # Ball acceleration and movement

                if ball.speed_x > 0: ball.speed_x += ball.acceleration
                elif ball.speed_x < 0: ball.speed_x -= ball.acceleration
                else: print("Error: ball.speed_x == 0")
                
                if ball.speed_y > 0: ball.speed_y += ball.acceleration
                elif ball.speed_y < 0: ball.speed_y -= ball.acceleration
                else: print("Error: ball.speed_y == 0")

                ball.rect.x += ball.speed_x 
                ball.rect.y += ball.speed_y


                # Ball-screen collisions
                if ball.rect.top <= screen_rect.top: 
                        reset_ball()
                        #ball.rect.center = screen_rect.center
                        #ball.initial_speed_x = get_random_int(-5, 5)
                        #ball.initial_speed_y = get_random_int(-5, 5)
                        #ball.speed_x = ball.initial_speed_x
                        #ball.speed_y = ball.initial_speed_y
                        red.alive = 0 #Red dies
                        people_alive -= 1

                if ball.rect.bottom >= screen_rect.bottom: 
                        reset_ball()
                        #ball.rect.center = screen_rect.center
                        #ball.initial_speed_x = get_random_int(-5, 5)
                        #ball.initial_speed_y = get_random_int(-5, 5)
                        #ball.speed_x = ball.initial_speed_x
                        #ball.speed_y = ball.initial_speed_y
                        blue.alive = 0 #Blue dies
                        people_alive -= 1

                if ball.rect.right >= screen_rect.right:
                        reset_ball()
                        #ball.rect.center = screen_rect.center
                        #ball.initial_speed_x = get_random_int(-5, 5)
                        #ball.initial_speed_y = get_random_int(-5, 5)
                        #ball.speed_x = ball.initial_speed_x
                        #ball.speed_y = ball.initial_speed_y
                        green.alive = 0 #Green dies
                        people_alive -= 1

                if ball.rect.left <= screen_rect.left:
                        reset_ball()
                        #ball.rect.center = screen_rect.center
                        #ball.initial_speed_x = get_random_int(-5, 5)
                        #ball.initial_speed_y = get_random_int(-5, 5)
                        #ball.speed_x = ball.initial_speed_x
                        #ball.speed_y = ball.initial_speed_y
                        white.alive = 0 #White dies
                        people_alive -= 1


                # Screen blit
        
                screen.blit(white.surf, white.rect)
                screen.blit(white.shield_surf, white.shield_rect)
                if white.alive == False: screen.blit(white.death_barrier_surf, white.death_barrier_rect)

                screen.blit(green.surf, green.rect)
                screen.blit(green.shield_surf, green.shield_rect)
                if green.alive == False: screen.blit(green.death_barrier_surf, green.death_barrier_rect)

                screen.blit(red.surf, red.rect)
                screen.blit(red.shield_surf, red.shield_rect)
                if red.alive == False: screen.blit(red.death_barrier_surf, red.death_barrier_rect)

                screen.blit(blue.surf, blue.rect)
                screen.blit(blue.shield_surf, blue.shield_rect)
                if blue.alive == False: screen.blit(blue.death_barrier_surf, blue.death_barrier_rect)

                screen.blit(ball.surf, ball.rect)

                # Game_ending_variable



                if people_alive == 1 and people_playing > 1: 
                        for x in player_list:
                                if x.alive == 1: x.win_count += 1
                                if x.alive == 0 and x.plays == 1: x.lose_count += 1
                        game_active = False
                elif people_playing == 1 and people_alive == 0:
                        game_active = False

        ## End game results ##
        if game_active == False and game_start == False:

                game_over_surf = start_font.render("Press Space to start again", False, "Yellow")
                game_over_rect = game_over_surf.get_rect(center = (screen_rect.centerx, screen_rect.centery))
                screen.blit(game_over_surf, game_over_rect)
                final_score_surf = start_font.render(f"Your score: {score}", False, "Yellow")
                final_score_rect = final_score_surf.get_rect (midbottom = (screen_rect.centerx, (game_over_rect.top - 20)))
                if people_playing == 1: screen.blit(final_score_surf, final_score_rect) #Score_variable

                # Player winning
                if people_alive == 1:
                        for x in player_list:
                                if x.alive == 1:
                                        
                                        winner_surf = start_font.render(f"Rounds won: {x.win_count}", False, x.color)
                                        winner_rect = winner_surf.get_rect(midtop = (game_over_rect.centerx, (game_over_rect.bottom + 20)))
                                        screen.blit(winner_surf, winner_rect)
                                        player_winner_rect = x.surf.get_rect(midtop = (winner_rect.centerx, (winner_rect.bottom + 20)))
                                        screen.blit(x.surf, player_winner_rect)

                # Player losing
                if people_alive > 1:
                        for x in player_list:
                                if x.plays == 1 and x.alive == 0:
                                        
                                        loser_surf = start_font.render(f"Rounds lost: {x.lose_count}", False, x.color)
                                        loser_rect = loser_surf.get_rect(midtop = (game_over_rect.centerx, (game_over_rect.bottom + 20)))
                                        screen.blit(loser_surf, loser_rect)
                                        player_loser_rect = x.surf.get_rect(midtop = (loser_rect.centerx, (loser_rect.bottom + 20)))
                                        screen.blit(x.surf, player_loser_rect)


                if keys[pygame.K_SPACE]:
                        game_active = True

                        white.alive = white.plays
                        white.rect.centery = screen_rect.centery
                        white.shield_rect.centery = screen_rect.centery

                        red.alive = red.plays
                        red.rect.centerx = screen_rect.centerx
                        red.shield_rect.centerx = screen_rect.centerx

                        green.alive = green.plays
                        green.rect.centery = screen_rect.centery
                        green.shield_rect.centery = screen_rect.centery

                        blue.alive = blue.plays
                        blue.rect.centerx = screen_rect.centerx
                        blue.shield_rect.centerx = screen_rect.centerx

                        people_alive = white.alive + red.alive + green.alive + blue.alive
                        start_time = pygame.time.get_ticks()
                        

        pygame.display.update()
        clock.tick(60)
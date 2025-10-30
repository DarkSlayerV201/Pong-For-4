import pygame
from sys import exit
from random import randint

pygame.init()

### Screen variales ###

screen_ratio = 1 / 1
screen_height = 800
screen_width = screen_height * screen_ratio
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
pygame.display.set_caption("Pong For 4")
if screen_ratio < 1: 
        start_font_size = screen_width / 20
        instructions_font_size = screen_width / 50
else:
        start_font_size = screen_height / 20
        instructions_font_size = screen_height / 50
instructions_font = pygame.font.Font("Pong For 4/Font/ci-gamedev.ttf", int(instructions_font_size))
start_font = pygame.font.Font("Pong For 4/Font/ci-gamedev.ttf", int(start_font_size))


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

### Ball class ###
class moving_object:
        def __init__(self, image, x, y):
                self.surf = pygame.transform.scale((pygame.image.load(image)), ((screen_width / 20), screen_height / 20)) #Ball size should be (50, 50) when screen is (1000, 1000)
                self.rect = self.surf.get_rect(center = (x, y))
                self.initial_speed_x = get_random_int(-5, 5)
                self.initial_speed_y = get_random_int(-5, 5)
                self.speed_x = self.initial_speed_x
                self.speed_y = self.initial_speed_y
                self.acceleration = get_random_float(2, 10, 1000)
                pass

ball = moving_object("Pong For 4/Ball/White ball.png", screen_rect.centerx, screen_rect.centery)


### Player class ###
class player:
        def __init__(self, image, x, y, shield, position, controls, color_value, plays, wins, loses):
                
                self.surf = pygame.transform.scale((pygame.image.load(image).convert_alpha()), ((screen_width / 12.5), screen_height / 12.5)) #Player size should be (80, 80) when screen is (1000, 1000)
                self.rect = self.surf.get_rect(center = (x, y))

                if position == "left" or position == "right":
                        self.shield_surf = pygame.transform.scale((pygame.image.load(shield)), ((screen_width / 50), (screen_height / (25 / 6)))) #Shield size should be (20, 240) when screen is (1000, 1000)
                        self.death_barrier_surf = pygame.transform.scale((pygame.image.load("Pong For 4/Barriers/Death.png")), ((screen_width / 50), screen_height)) #Death barrier size should be (20, 1000) when screen is (1000, 1000)

                        if position == "left": 
                                self.shield_rect = self.shield_surf.get_rect(midleft = (self.rect.right, y))
                                self.death_barrier_rect = self.death_barrier_surf.get_rect(midleft = (self.rect.right, y))

                        elif position == "right": 
                                self.shield_rect = self.shield_surf.get_rect(midright = (self.rect.left, y))
                                self.death_barrier_rect = self.death_barrier_surf.get_rect(midright = (self.rect.left, y))

                elif position == "top" or position == "bottom":
                        self.shield_surf = pygame.transform.scale((pygame.image.load(shield)), ((screen_width / (25 / 6)), (screen_height / 50))) #Shield size should be (240, 20) when screen is (1000, 1000)
                        self.death_barrier_surf = pygame.transform.scale((pygame.image.load("Pong For 4/Barriers/Death.png")), (screen_width, (screen_height / 50))) #Death barrier size should be (20, 1000) when screen is (1000, 1000)
                        
                        if position == "top": 
                                self.shield_rect = self.shield_surf.get_rect(midtop = (x, self.rect.bottom))
                                self.death_barrier_rect = self.death_barrier_surf.get_rect(midtop = (x, self.rect.bottom))

                        elif position == "bottom":
                                self.shield_rect = self.shield_surf.get_rect(midbottom = (x, self.rect.top))
                                self.death_barrier_rect = self.death_barrier_surf.get_rect(midbottom = (x, self.rect.top))

                else: print("Error al asignar posición") #Error

                self.speed = 5
                self.acceleration = 0
                self.plays = plays
                self.alive = self.plays
                self.win_count = wins
                self.lose_count = loses
                self.color = color_value
                self.position = position
                if position in ["left", "right"]: self.movement_axis = "y"
                elif position in ["top", "bottom"]: self.movement_axis = "x"
                else: print("Error al asignar eje") #Error

                self.instructions_surf = instructions_font.render(controls, False, color_value)
                self.instructions_rect = self.instructions_surf.get_rect(center = (x, y))

                pass

        def stops_playing(self):
                self.plays = 0
                self.alive = 0
                self.instructions_surf = instructions_font.render("Not playing", False, "Grey")
                pass

        def dies(self):
                reset_ball()
                self.alive = 0
                global people_alive
                people_alive -= 1
                pass

        def display_instructions(self):
                screen.blit(self.instructions_surf, self.instructions_rect)
                pass

        def moves(self, direction):
                if direction in ["up", "left"]: direction = -1
                elif direction in ["down", "right"]: direction = 1
                else: print("Error al asignar dirección") #Error
                if self.movement_axis == "x":
                        self.rect.x += direction * self.speed
                        self.shield_rect.x += direction * self.speed
                        self.acceleration = direction * 2
                elif self.movement_axis == "y":
                        self.rect.y += direction * self.speed
                        self.shield_rect.y += direction * self.speed
                        self.acceleration = direction * 2
                else: print("Error al asignar eje") #Error
                pass

        def collides_with_ball(self):
                if self.movement_axis == "x":
                        ball.speed_y = -ball.speed_y
                        ball.speed_x = ball.speed_x + self.acceleration
                        if self.position == "top": ball.rect.top = self.shield_rect.bottom
                        elif self.position == "bottom": ball.rect.bottom = self.shield_rect.top
                elif self.movement_axis == "y":
                        ball.speed_x = -ball.speed_x
                        ball.speed_y = ball.speed_y + self.acceleration
                        if self.position == "left": ball.rect.left = self.shield_rect.right
                        elif self.position == "right": ball.rect.right = self.shield_rect.left
                else: print("Error al asignar eje") #Error
                pass

        def reset_position(self):
                self.alive = self.plays
                if self.position == "left" or self.position == "right":
                        self.rect.centery = screen_rect.centery
                        self.shield_rect.centery = screen_rect.centery
                elif self.position == "top" or self.position == "bottom":
                        self.rect.centerx = screen_rect.centerx
                        self.shield_rect.centerx = screen_rect.centerx
                else: print("Error al asignar posición") #Error
                pass


### Players
white = player("Pong For 4/Players/White.png", (screen_width / 10), screen_rect.centery, "Pong For 4/Barriers/White.png", "left", "W/S", "White", 1, 0, 0)
green = player("Pong For 4/Players/Green.png", (screen_rect.right - (screen_width / 10)), screen_rect.centery, "Pong For 4/Barriers/Green.png", "right", "Num 8/Num 2", "Green", 1, 0, 0)
red = player("Pong For 4/Players/Red.png", screen_rect.centerx, (screen_height / 10), "Pong For 4/Barriers/Red.png", "top", "N/M", "Red", 1, 0, 0)
blue = player("Pong For 4/Players/Blue.png", screen_rect.centerx, (screen_rect.bottom - (screen_height / 10)), "Pong For 4/Barriers/Blue.png", "bottom", "Left/Right", "Blue", 1, 0, 0)
player_list = [white, red, green, blue]

### Game variables ###
clock = pygame.time.Clock()
game_active = False
game_start = True
start_time = 0
score = 0

### Main loop ###
while True:
        for event in pygame.event.get(): # Inputs #
                if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                if event.type == pygame.MOUSEBUTTONDOWN and game_start == True: # Disabling players before game starts #
                        for x in player_list: 
                                if x.instructions_rect.collidepoint(event.pos): x.stops_playing()
        
        ## Keyboard and background ##
        keys = pygame.key.get_pressed()
        background = pygame.draw.rect(screen, "Black", screen_rect)
        
        if game_start and game_active == False: ## Start screen ##
                for x in player_list: x.display_instructions()
                        
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

                # Variables #
                people_playing = white.plays + red.plays + green.plays + blue.plays
                people_alive = white.alive + red.alive + green.alive + blue.alive
                if people_playing == 1: score = display_score()

                # Player inputs #
                for x in player_list: x.acceleration = 0

                if white.alive == 1: # White inputs #
                        if keys[pygame.K_s]: white.moves("down")
                        if keys[pygame.K_w]: white.moves("up")

                if green.alive == 1: # Green inputs #
                        if keys[pygame.K_KP2]: green.moves("down")
                        if keys[pygame.K_KP8]: green.moves("up")

                if red.alive == 1: # Red inputs #
                        if keys[pygame.K_m]: red.moves("right")
                        if keys[pygame.K_n]: red.moves("left")

                if blue.alive == 1: # Blue inputs #
                        if keys[pygame.K_RIGHT]: blue.moves("right")
                        if keys[pygame.K_LEFT]: blue.moves("left")

                

                for x in player_list: # Ball-players collisions #
                        if x.alive == 1:
                                if ball.rect.colliderect(x.shield_rect): x.collides_with_ball()
                        else:
                                if ball.rect.colliderect(x.death_barrier_rect): x.collides_with_ball()

                # Ball acceleration and movement #
                if ball.speed_x > 0: ball.speed_x += ball.acceleration
                elif ball.speed_x < 0: ball.speed_x -= ball.acceleration
                else: print("Error: ball.speed_x == 0")
                
                if ball.speed_y > 0: ball.speed_y += ball.acceleration
                elif ball.speed_y < 0: ball.speed_y -= ball.acceleration
                else: print("Error: ball.speed_y == 0")

                ball.rect.x += ball.speed_x 
                ball.rect.y += ball.speed_y

                # Ball-screen collisions #
                if ball.rect.top <= screen_rect.top: red.dies()
                if ball.rect.bottom >= screen_rect.bottom: blue.dies()
                if ball.rect.right >= screen_rect.right: green.dies()
                if ball.rect.left <= screen_rect.left: white.dies()

                # Screen blit #

                for x in player_list:
                        screen.blit(x.shield_surf, x.shield_rect)
                        screen.blit(x.surf, x.rect)
                        if x.alive == False: screen.blit(x.death_barrier_surf, x.death_barrier_rect)
                screen.blit(ball.surf, ball.rect)

                # Game_ending_variables #
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

                # Player winning #
                if people_alive == 1:
                        for x in player_list:
                                if x.alive == 1:
                                        winner_surf = start_font.render(f"Rounds won: {x.win_count}", False, x.color)
                                        winner_rect = winner_surf.get_rect(midtop = (game_over_rect.centerx, (game_over_rect.bottom + 20)))
                                        screen.blit(winner_surf, winner_rect)
                                        player_winner_rect = x.surf.get_rect(midtop = (winner_rect.centerx, (winner_rect.bottom + 20)))
                                        screen.blit(x.surf, player_winner_rect)

                # Player losing #
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
                        for x in player_list: x.reset_position()
                        people_alive = white.alive + red.alive + green.alive + blue.alive
                        start_time = pygame.time.get_ticks()

        pygame.display.update()
        clock.tick(60)
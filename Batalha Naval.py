#import the needed libraries
import pygame
import os
import random
import time
from datetime import datetime

try:
    sleep_time = int(input("Indica a duração, em segundos, de cada mensagem: "))
except ValueError:
    sleep_time = 5

#start the game
pygame.init()

#configure the gameboard
WIDTH, HEIGHT = 1280, 800
GRID_SIZE = 6
CELL_SIZE = int((0.8 * min(WIDTH, HEIGHT)) / GRID_SIZE)
gameboard = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Batalha Naval')

#set the colours
blue = (0, 75, 148)
#gold = (194, 151, 13) might use it
black = (0, 0, 0)
white = (255, 255, 255)

#set the frames per second rate
FPS = 60

#import and resize images
boat_1_image = pygame.image.load(os.path.join('Assets', 'boat 1.png'))
boat_1 = pygame.transform.scale(boat_1_image, (50, 105))
boat_2_image = pygame.image.load(os.path.join('Assets', 'boat 2.png'))
boat_2 = pygame.transform.scale(boat_2_image, (30, 100))
boat_3_image = pygame.image.load(os.path.join('Assets', 'boat 3.png'))
boat_3 = pygame.transform.scale(boat_3_image, (30, 100))
logo_image = pygame.image.load(os.path.join('Assets', 'Icon.png'))
logo_ = pygame.transform.scale(logo_image, (93, 100))

#load music files
music_1 = pygame.mixer.music.load(os.path.join('Assets','music 5.mp3'))
music_2 = pygame.mixer.music.load(os.path.join('Assets','music 4.mp3'))
music_3 = pygame.mixer.music.load(os.path.join('Assets','music 3.mp3'))
music_4 = pygame.mixer.music.load(os.path.join('Assets','music 2.mp3'))
music_5 = pygame.mixer.music.load(os.path.join('Assets','music 1.mp3'))

#play the music
#pygame.mixer.music.play(-1)

#define different fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)
extra_small_font = pygame.font.Font(None, 20)
big_font = pygame.font.Font(None, 50)

#authors text
authors_text = 'Turma de Aplicações Informáticas do 12º ano (2023/2024)'
authors_surface = extra_small_font.render(authors_text, True, black)

#initial message text
initial_message_text = 'Barcos a colocar:'
initial_surface = font.render(initial_message_text, True, black)

#messages text
messages_text = 'Mensagens:'
text_surface = font.render(messages_text, True, black)

#message 1
message1_text = 'Tudo a postos.'
message1_text2 = 'Manda um míssil!'
message1_surface = small_font.render(message1_text, True, black)
message1_surface2 = small_font.render(message1_text2, True, black)

#regists text
regists_text = 'Registos:'
regists_surface = font.render(regists_text, True, black)

#plays text
question_plays_text = 'Qual é o alvo'
question_plays_text2 = 'a atingir?'
plays_text__1 = ''

plays_box__1 = pygame.Rect(1000, 560, 200, 32)
plays_box_colour = black
write_plays__1 = False
modify_plays__1 = True

question_plays_surface1 = small_font.render(question_plays_text, True, black)
question_plays_surface2 = small_font.render(question_plays_text2, True, black)
plays_surface__1 = font.render(plays_text__1, True, plays_box_colour)
player_target_text__1 = ''

#input text 1
question_text = 'Barco 1:'
user_text = ''

input_box = pygame.Rect(1000, 200, 200, 32)
input_box_colour = black
write = False
modify = True

text_surface1 = font.render(question_text, True, black)
text_surface2 = font.render(user_text, True, input_box_colour)
saved_text = ''

#input text 2
question_text2 = 'Barco 2:'
user_text2 = ''

input_box2 = pygame.Rect(1000, 400, 200, 32)
write2 = False
modify2 = True

text_surface12 = font.render(question_text2, True, black)
text_surface22 = font.render(user_text2, True, input_box_colour)
saved_text2 = ''

#input text 3
question_text3 = 'Barco 3:'
user_text3 = ''

input_box3 = pygame.Rect(1000, 600, 200, 32)
write3 = False
modify3 = True

text_surface13 = font.render(question_text3, True, black)
text_surface23 = font.render(user_text3, True, input_box_colour)
saved_text3 = ''

def register_time():
    time = datetime.now()

    f_time = time.strftime("%H:%M:%S")

    hours = int(f_time[0:2]) * 3600
    minutes = int(f_time[3:5]) * 60
    seconds = int(f_time[6:8])
    sum = hours + minutes + seconds
    return (f_time, sum)

#draw the gameboard
def draw_gameboard(z, plays_surface__1, player_target_text__1):
    gameboard.fill(blue)

    board_width = GRID_SIZE * CELL_SIZE
    board_height = GRID_SIZE * CELL_SIZE
    x_offset = (WIDTH - board_width) // 2
    y_offset = (HEIGHT - board_height) // 2

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = x_offset + col * CELL_SIZE
            y = y_offset + row * CELL_SIZE
            pygame.draw.rect(gameboard, black, (x, y, CELL_SIZE, CELL_SIZE), 2)

            if row == 0:
                font = pygame.font.Font(None, 36)
                text = font.render(chr(65 + col), True, black)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y - 20))
                gameboard.blit(text, text_rect)

            if col == 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(row + 1), True, black)
                text_rect = text.get_rect(center=(x - 20, y + CELL_SIZE // 2))
                gameboard.blit(text, text_rect)

    #draw the boats and other images
    gameboard.blit(boat_1, (boat1.x, boat1.y))
    gameboard.blit(boat_2, (boat2.x, boat2.y))
    gameboard.blit(boat_3, (boat3.x, boat3.y))
    gameboard.blit(logo_, (logo.x, logo.y))

    #draw authors text
    gameboard.blit(authors_surface, (10, 770))

    #draw initial message text
    gameboard.blit(initial_surface, (50, 125))

    #draw input text 1
    gameboard.blit(text_surface1, (1000, 150))
    pygame.draw.rect(gameboard, input_box_colour, input_box, 2)
    gameboard.blit(text_surface2, (input_box.x + 5, input_box.y + 5))

    #draw input text 2
    gameboard.blit(text_surface12, (1000, 350))
    pygame.draw.rect(gameboard, input_box_colour, input_box2, 2)
    gameboard.blit(text_surface22, (input_box2.x + 5, input_box2.y + 5))

    #draw input text 3
    gameboard.blit(text_surface13, (1000, 550))
    pygame.draw.rect(gameboard, input_box_colour, input_box3, 2)
    gameboard.blit(text_surface23, (input_box3.x + 5, input_box3.y + 5))

    #begin the battle
    if z == 1:

        #remove the input text boxes since they're not needed anymore
        pygame.draw.rect(gameboard, blue, (WIDTH // 1.3, 0, WIDTH // 2, HEIGHT))
        pygame.draw.rect(gameboard, blue, (45, 120, 220, 50))

        #draw messages text
        gameboard.blit(text_surface, (50, 125))

        #display the message that the battle will commence
        gameboard.blit(message1_surface, (50, 200))
        gameboard.blit(message1_surface2, (50, 230))

        #display the regists to show the game state
        gameboard.blit(regists_surface, (1000, 125))

        #display the game state
        display_game_state()

        #draw the text for the user to select a target to hit
        gameboard.blit(question_plays_surface1, (1000, 500))
        gameboard.blit(question_plays_surface2, (1000, 525))


        pygame.draw.rect(gameboard, plays_box_colour, plays_box__1, 2)
        gameboard.blit(plays_surface__1, (plays_box__1.x + 5, plays_box__1.y + 5))

        if player_target_text__1 in cpu_choices:
            pygame.draw.rect(gameboard, blue, (45, 160, 250, 200))
            display_message('Míssil lançado.')

            if player_target_text__1 in cpu_boats:
                display_message2('O míssil atingiu um barco!')
                time.sleep(3)
                cpu_boats.remove(player_target_text__1)

            elif player_target_text__1 not in cpu_boats:
                display_message2('O míssil caiu na água.')
                time.sleep(3)

            if len(cpu_guess) == 2:
                pygame.draw.rect(gameboard, blue, (45, 160, 250, 200))
                display_message('O oponente lançou um míssil.')

                if cpu_guess in player_boats:
                    display_message2('O míssil atingiu um barco!')
                    time.sleep(3)
                    player_boats.remove(cpu_guess)

                elif cpu_guess not in player_boats:
                    display_message2('O míssil caiu na água.')
                    time.sleep(3)

                reset_text()

        if player_missiles == 0:

            if len(cpu_boats) < len(player_boats):
                final_message('Vitória!', 'Venceste o jogo. Parabéns!')

            elif len(cpu_boats) > len(player_boats):
                final_message('Perdeste.', 'Podes tentar de novo se quiseres.')

            elif len(cpu_boats) == len(player_boats):
                final_message('Empate.', 'Sabor amargo... Vê lá se consegues da próxima.')

        elif len(cpu_boats) == 0:
            final_message('Vitória!', 'Venceste o jogo. Parabéns!')

        elif len(player_boats) == 0:
            final_message('Perdeste.', 'Podes tentar de novo se quiseres.')

    #update the gameboard
    pygame.display.update()


#create skip variable
skip = False

skip_text = 'Para pular o tutorial, prima "ENTER".'
skip_surface1 = small_font.render(skip_text, True, black)


#functions to show a specific message
def opening_message(opening_message):
    text = big_font.render(opening_message, True, black)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2.3))

    gameboard.fill(blue)
    gameboard.blit(text, text_rect)
    gameboard.blit(skip_surface1, (910, 750))
    pygame.display.update()


def opening_message2(opening_message2):
    text = big_font.render(opening_message2, True, black)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    gameboard.blit(text, text_rect)
    pygame.display.update()


def display_message(message):
    text = small_font.render(message, True, black)

    gameboard.blit(text, (50, 200))
    pygame.display.update()


def display_message2(message):
    text = small_font.render(message, True, black)

    gameboard.blit(text, (50, 230))
    pygame.display.update()


#function to show the state of the 6 boats
def display_game_state():
    gameboard.blit(game_state_surface1, (1000, 200))
    gameboard.blit(game_state_surface2, (1000, 240))
    gameboard.blit(game_state_surface3, (1000, 270))
    gameboard.blit(game_state_surface1cpu, (1000, 340))
    gameboard.blit(game_state_surface2cpu, (1000, 380))
    gameboard.blit(game_state_surface3cpu, (1000, 410))
    gameboard.blit(game_state_armament_surface, (50, 525))
    gameboard.blit(game_state_missiles_surface, (50, 600))

#function to reset the plays text
def reset_text():
    global plays_text__1
    global player_target_text__1
    global modify_plays__1
    plays_text__1 = ''
    player_target_text__1 = ''
    modify_plays__1 = True

def final_message(final_message1, final_message2):
    text1 = big_font.render(final_message1, True, black)
    text_rect1 = text1.get_rect(center=(WIDTH // 2, HEIGHT - 600))
    text2 = big_font.render(final_message2, True, black)
    text_rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    gameboard.fill(blue)
    gameboard.blit(text1, text_rect1) 
    gameboard.blit(text2, text_rect2)
    pygame.display.update()


#write the images' coordinates
boat1 = pygame.Rect(80, 200, 50, 105)
boat2 = pygame.Rect(88, 350, 30, 100)
boat3 = pygame.Rect(88, 500, 30, 100)
logo = pygame.Rect(0, 0, 103, 88)


#introduce the user to the game with skip feature
if not skip:
    intro_messages = [
        ['Olá. Seja bem-vindo ao jogo simplificado da batalha naval!'],
        ['Este jogo foi feito pela turma de 12ºA de Aplicações Informáticas B.'],
        ['Depois de esta mensagem introdutória, poderás jogar o nosso jogo.'],
        ['Mas antes, precisas de saber as regras.'],
        ['No início do jogo, terás um tabuleiro onde irás colocar os teus barcos',
        'através das caixas de texto que estarão na direita da tela.'],
        ['Tens de colocar os 3 barcos em posições diferentes!'],
        ['Uma vez colocados, poderás escolher uma coordenada',
        'para atingir.'],
        ['Terás 25 tentativas e tens de destruir os 3 barcos',
        'do adversário'],
        ['Ganha quem destruir os 3 barcos do outro primeiro',
        'ou quem destruir mais após as 25 rodadas.'],
        ['Se o número de barcos abatidos for igual',
        'será declarado um empate.'],
        ['Boa sorte!']
    ]
    for msg in intro_messages:
        # Process events to allow skipping
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                skip = True
        if skip:
            break
        opening_message(msg[0])
        if len(msg) == 2:
            opening_message2(msg[1])
            time.sleep(sleep_time / 2) if skip == False else None
        time.sleep(sleep_time) if skip == False else None


#start the time counter
f_start_time, start_time = register_time()

#write the main loop
clock = pygame.time.Clock()
run = True
player_boats = []
player_missiles = 25
cpu_guess = ""
z = 0

#give the cpu (opponent) the positions of its boats
cpu_choices = ['A1', 'A2' , 'A3', 'A4', 'A5', 'A6', 'B1' , 'B2', 'B3', 'B4', 'B5', 'B6', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6']
cpu_choices2 = ['A1', 'A2' , 'A3', 'A4', 'A5', 'A6', 'B1' , 'B2', 'B3', 'B4', 'B5', 'B6', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6']
cpu_boats = random.sample(cpu_choices, 3)

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():

        #condition to leave the game
        if event.type == pygame.QUIT:
            run = False

        #condition for input text 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                write = True

            else:
                write = False

            input_box_colour = black if write else black

        if event.type == pygame.KEYDOWN and write and modify:

            if event.key == pygame.K_BACKSPACE or len(user_text) > 2:
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                saved_text = user_text.upper()
                
                if saved_text not in player_boats:

                    match saved_text:

                        case 'A1':
                            boat1.x = 351
                            boat1.y = 84
                            player_boats.append(saved_text)
                            modify = False

                        case 'A2':
                            boat1.x = 351
                            boat1.y = 190
                            player_boats.append(saved_text)
                            modify = False

                        case 'A3':
                            boat1.x = 351
                            boat1.y = 297
                            player_boats.append(saved_text)
                            modify = False

                        case 'A4':
                            boat1.x = 351
                            boat1.y = 403
                            player_boats.append(saved_text)
                            modify = False

                        case 'A5':
                            boat1.x = 351
                            boat1.y = 509
                            player_boats.append(saved_text)
                            modify = False

                        case 'A6':
                            boat1.x = 351
                            boat1.y = 615
                            player_boats.append(saved_text)
                            modify = False

                        case 'B1':
                            boat1.x = 457
                            boat1.y = 84
                            player_boats.append(saved_text)
                            modify = False

                        case 'B2':
                            boat1.x = 457
                            boat1.y = 190
                            player_boats.append(saved_text)
                            modify = False

                        case 'B3':
                            boat1.x = 457
                            boat1.y = 297
                            player_boats.append(saved_text)
                            modify = False

                        case 'B4':
                            boat1.x = 457
                            boat1.y = 403
                            player_boats.append(saved_text)
                            modify = False

                        case 'B5':
                            boat1.x = 457
                            boat1.y = 509
                            player_boats.append(saved_text)
                            modify = False

                        case 'B6':
                            boat1.x = 457
                            boat1.y = 615
                            player_boats.append(saved_text)
                            modify = False

                        case 'C1':
                            boat1.x = 563
                            boat1.y = 84
                            player_boats.append(saved_text)
                            modify = False

                        case 'C2':
                            boat1.x = 563
                            boat1.y = 190
                            player_boats.append(saved_text)
                            modify = False

                        case 'C3':
                            boat1.x = 563
                            boat1.y = 297
                            player_boats.append(saved_text)
                            modify = False

                        case 'C4':
                            boat1.x = 563
                            boat1.y = 403
                            player_boats.append(saved_text)
                            modify = False

                        case 'C5':
                            boat1.x = 563
                            boat1.y = 509
                            player_boats.append(saved_text)
                            modify = False

                        case 'C6':
                            boat1.x = 563
                            boat1.y = 615
                            player_boats.append(saved_text)
                            modify = False

                        case 'D1':
                            boat1.x = 669
                            boat1.y = 84
                            player_boats.append(saved_text)
                            modify = False

                        case 'D2':
                            boat1.x = 669
                            boat1.y = 190
                            player_boats.append(saved_text)
                            modify = False

                        case 'D3':
                            boat1.x = 669
                            boat1.y = 297
                            player_boats.append(saved_text)
                            modify = False

                        case 'D4':
                            boat1.x = 669
                            boat1.y = 403
                            player_boats.append(saved_text)
                            modify = False

                        case 'D5':
                            boat1.x = 669
                            boat1.y = 509
                            player_boats.append(saved_text)
                            modify = False

                        case 'D6':
                            boat1.x = 669
                            boat1.y = 615
                            player_boats.append(saved_text)
                            modify = False

                        case 'E1':
                            boat1.x = 775
                            boat1.y = 84
                            player_boats.append(saved_text)
                            modify = False

                        case 'E2':
                            boat1.x = 775
                            boat1.y = 190
                            player_boats.append(saved_text)
                            modify = False

                        case 'E3':
                            boat1.x = 775
                            boat1.y = 297
                            player_boats.append(saved_text)
                            modify = False

                        case 'E4':
                            boat1.x = 775
                            boat1.y = 403
                            player_boats.append(saved_text)
                            modify = False

                        case 'E5':
                            boat1.x = 775
                            boat1.y = 509
                            player_boats.append(saved_text)
                            modify = False

                        case 'E6':
                            boat1.x = 775
                            boat1.y = 615
                            player_boats.append(saved_text)
                            modify = False

                        case 'F1':
                            boat1.x = 881
                            boat1.y = 84
                            player_boats.append(saved_text)
                            modify = False

                        case 'F2':
                            boat1.x = 881
                            boat1.y = 190
                            player_boats.append(saved_text)
                            modify = False

                        case 'F3':
                            boat1.x = 881
                            boat1.y = 297
                            player_boats.append(saved_text)
                            modify = False

                        case 'F4':
                            boat1.x = 881
                            boat1.y = 403
                            player_boats.append(saved_text)
                            modify = False

                        case 'F5':
                            boat1.x = 881
                            boat1.y = 509
                            player_boats.append(saved_text)
                            modify = False

                        case 'F6':
                            boat1.x = 881
                            boat1.y = 615
                            player_boats.append(saved_text)
                            modify = False
            
            else:
                user_text += event.unicode

            text_surface2 = font.render(user_text, True, input_box_colour)

        #condition for input text 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box2.collidepoint(event.pos):
                write2 = True

            else:
                write2 = False

            input_box_colour = black if write2 else black

        if event.type == pygame.KEYDOWN and write2 and modify2:

            if event.key == pygame.K_BACKSPACE or len(user_text2) > 2:
                user_text2 = user_text2[:-1]

            elif event.key == pygame.K_RETURN:
                saved_text2 = user_text2.upper()

                if saved_text2 not in player_boats:

                    match saved_text2:

                        case 'A1':
                            boat2.x = 359
                            boat2.y = 86
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'A2':
                            boat2.x = 359
                            boat2.y = 192
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'A3':
                            boat2.x = 359
                            boat2.y = 298
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'A4':
                            boat2.x = 359
                            boat2.y = 404
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'A5':
                            boat2.x = 359
                            boat2.y = 510
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'A6':
                            boat2.x = 359
                            boat2.y = 616
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'B1':
                            boat2.x = 465
                            boat2.y = 86
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'B2':
                            boat2.x = 465
                            boat2.y = 192
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'B3':
                            boat2.x = 465
                            boat2.y = 298
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'B4':
                            boat2.x = 465
                            boat2.y = 404
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'B5':
                            boat2.x = 465
                            boat2.y = 510
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'B6':
                            boat2.x = 465
                            boat2.y = 616
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'C1':
                            boat2.x = 571
                            boat2.y = 86
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'C2':
                            boat2.x = 571
                            boat2.y = 192
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'C3':
                            boat2.x = 571
                            boat2.y = 298
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'C4':
                            boat2.x = 571
                            boat2.y = 404
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'C5':
                            boat2.x = 571
                            boat2.y = 510
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'C6':
                            boat2.x = 571
                            boat2.y = 616
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'D1':
                            boat2.x = 677
                            boat2.y = 86
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'D2':
                            boat2.x = 677
                            boat2.y = 192
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'D3':
                            boat2.x = 677
                            boat2.y = 298
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'D4':
                            boat2.x = 677
                            boat2.y = 404
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'D5':
                            boat2.x = 677
                            boat2.y = 510
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'D6':
                            boat2.x = 677
                            boat2.y = 616
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'E1':
                            boat2.x = 783
                            boat2.y = 86
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'E2':
                            boat2.x = 783
                            boat2.y = 192
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'E3':
                            boat2.x = 783
                            boat2.y = 298
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'E4':
                            boat2.x = 783
                            boat2.y = 404
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'E5':
                            boat2.x = 783
                            boat2.y = 510
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'E6':
                            boat2.x = 783
                            boat2.y = 616
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'F1':
                            boat2.x = 889
                            boat2.y = 86
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'F2':
                            boat2.x = 889
                            boat2.y = 192
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'F3':
                            boat2.x = 889
                            boat2.y = 298
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'F4':
                            boat2.x = 889
                            boat2.y = 404
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'F5':
                            boat2.x = 889
                            boat2.y = 510
                            player_boats.append(saved_text2)
                            modify2 = False

                        case 'F6':
                            boat2.x = 889
                            boat2.y = 616
                            player_boats.append(saved_text2)
                            modify2 = False

            else:
                user_text2 += event.unicode

            text_surface22 = font.render(user_text2, True, input_box_colour)


        #condition for input text 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box3.collidepoint(event.pos):
                write3 = True

            else:
                write3 = False

            input_box_colour = black if write3 else black

        if event.type == pygame.KEYDOWN and write3 and modify3:

            if event.key == pygame.K_BACKSPACE or len(user_text3) > 2:
                user_text3 = user_text3[:-1]

            elif event.key == pygame.K_RETURN:
                saved_text3 = user_text3.upper()

                if saved_text3 not in player_boats:

                    match saved_text3:

                        case 'A1':
                            boat3.x = 359
                            boat3.y = 83
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'A2':
                            boat3.x = 359
                            boat3.y = 189
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'A3':
                            boat3.x = 359
                            boat3.y = 295
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'A4':
                            boat3.x = 359
                            boat3.y = 401
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'A5':
                            boat3.x = 359
                            boat3.y = 507
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'A6':
                            boat3.x = 359
                            boat3.y = 613
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'B1':
                            boat3.x = 465
                            boat3.y = 83
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'B2':
                            boat3.x = 465
                            boat3.y = 189
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'B3':
                            boat3.x = 465
                            boat3.y = 295
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'B4':
                            boat3.x = 465
                            boat3.y = 401
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'B5':
                            boat3.x = 465
                            boat3.y = 507
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'B6':
                            boat3.x = 465
                            boat3.y = 613
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'C1':
                            boat3.x = 571
                            boat3.y = 83
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'C2':
                            boat3.x = 571
                            boat3.y = 189
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'C3':
                            boat3.x = 571
                            boat3.y = 295
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'C4':
                            boat3.x = 571
                            boat3.y = 401
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'C5':
                            boat3.x = 571
                            boat3.y = 507
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'C6':
                            boat3.x = 571
                            boat3.y = 613
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'D1':
                            boat3.x = 677
                            boat3.y = 83
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'D2':
                            boat3.x = 677
                            boat3.y = 189
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'D3':
                            boat3.x = 677
                            boat3.y = 295
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'D4':
                            boat3.x = 677
                            boat3.y = 401
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'D5':
                            boat3.x = 677
                            boat3.y = 507
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'D6':
                            boat3.x = 677
                            boat3.y = 613
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'E1':
                            boat3.x = 783
                            boat3.y = 83
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'E2':
                            boat3.x = 783
                            boat3.y = 189
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'E3':
                            boat3.x = 783
                            boat3.y = 295
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'E4':
                            boat3.x = 783
                            boat3.y = 401
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'E5':
                            boat3.x = 783
                            boat3.y = 507
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'E6':
                            boat3.x = 783
                            boat3.y = 613
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'F1':
                            boat3.x = 889
                            boat3.y = 83
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'F2':
                            boat3.x = 889
                            boat3.y = 189
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'F3':
                            boat3.x = 889
                            boat3.y = 295
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'F4':
                            boat3.x = 889
                            boat3.y = 401
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'F5':
                            boat3.x = 889
                            boat3.y = 507
                            player_boats.append(saved_text3)
                            modify3 = False

                        case 'F6':
                            boat3.x = 889
                            boat3.y = 613
                            player_boats.append(saved_text3)
                            modify3 = False

            else:
                user_text3 += event.unicode

            text_surface23 = font.render(user_text3, True, input_box_colour)

        #game state text
        game_state_text1 = '- Jogador'
        game_state_text2 = f'   Barcos restantes: {len(player_boats)}'
        game_state_text3 = f'   Barcos destruídos: {3 - len(player_boats)}'
        game_state_surface1 = small_font.render(game_state_text1, True, black)
        game_state_surface2 = small_font.render(game_state_text2, True, black)
        game_state_surface3 = small_font.render(game_state_text3, True, black)

        game_state_text1cpu = '- Oponente (CPU)'
        game_state_text2cpu = f'    Barcos restantes: {len(cpu_boats)}'
        game_state_text3cpu = f'    Barcos destruídos: {3 - len(cpu_boats)}'
        game_state_surface1cpu = small_font.render(game_state_text1cpu, True, black)
        game_state_surface2cpu = small_font.render(game_state_text2cpu, True, black)
        game_state_surface3cpu = small_font.render(game_state_text3cpu, True, black)

        game_state_armament = 'Armamento:'
        game_state_armament_surface = font.render(game_state_armament, True, black)
        game_state_missiles = f'Mísseis restantes: {player_missiles}'
        game_state_missiles_surface = small_font.render(game_state_missiles, True, black)

        if len(player_boats) == 3:
            z = 1

        #condition for plays text 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if plays_box__1.collidepoint(event.pos):
                write_plays__1 = True

            else:
                write_plays__1 = False

            plays_box_colour = black if write_plays__1 else black

        if event.type == pygame.KEYDOWN and write_plays__1 and modify_plays__1:

            if event.key == pygame.K_BACKSPACE or len(plays_text__1) > 2:
                plays_text__1 = plays_text__1[:-1]

            elif event.key == pygame.K_RETURN and len(plays_text__1) == 2:
                player_target_text__1 = plays_text__1.upper()

                if player_target_text__1 in cpu_choices:
                    player_missiles -= 1
                    modify_plays__1 = False

                    cpu_guess = random.choice(cpu_choices2)
                    cpu_choices2.remove(cpu_guess)
                    print(cpu_boats)

            else:
                plays_text__1 += event.unicode

            plays_surface__1 = font.render(plays_text__1, True, plays_box_colour)

    draw_gameboard(z, plays_surface__1, player_target_text__1)

#stop the time counter and calculate the delta time
f_end_time, end_time = register_time()

delta_time = end_time - start_time

#leave the game
pygame.quit()

#create the file
file_name = "Batalha Naval - Dados da Execução.txt"

with open(file_name, "w") as f:
    f.write("Batalha Naval - Dados da Execução:\n")
    f.write("\n")
    f.write(f"  Hora de início: {f_start_time}\n")
    f.write(f"  Hora de fim: {f_end_time}\n")
    f.write(f"  Duração do jogo: {delta_time} segundos\n")
    #add the winners, boat information...
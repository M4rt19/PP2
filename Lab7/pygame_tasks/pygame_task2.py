import pygame
import os


def play_song(ind):
    pygame.mixer.music.load(songs[ind])
    pygame.mixer.music.play()


pygame.init()


HEIGHT, WEIGHT = 800, 500
screen = pygame.display.set_mode((HEIGHT, WEIGHT))
screen.fill((255, 255, 255))
pygame.display.set_caption("Music player")


pygame.display.update()
songs = []
ind = 0
directory = r"/Users/bmk/Documents/MyDocs/Student/3 Course 2 part/PP2/Lab7/songs"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename.endswith('.mp3'):
        songs.append(f)
print(songs)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            play_song(ind)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            pygame.mixer.music.stop()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            if ind < len(songs) - 1:
                ind += 1
                play_song(ind)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_j:
            if ind > 0:
                ind -= 1
                play_song(ind)
                
                
    screen.fill((255, 255, 255))
    f = pygame.font.SysFont(None, 36)
    
    text1 = f.render('PLAY - F', True, (0, 0, 0))
    text2 = f.render('STOP - G', True, (0, 0, 0))
    text3 = f.render('NEXT - H', True, (0, 0, 0))
    text4 = f.render('PREVIOUS - J', True, (0, 0, 0))



    screen.blit(text1, (10, 50))
    screen.blit(text2, (10, 100))
    screen.blit(text3, (10, 150))
    screen.blit(text4, (10, 200))
    
    img = f.render(f'Current music is {songs[ind].replace("/Users/bmk/Documents/MyDocs/Student/3 Course 2 part/PP2/Lab7/songs/", "")}', True, (0,0,255))
    screen.blit(img, (WEIGHT/2 - 100, HEIGHT/2))
    pygame.display.update()
    
    
"""
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_f]:
        play_song(ind)
    if pressed[pygame.K_g]:
        
    if pressed[pygame.K_h]:
        if ind < len(songs) - 1:
            ind += 1
            print(ind)
            play_song(ind)
    if pressed[pygame.K_j]:
        if ind >= 0:
            ind -= 1
            play_song(ind)
"""





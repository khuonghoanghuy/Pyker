import pygame
import saveData

def placeBG():
    bg = pygame.image.load('images/bg.png')
    pygame.display.get_surface().blit(bg, (0, 0))
    pygame.display.flip()

circle = pygame.image.load('images/circle.png') 
def getCircle():
    global circle
    return circle

def placeCircle():
    circle = pygame.transform.scale(getCircle(), (int(getCircle().get_width() * 1.3), int(getCircle().get_height() * 1.3)))
    pygame.display.get_surface().blit(circle, (400, 300))
    pygame.display.flip()

def placeText():
    text = pygame.font.Font(None, 54).render('Score: ' + str(saveData.loadData()['score']), True, (255, 255, 255))
    text_rect = text.get_rect(center=(35, 35))
    pygame.display.get_surface().blit(text, (35, 35))
    pygame.display.flip()

def updatePart():
    pygame.display.get_surface().fill((0, 0, 0))
    placeBG()
    placeText()
    placeCircle()
    playSound()

def playSound():
    sound = pygame.mixer.Sound('sounds/clicker.wav')
    sound.play()
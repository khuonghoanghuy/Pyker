import pygame
import saveData

def placeCircle():
    circle = pygame.image.load('images/circle.png')
    circle = pygame.transform.scale(circle, (int(circle.get_width() * 1.3), int(circle.get_height() * 1.3)))
    pygame.display.get_surface().blit(circle, (400, 300))
    pygame.display.flip()

def placeText():
    text = pygame.font.Font(None, 54).render('Score: ' + str(saveData.loadData()['score']), True, (255, 255, 255))
    text_rect = text.get_rect(center=(35, 35))
    pygame.display.get_surface().blit(text, (35, 35))
    pygame.display.flip()

def updatePart():
    pygame.display.get_surface().fill((0, 0, 0))
    placeText()
    placeCircle()
    playSound()

def playSound():
    sound = pygame.mixer.Sound('sounds/clicker.wav')
    sound.play()
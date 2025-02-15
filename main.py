import pygame
import saveData
import gameplay
import engine

saveData.loadData()

pygame.init()
pygame.display.set_mode((640, 480))
pygame.display.set_caption("PyKer Game")

gameplay.placeBG()
gameplay.placeCircle()
gameplay.placeText()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if engine.isMouseOverlaps(400, 300, gameplay.getCircle().get_width(), gameplay.getCircle().get_height(), event.pos):
                    saveData.saveData({
                        'score': saveData.loadData()['score'] + 1
                    })
                    gameplay.updatePart()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                saveData.resetData()
                gameplay.updatePart()
            if event.key == pygame.K_SPACE:
                saveData.saveData({
                    'score': saveData.loadData()['score'] + 1
                })
                gameplay.updatePart()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
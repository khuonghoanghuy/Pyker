import pygame
import saveData

saveData.loadData()

pygame.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyKer Game")

text = pygame.font.Font(None, 54).render('Score: ' + str(saveData.loadData()['score']), True, (255, 255, 255))
text_rect = text.get_rect(center=(35, 35))
pygame.display.get_surface().blit(text, (35, 35))
pygame.display.flip()

circle = pygame.image.load('images/circle.png')
circle = pygame.transform.scale(circle, (int(circle.get_width() * 1.1), int(circle.get_height() * 1.1)))
pygame.display.get_surface().blit(circle, (400, 300))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                saveData.saveData({
                    'score': saveData.loadData()['score'] + 1
                })
                pygame.display.get_surface().fill((0, 0, 0)) 
                text = pygame.font.Font(None, 54).render('Score: ' + str(saveData.loadData()['score']), True, (255, 255, 255))
                text_rect = text.get_rect(center=(35, 35))
                pygame.display.get_surface().blit(text, (35, 35))
                pygame.display.flip()

                circle = pygame.image.load('images/circle.png')
                circle = pygame.transform.scale(circle, (int(circle.get_width() * 1.1), int(circle.get_height() * 1.1)))
                pygame.display.get_surface().blit(circle, (400, 300))
                pygame.display.flip()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                saveData.resetData()
                pygame.display.get_surface().fill((0, 0, 0))
                text = pygame.font.Font(None, 54).render('Score: ' + str(saveData.loadData()['score']), True, (255, 255, 255))
                text_rect = text.get_rect(center=(35, 35))
                pygame.display.get_surface().blit(text, (35, 35))
                pygame.display.flip()

                circle = pygame.image.load('images/circle.png')
                circle = pygame.transform.scale(circle, (int(circle.get_width() * 1.1), int(circle.get_height() * 1.1)))
                pygame.display.get_surface().blit(circle, (400, 300))
                pygame.display.flip()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
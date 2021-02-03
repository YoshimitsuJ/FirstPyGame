import pygame

pygame.init()

width = 800
height = 900

frameColor = (255, 255, 255)#
lineColor = frameColor
columnCount = 7

player_pos = [352, 800]
player_size = 98
player_Color = (255, 0, 0)

screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:

        x = player_pos[0]
        y = player_pos[1]

        if event.key == pygame.K_RIGHT:
            x += player_size + 8
        elif event.key == pygame.K_LEFT:
            x -= player_size - 8

        if event.key == pygame.K_UP:
            y -= player_size

        player_pos = [x, y]


    screen.fill((0,0,0))
    pygame.draw.rect(screen, player_Color, (player_pos[0], player_pos[1], player_size, player_size))
   
    dWidth = width - 40
    dHeight = height - 140
    frameX = 20
    frameY = 20
    frameWidth = 10
    pygame.draw.rect(screen, frameColor, (frameX, frameY, dWidth, dHeight), frameWidth)

    margin = dWidth / columnCount

    for i in range(columnCount):

        x = frameX + (margin * i)

        pygame.draw.line(screen, lineColor, (x, 20),(x, dHeight), 4)
   
    pygame.display.update()

    # player_pos[1] >= 0 and player_pos[1] < height
    #      player_pos[1] -= 20
    #    else:
    #      player_pos[1] = 0
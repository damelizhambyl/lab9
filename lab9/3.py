import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("paint")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK

screen.fill(WHITE)


brush_size = 5
drawing = False
last_pos = None
mode = "brush" 
start_pos = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_t:
                mode = "brush"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_q:
                mode = "square"
            elif event.key == pygame.K_p:
                mode = "right_triangle"
            elif event.key == pygame.K_e:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_d:
                mode = "rhombus"
            elif event.key == pygame.K_l:
                mode = "rect"

       
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos

            if mode == "rect":
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                   abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
                pygame.draw.rect(screen, current_color, rect, width=2)

            elif mode == "circle":
                radius = int(((start_pos[0] - end_pos[0])**2 + (start_pos[1] - end_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, width=2)

            elif mode == "square":
                side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                pygame.draw.rect(screen, current_color, rect, width=2)

            elif mode == "right_triangle":
                
                x1, y1 = start_pos
                x2, y2 = end_pos
                points = [start_pos, (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, current_color, points, width=2)

            elif mode == "equilateral_triangle":
                
                x1, y1 = start_pos
                x2, y2 = end_pos
                side = max(abs(x2 - x1), abs(y2 - y1))
                point1 = (x1, y1)
                point2 = (x1 + side, y1)
                point3 = (x1 + side / 2, y1 - (3**0.5/2)*side)
                pygame.draw.polygon(screen, current_color, [point1, point2, point3], width=2)

            elif mode == "rhombus":
                
                x1, y1 = start_pos
                x2, y2 = end_pos
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                points = [
                    (center_x, center_y - dy),
                    (center_x + dx, center_y),
                    (center_x, center_y + dy),
                    (center_x - dx, center_y)
                ]
                pygame.draw.polygon(screen, current_color, points, width=2)

            drawing = False


        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 2)
                last_pos = event.pos

    pygame.display.update()
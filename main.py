import pygame

screen = pygame.display.set_mode((800, 800))
width, height = pygame.display.get_window_size()

# 0 is right, 1 is down, 2 is left, 3 is up
instructions = [1, 0]
size = 5
instruction_draw = {
    0: [size, 0],
    1: [0, size],
    2: [-size, 0],
    3: [0, -size]}
temp = instructions

for iteration in range(11):
    temp = [a for a in instructions]
    instructions.reverse()
    for instruction in instructions:
        temp.append((instruction - 1) % 4)
    instructions = [a for a in temp]

x, y = width / 2, height / 8 * 5
xavg, yavg = 0, 0
for instruction in instructions:
    move = instruction_draw[instruction]
    pygame.draw.line(screen, [255] * 3, (x, y), (x + move[0], y + move[1]))
    x += move[0]
    y += move[1]

while True:
    pygame.display.flip()
    pass
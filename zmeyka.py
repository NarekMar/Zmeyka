# ----------------------- GAME ----------------------------
import os
import random
x = random.randint(0, 19)
y = random.randint(0, 19)
random_apple_x = random.randint(0, 19)
random_apple_y = random.randint(0, 19)
point = 0
while True:
    print(point)
    step = input('W/A/S/D:  ').upper()
    os.system('cls')
    if step == 'W':
        x -= 1
    elif step == 'S':
        x += 1
    elif step == 'A':
        y -= 1
    elif step == 'D':
        y += 1
    if x >= 20 or x < 0 or y >= 20 or y < 0:
        print('Game Over :(!!!')
        break
    if x == random_apple_x and y == random_apple_y:
        random_apple_x = random.randint(0, 19)
        random_apple_y = random.randint(0, 19)
        point += 1
    for i in range(20):
        for j in range(20):
            if i == x and j == y:
                print(':😀:', end='')
            elif i == random_apple_x and j == random_apple_y:
                print(':🍔:', end='')
            else:
                print('.', end=' ')
        print()
# ---------------------------------------------------------------
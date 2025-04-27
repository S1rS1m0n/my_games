from math import sqrt
import turtle


s = turtle.Screen()
s.title('Tic-Tac-Toe')
t = turtle.Turtle()  # It is the designer

# Game state: centers[0] stores Player 1's occupied positions (circles),
# centers[1] stores Player 2's occupied positions (crosses)
centers = [[], []]
grid_centers = {
    1: [-350, 200], 2: [-150, 200], 3: [50, 200], 4: [-350, 0], 5: [-150, 0],
    6: [50, 0], 7: [-350, -200], 8: [-150, -200], 9: [50, -200],
    }

def draw_line(x, y, angle, length=600):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)

def draw_grid():
    draw_line(-250, 300, -90)
    draw_line(-50, 300, -90)
    draw_line(-450, 100, 0)
    draw_line(-450, -100, 0)

def draw_circle():
    s.onclick(None)  # Disable click while the designer is drawing
    t.pencolor('blue')
    t.setheading(-90)
    t.forward(75)
    t.setheading(0)
    t.pendown()
    t.circle(75)
    s.onclick(click)  # Reactivate click as soon as the drawing finishes

def draw_cross():
    s.onclick(None)
    t.pencolor('red')
    t.setheading(-45)
    t.backward(sqrt(2) * 75)
    t.pendown()
    t.forward(sqrt(2) * 150)
    t.penup()
    t.setheading(90)
    t.forward(150)
    t.setheading(225)
    t.pendown()
    t.forward(sqrt(2) * 150)
    s.onclick(click)

def make_move(x, y, center):
    if -450 < x < 150 and -300 < y < 300:  # Click inside the grid
        x_min, x_max = center[0] - 100, center[0] + 100
        y_min, y_max = center[1] - 100, center[1] + 100
        occupied_centers = centers[0] + centers[1]
        if center not in occupied_centers and x_min < x < x_max and \
        y_min < y < y_max:
            t.penup()
            t.goto(center[0], center[1])
            if len(centers[0]) == len(centers[1]):
                draw_circle()
                centers[0].append(center)
            elif len(centers[0]) > len(centers[1]):
                draw_cross()
                centers[1].append(center)

def check_win():
    win_combos = (
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7],  # Diagonals
    )
    for n in range(2):
        for m in range(8):
            win_centers = [grid_centers[win_combos[m][i]] for i in range(3)]
            if all(center in centers[n] for center in win_centers):
                if m in (0, 1, 2):
                    draw_line(win_centers[0][0] - 100, win_centers[0][1], 0)
                elif m in (3, 4, 5):
                    draw_line(win_centers[0][0], win_centers[0][1] + 100, -90)
                elif m in (6, 7):
                    x_increments = (-100, 100)
                    angles = (-45, 225)
                    draw_line(
                        win_centers[0][0] + x_increments[m - 6],
                        win_centers[0][1] + 100, angles[m - 6], sqrt(2) * 600
                        )
                return True
    return False

def check_draw():
    return len(centers[0]) + len(centers[1]) == 9

def print_results():
    win = check_win()
    draw = check_draw()
    if win or draw:
        t.penup()
        t.setheading(0)
        t.goto(170, 0)
        if len(centers[0]) > len(centers[1]) and not draw:
            t.write('PLAYER 1 WINS!', font = ('Arial', 25))
        elif len(centers[0]) == len(centers[1]):
            t.write('PLAYER 2 WINS!', font = ('Arial', 25))
        if draw:
            t.pencolor('black')
            t.write('THE GAME ENDED\nIN A DRAW', font = ('Arial', 25))
        s.onclick(None)  # Disable click when the game ends

def click(x, y):
    '''Play clicking inside the grid until the game ends.'''
    for center in grid_centers.values():
        make_move(x, y, center)
    if len(centers[0]) + len(centers[1]) > 4:
        print_results()

draw_grid()
s.onclick(click)
turtle.done()
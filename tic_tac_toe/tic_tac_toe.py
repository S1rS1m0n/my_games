from math import sqrt
import turtle


s = turtle.Screen()
s.title('Tic-Tac-Toe')
t = turtle.Turtle()

# Game state: centers[0] stores Player 1's occupied positions (circles),
# centers[1] stores Player 2's occupied positions (crosses)
centers = [[], []]
grid_centers = {
    1: [-350, 200], 2: [-150, 200], 3: [50, 200], 4: [-350, 0], 5: [-150, 0],
    6: [50, 0], 7: [-350, -200], 8: [-150, -200], 9: [50, -200],
    }

def draw_line(x, y, angle, length=600):
    '''Draw a line with a certain orientation and length starting from (x, y)
    position.'''
    disable_input()
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    react_input()

def draw_grid():
    '''Draw the 3x3 game grid.'''
    draw_line(-250, 300, -90)
    draw_line(-50, 300, -90)
    draw_line(-450, 100, 0)
    draw_line(-450, -100, 0)

def draw_circle(x, y):
    '''Draw a circle centered at (x, y) position.'''
    disable_input()
    t.penup()
    t.goto(x, y)
    t.pencolor('blue')
    t.setheading(-90)
    t.forward(75)
    t.setheading(0)
    t.pendown()
    t.circle(75)
    react_input()

def draw_cross(x, y):
    '''Draw a cross centered at (x, y) position.'''
    disable_input()
    t.penup()
    t.goto(x, y)
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
    react_input()

def make_move(x, y, center):
    '''Draw a circle or a cross when you click inside the grid.'''
    if -450 < x < 150 and -300 < y < 300:  # Click within the grid boundaries
        x_min, x_max = center[0] - 100, center[0] + 100
        y_min, y_max = center[1] - 100, center[1] + 100
        occ_centers = centers[0] + centers[1]
        if center not in occ_centers and x_min < x < x_max and \
        y_min < y < y_max:
            if len(centers[0]) == len(centers[1]):
                draw_circle(center[0], center[1])
                centers[0].append(center)
            elif len(centers[0]) > len(centers[1]):
                draw_cross(center[0], center[1])
                centers[1].append(center)

def check_win():
    '''Draw a green line to highlight a winning position.'''
    win_combos = (
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7],  # Diagonals
    )
    for n in range(2):  # centers index
        for m in range(8):  # win_combos index
            win_centers = [grid_centers[win_combos[m][i]] for i in range(3)]
            if all(center in centers[n] for center in win_centers):
                t.pencolor('green')
                t.width(5)
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

def print_results():
    '''Display a message at the end depending on how the game ends.'''
    win = check_win()
    draw = bool(len(centers[0]) + len(centers[1]) == 9 and not win)
    if win or draw:
        disable_input()  # To print the results correctly
        t.penup()
        t.setheading(0)
        t.goto(170, 0)
        if len(centers[0]) > len(centers[1]) and win:
            t.write('PLAYER 1 WINS!', font = ('Arial', 25))
        elif len(centers[0]) == len(centers[1]):
            t.write('PLAYER 2 WINS!', font = ('Arial', 25))
        if draw:
            t.pencolor('black')
            t.write('THE GAME ENDS\nIN A DRAW', font = ('Arial', 25))
        # Reactivate the restart button after printing the results
        s.onkey(restart, 'space')
        s.listen()

def click(x, y):
    '''Play clicking inside the grid until the game ends.'''
    for center in grid_centers.values():
        make_move(x, y, center)
    if len(centers[0]) + len(centers[1]) > 4:
        print_results()

def restart():
    '''Press the space bar to clear the screen and restart the game.'''
    t.clear()
    t.pencolor('black')
    t.width(1)
    draw_grid()
    # Reset the game state
    centers[0].clear()
    centers[1].clear()

def disable_input():
    '''Temporarily disable click and press to avoid wrong drawings.'''
    s.onclick(None)
    s.onkey(None, 'space')

def react_input():
    '''Reactivate click and press.'''
    s.onclick(click)
    s.onkey(restart, 'space')
    s.listen()

draw_grid()
s.onclick(click)
s.onkey(restart, 'space')
s.listen()

turtle.done()
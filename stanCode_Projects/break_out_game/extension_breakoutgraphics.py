"""
File: extension_breakoutgraphics.py
Name: Shih Hsuan Lin
-----------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This file contains a class named BreakoutGraphics.
This class creates all the graphics needed for the game of Breakout.
Additional, it animates the paddle and defines the ball's velocity.

extension:
1. Add score board and number of lives
2. Add text prompts when the game ends
3. The speed of the ball increases as the score gets higher
4. The red brick is a hard type of brick that has a 50% chance of being removed. Removing it earns 2 scores.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.move_ball)
        onmousemoved(self.move_paddle)
        # Draw bricks
        self.brick_spacing = BRICK_SPACING
        self.brick_height = BRICK_HEIGHT
        self.num_bricks = brick_cols*brick_rows
        self.brick_offset = BRICK_OFFSET
        for y in range(BRICK_ROWS):
            for x in range(BRICK_COLS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=(BRICK_WIDTH+BRICK_SPACING)*x, y=BRICK_OFFSET+(BRICK_HEIGHT+BRICK_SPACING)*y)
                brick.filled = True
                if y < 2:
                    brick.fill_color = brick.color = 'red'
                elif y < 4:
                    brick.fill_color = brick.color = 'orange'
                elif y < 6:
                    brick.fill_color = brick.color = 'yellow'
                elif y < 8:
                    brick.fill_color = brick.color = 'green'
                else:
                    brick.fill_color = brick.color = 'blue'
                self.window.add(brick)

        # Add scoreboard
        self.score = 0
        self.scoreboard = GLabel('Score: '+str(self.score), x=0, y=window_height)
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard)

        # Add number of lives
        self.num_lives = GLabel('Lives: ', x=window_width-85, y=window_height)
        self.num_lives.font = '-20'
        self.window.add(self.num_lives)

    def move_ball(self, mouse):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx *= -1

    def move_paddle(self, mouse):
        if 0 <= mouse.x-self.paddle.width/2 and mouse.x+self.paddle.width/2 <= self.window.width:
            self.paddle.x = mouse.x-self.paddle.width/2

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_ball(self):
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.width)/2
        self.__dx = 0
        self.__dy = 0

    def you_win(self):
        you_win = GLabel('You win!!\nYour score: '+str(self.score), x=self.window.width/2-82.5, y=self.window.height/2+27.5)
        you_win.font = '-20'
        self.window.add(you_win)

    def you_lose(self):
        you_lose = GLabel('You lose : (\nYour score: '+str(self.score), x=self.window.width/2-82.5, y=self.window.height/2+27.5)
        you_lose.font = '-20'
        self.window.add(you_lose)

    @staticmethod
    def check_red_brick_removed():
        if random.randint(0, 1) == 0:
            return False
        return True

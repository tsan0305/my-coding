"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
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
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle_offset = paddle_offset
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-self.paddle_offset))

        # Center a filled ball in the graphical window
        self.r = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        # self.ball.x = 2
        # self.ball.y = 2

        self.window.add(self.ball)

        self.ball2 = GOval(ball_radius*2, ball_radius*2)
        self.ball2.filled = True
        self.ball2.fill_color = 'blue'
        self.ball2.x = (self.window.width-self.ball.width)/2
        self.ball2.y = (self.window.height-self.ball.height)/2

        # Default initial velocity for the ball
        self.set_ball_velocity()
        # self.max_x_speed = MAX_X_SPEED
        # self.min_y_speed = INITIAL_Y_SPEED
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        onmouseclicked(self.ball_switch)
        onmousemoved(self.paddle_move)

        self.a = False

        # start_label
        self.start_label = GLabel('START')
        self.start_label.font = '-20'
        self.window.add(self.start_label, x=185, y=390)

        # game_over_label
        self.lose_label = GLabel('GAME OVER')
        self.lose_label.color = 'red'
        self.lose_label.font = '-20'

        # victory_label
        self.win_label = GLabel('VICTORY')
        self.win_label.color = 'red'
        self.win_label.font = '-20'

        # re_start_label
        self.re_start = GLabel('RESTART')
        self.re_start.color = 'blue'
        self.re_start.font = '-20'

        # Draw bricks
        self.b_r = brick_rows
        self.b_c = brick_cols
        self.b_w = brick_width
        self.b_h = brick_height
        self.b_o = brick_offset
        self.b_s = brick_spacing
        self.bricks()  # create bricks

    def paddle_move(self, event):
        self.paddle.x = event.x-self.paddle.width/2
        # self.paddle.y = self.window.height-self.paddle_offset
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x+self.paddle.width > self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    '''control the mouse clicked
        if mouse clicks the start label or the restart label'''
    def ball_switch(self, mouse):
        if self.window.get_object_at(mouse.x, mouse.y) == self.start_label:
            self.window.remove(self.start_label)
            self.a = True
        if self.window.get_object_at(mouse.x, mouse.y) == self.re_start:
            self.window.remove(self.re_start)
            self.window.remove(self.lose_label)
            self.a = True

    # set the initial velocity of the ball
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        while self.__dx == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # let user get dx variable
    def get_dx(self):
        self.set_ball_velocity()
        return self.__dx

    # let user get dy variable
    def get_dy(self):
        return self.__dy

    # create bricks (10X10)
    def bricks(self):
        for i in range(self.b_r):
            for j in range(self.b_c):
                brick = GRect(self.b_w, self.b_h)
                brick.filled = True
                if i <= 1:
                    brick.fill_color = 'red'
                elif 1 < i <= 3:
                    brick.fill_color = 'orange'
                elif 3 < i <= 5:
                    brick.fill_color = 'yellow'
                elif 5 < i <= 7:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                brick_x = j*(self.b_w+self.b_s)
                brick_y = self.b_o + i*(self.b_h+self.b_s)
                self.window.add(brick, x=brick_x, y=brick_y)


    # def score_label(self, scores):
    #     score_label = GLabel('Score==>' + str(scores))
    #     score_label.font = '-20'
    #     self.window.add(score_label, x=0, y=630)

    # def check_for_collisions(self):
    #     if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
    #         if self.window.get_object_at(self.ball.x, self.ball.y) == self.paddle:
    #             self.__dx = -self.get_dx()
    #             self.__dy = -self.__dy
    #         else:
    #             self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
    #             self.__dx = -self.get_dx()
    #             self.__dy = -self.__dy
    #     elif self.window.get_object_at(self.ball.x, self.ball.y + 2*self.r) is not None:
    #         if self.window.get_object_at(self.ball.x, self.ball.y) == self.paddle:
    #             self.__dx = -self.get_dx()
    #             self.__dy = -self.__dy
    #         else:
    #             self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
    #             self.__dx = -self.get_dx()
    #             self.__dy = -self.__dy










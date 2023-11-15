"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3	        # Number of attempts


# b_num = 0




def main():
    lives = NUM_LIVES
    b_num = 0
    graphics = BreakoutGraphics()

    # create score label
    score_label = GLabel('Score==>' + str(b_num))
    score_label.font = '-20'
    graphics.window.add(score_label, x=10, y=630)

    # create lives label
    lives_label = GLabel('Lives==>' + str(lives))
    lives_label.font = '-20'
    graphics.window.add(lives_label, x=300, y=630)

    ball_dx = graphics.get_dx()
    ball_dy = graphics.get_dy()
    while True:
        if graphics.a:
            # already win the game or lose the game
            if b_num == 100 or lives == 0:
                graphics.window.clear()
                graphics.bricks()
                graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width)/2,
                                    y=(graphics.window.height-graphics.ball.height)/2)
                graphics.window.add(graphics.paddle)
                b_num = 0
                lives = 3
                graphics.window.add(score_label, x=10, y=630)
                graphics.window.add(lives_label, x=300, y=630)
                lives_label.text = 'lives==>' + str(lives)
            if lives > 0:
                while True:
                    graphics.ball.move(ball_dx, ball_dy)
                    # graphics.ball2.move(ball_dx, ball_dy)
                    ball_top_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                    ball_top_right = graphics.window.get_object_at(graphics.ball.x + 2*graphics.r, graphics.ball.y)
                    ball_bottom_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2*graphics.r)
                    ball_bottom_right = graphics.window.get_object_at(graphics.ball.x+2*graphics.r, graphics.ball.y+2*graphics.r)

                    # ball_top_left
                    if ball_top_left is not None:
                        if ball_top_left == graphics.paddle:
                            ball_dy = -ball_dy
                            # graphics.ball.move(ball_dx, ball_dy)
                        else:
                            if ball_top_left != score_label and ball_top_left != lives_label:
                                graphics.window.remove(ball_top_left)
                                ball_dy = -ball_dy
                                b_num += 1
                    # ball_top_right
                    elif ball_top_right is not None:
                        if ball_top_right == graphics.paddle:
                            ball_dy = -ball_dy
                            # graphics.ball.move(ball_dx, ball_dy)
                        else:
                            if ball_top_right != score_label and ball_top_right != lives_label:
                                graphics.window.remove(ball_top_right)
                                ball_dy = -ball_dy
                                b_num += 1
                    # ball_bottom_left
                    elif ball_bottom_left is not None:
                        if ball_bottom_left == graphics.paddle:
                            ball_dy = -ball_dy
                            # graphics.ball.move(ball_dx, ball_dy)
                        else:
                            if ball_bottom_left != score_label and ball_bottom_left != lives_label:
                                graphics.window.remove(ball_bottom_left)
                                ball_dy = -ball_dy
                                b_num += 1
                    # ball_bottom_right
                    elif ball_bottom_right is not None:
                        if ball_bottom_right == graphics.paddle:
                            ball_dy = -ball_dy
                            # graphics.ball.move(ball_dx, ball_dy)
                        else:
                            if ball_bottom_right != score_label and ball_bottom_right != lives_label:
                                graphics.window.remove(ball_bottom_right)
                                ball_dy = -ball_dy
                                b_num += 1
                    # score_label
                    score_label.text = 'Score==>' + str(b_num)
                    # ball_x_bounding
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        ball_dx = -ball_dx
                    # ball_y_bounding
                    if graphics.ball.y <= 0:
                        ball_dy = -ball_dy
                    # the ball touch the bottom, the game loses one life
                    if graphics.ball.y > graphics.window.height:
                        lives -= 1
                        graphics.a = False
                        lives_label.text = 'lives==>' + str(lives)
                        graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width)/2, y=(graphics.window.height-graphics.ball.height)/2)
                        # graphics.window.add(graphics.ball2, x=1, y=1)

                        if lives == 0:
                            graphics.window.add(graphics.lose_label, x=190, y=390)

                        break
                    # brick finish
                    if b_num == 100:
                        # graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                        #                     y=(graphics.window.height-graphics.ball.height)/2)
                        graphics.a = False
                        graphics.window.remove(graphics.ball)
                        break
                    pause(FRAME_RATE)
                if b_num == 100:
                    graphics.window.add(graphics.win_label, x=190, y=390)
                    graphics.window.add(graphics.re_start, x=190, y=430)
                elif lives > 0 and b_num < 100:
                    graphics.window.add(graphics.start_label)
                elif lives == 0:
                    graphics.window.add(graphics.re_start, x=190, y=430)

            # else:
            #     graphics.window.remove(graphics.start_label)


        pause(FRAME_RATE)

    # Add the animation loop here!

# def ball_bounding(ball):
#     if ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
#         ball_dx = -ball_dx
#     # ball_y_bounding
#     if graphics.ball.y <= 0:
#         ball_dy = -ball_dy


if __name__ == '__main__':
    main()

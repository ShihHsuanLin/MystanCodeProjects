"""
File: extension_breakout.py
Name: Shih Hsuan Lin
-----------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This file creates the animation for the ball in the Breakout game,
including its behavior when it collides the window boundaries, the paddle, and the bricks.
Finally, it defines the end-game conditions.

extension:
1. Add score board and number of lives
2. Add text prompts when the game ends
3. The speed of the ball increases as the score gets higher
4. The red brick is a hard type of brick that has a 50% chance of being removed. Removing it earns 2 scores.
"""

from campy.gui.events.timer import pause
from extension_breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
SPEED_INCREASE_MULTIPLE = 1.007  # The multiple by which the ball speed increases as the score gets higher


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    # Thanks to Cheryl for teaching me that initial conditions can be written on the same line
    dx = dy = 0
    num_lives = NUM_LIVES
    graphics.num_lives.text = 'Lives: '+str(num_lives)
    while True:
        # The switch to disconnect from the coder side
        if dy == 0:
            dx = graphics.get_dx()*SPEED_INCREASE_MULTIPLE**graphics.score
            dy = graphics.get_dy()*SPEED_INCREASE_MULTIPLE**graphics.score
        graphics.ball.move(dx, dy)
        # Determine if the ball has collided with the window boundary
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            dx *= -1
        if graphics.ball.y <= 0:
            dy *= -1
        # When the ball goes beyond the bottom boundary of the window, determine whether to reset the ball or terminate the game
        elif graphics.ball.y+graphics.ball.height >= graphics.window.height:
            num_lives -= 1
            graphics.num_lives.text = 'Lives: '+str(num_lives)
            if num_lives > 0:
                graphics.reset_ball()
                dx = dy = 0
            else:
                graphics.you_lose()
                break
        # Use a double for loop to check if the 4 vertices of the ball collide
        is_collision = False
        for y in (graphics.ball.y, graphics.ball.y+graphics.ball.height):
            for x in (graphics.ball.x, graphics.ball.x+graphics.ball.width):
                collided_object = graphics.window.get_object_at(x, y)
                # Determine if the ball has collided
                if collided_object is not None and collided_object is not graphics.scoreboard and collided_object is not graphics.num_lives:
                    is_collision = True
                    # The ball collides with the paddle
                    if collided_object is graphics.paddle:
                        if dy > 0:
                            dy *= -1
                    # The ball collides with the red brick
                    elif collided_object.y < graphics.brick_offset+(graphics.brick_height+graphics.brick_spacing)*2:
                        if BreakoutGraphics.check_red_brick_removed():
                            graphics.window.remove(collided_object)
                            graphics.num_bricks -= 1
                            graphics.score += 2
                            graphics.scoreboard.text = 'Score: ' + str(graphics.score)
                            # The speed of the ball increases as the score gets higher
                            dx *= SPEED_INCREASE_MULTIPLE**2
                            dy *= -SPEED_INCREASE_MULTIPLE**2
                        else:
                            dy *= -1
                    # The ball collides with any brick except for the red one
                    else:
                        graphics.window.remove(collided_object)
                        graphics.num_bricks -= 1
                        graphics.score += 1
                        graphics.scoreboard.text = 'Score: '+str(graphics.score)
                        # The speed of the ball increases as the score gets higher
                        dx *= SPEED_INCREASE_MULTIPLE
                        dy *= -SPEED_INCREASE_MULTIPLE
                    # The game ends when all bricks are destroyed
                    if graphics.num_bricks == 0:
                        graphics.you_win()
                        return None
                    break
            if is_collision:
                break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

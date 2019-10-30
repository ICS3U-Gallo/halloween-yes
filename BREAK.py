import arcade
import os

WIDTH = 640
HEIGHT = 480
current_screen = "menu"
score = 0


def setup():
    global x1, y1, y2
    x1 = 0
    y1 = 425
    y2 = 240
    arcade.open_window(WIDTH, HEIGHT, "Halloween Program")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global x1, y1, score, current_screen
    x1 += 4
    if x1 >= 640:
        x1 = -300
    if score == 4:
        current_screen = "escaped"
        score = 0

def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        draw_menu()
    if current_screen == "start":
        draw_start()
    if current_screen == "room_one":
        draw_room_one()
    if current_screen == "room_one_right":
        draw_room_one_right()
    if current_screen == "room_one_left":
        draw_room_one_left()
    if current_screen == "d1_rm1":
        draw_d1_rm1()
    if current_screen == "b1_rm1":
        draw_b1_rm1()
    if current_screen == "d1_rm1l":
        draw_d1_rm1l()
    if current_screen == "c1_rm1r":
        draw_c1_rm1r()
    if current_screen == "escaped":
        draw_escaped()

def draw_menu():
    arcade.draw_text("BREAK", 292.5, 240, arcade.color.WHITE, font_size=20)
    arcade.draw_text("Escape Or Be Spooked", 260, 220, arcade.color.WHITE)
    arcade.draw_text("Press Enter To Begin", 265, 200, arcade.color.WHITE)
    arcade.draw_text("I For Instructions", 10, 455, arcade.color.WHITE)

def draw_escaped():
    arcade.draw_text("YOU'VE ESCAPED", x1, y2, arcade.color.GREEN, font_size=20)
    arcade.draw_text("Press ESC To Return To Menu", 10, 455, arcade.color.WHITE)

def draw_start():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_rectangle_outline(320, 240, 180, 300, arcade.color.WHITE)
    arcade.draw_line(230, 380, 410, 380, arcade.color.WHITE)
    arcade.draw_line(230, 120, 410, 120, arcade.color.WHITE)
    arcade.draw_circle_outline(320, 105, 8, arcade.color.WHITE)
    arcade.draw_text("EMERGENCY ALERT", x1, y1, arcade.color.WHITE, font_size=20)
    arcade.draw_text("Unknown Number", 275, 362, arcade.color.GREEN, font_size=9)
    arcade.draw_text("You've been assigned a mission...", 235, 338, arcade.color.GREEN, font_size=9)
    arcade.draw_text("It has been discovered that", 235, 326, arcade.color.GREEN, font_size=9)
    arcade.draw_text("Casa Loma has been taken over", 235, 314, arcade.color.GREEN, font_size=9)
    arcade.draw_text("by an arsenal of ancient spirits.", 235, 302, arcade.color.GREEN, font_size=9)
    arcade.draw_text("It is your job to rescue the people", 235, 290, arcade.color.GREEN, font_size=9)
    arcade.draw_text("trapped in each room of the castle.", 235, 278, arcade.color.GREEN, font_size=9)
    arcade.draw_text("There are 4 keys in each room,", 235, 266, arcade.color.GREEN, font_size=9)
    arcade.draw_text("All keys need to be collected in", 235, 254, arcade.color.GREEN, font_size=9)
    arcade.draw_text("order to break from the spirits.", 235, 242, arcade.color.GREEN, font_size=9)
    arcade.draw_text("Do you accept this mission (y/n)?", 235, 230, arcade.color.GREEN, font_size=9)

def draw_score_page():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("ROOM ONE LEFT FACING", x1, y1, arcade.color.WHITE, font_size=20)


def draw_room_one():
    # Background Color
    arcade.set_background_color(arcade.color.BLACK)
    # Score
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    # Interaction Message
    arcade.draw_text("Press Idicated Key To Interact", 10, 455, arcade.color.GREEN)
    # Room Name
    arcade.draw_text("Night Vision Room", 10, 435, arcade.color.GREEN)
    # Wardrobe
    arcade.draw_rectangle_outline(100, 160, 180, 300, arcade.color.GREEN)
    arcade.draw_circle_outline(160, 145, 8, arcade.color.GREEN)
    arcade.draw_text("W", 16, 290, arcade.color.GREEN)
    # Shelf
    arcade.draw_rectangle_outline(300, 75, 200, 130, arcade.color.GREEN)
    arcade.draw_rectangle_outline(300, 75, 200, 130, arcade.color.GREEN)
    arcade.draw_line(200, 75, 400, 75, arcade.color.GREEN)
    arcade.draw_circle_outline(300, 52, 8, arcade.color.GREEN)
    arcade.draw_circle_outline(300, 120, 8, arcade.color.GREEN)
    arcade.draw_rectangle_filled(500, 100, 100, 180, arcade.color.BLACK)
    # Box
    arcade.draw_rectangle_outline(480, 201, 40, 18, arcade.color.GREEN)
    arcade.draw_line(460, 206, 500, 206, arcade.color.GREEN)
    arcade.draw_circle_outline(480, 200, 2, arcade.color.GREEN)
    arcade.draw_text("B", 440, 200, arcade.color.GREEN)
    # Box - 3D
    arcade.draw_line(200, 140, 210, 158, arcade.color.GREEN)
    arcade.draw_line(400, 140, 410, 158, arcade.color.GREEN)
    arcade.draw_line(210, 158, 410, 158, arcade.color.GREEN)
    arcade.draw_line(410, 158, 410, 28, arcade.color.GREEN)
    arcade.draw_line(410, 28, 400, 10, arcade.color.GREEN)

    # Bookshelf
    arcade.draw_rectangle_outline(500, 100, 100, 180, arcade.color.GREEN)
    arcade.draw_line(450, 54, 550, 54, arcade.color.GREEN)
    arcade.draw_line(450, 100, 550, 100, arcade.color.GREEN)
    arcade.draw_line(450, 144, 550, 144, arcade.color.GREEN)
    # Bookshelf - 3D
    arcade.draw_line(450, 190, 460, 208, arcade.color.GREEN)
    arcade.draw_line(550, 190, 560, 208, arcade.color.GREEN)
    arcade.draw_line(512, 208, 500, 208, arcade.color.GREEN)
    arcade.draw_line(528, 208, 560, 208, arcade.color.GREEN)
    arcade.draw_line(560, 208, 560, 28, arcade.color.GREEN)
    # REFRENCE 3D TRANSLATION
    # RIGHT 10 UP 18
    arcade.draw_line(560, 28, 550, 10, arcade.color.GREEN)
    # Books
    arcade.draw_rectangle_outline(455, 73, 5, 35, arcade.color.GREEN)
    arcade.draw_rectangle_outline(535, 68, 5, 25, arcade.color.GREEN)
    # Lamp
    arcade.draw_rectangle_outline(520, 220, 16, 60, arcade.color.GREEN)
    arcade.draw_triangle_filled(492, 250, 512, 275, 512, 250, arcade.color.GREEN)
    arcade.draw_triangle_filled(528, 275, 548, 250, 528, 250, arcade.color.GREEN)
    arcade.draw_rectangle_filled(520, 262, 16, 25, arcade.color.GREEN)

def draw_d1_rm1():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Wardrobe #1", 10, 455, arcade.color.GREEN)
    arcade.draw_text("Answer The Following Puzzle To Obtain A Key:", 10, 435, arcade.color.GREEN)
    arcade.draw_text("Press Escape To Leave Room", 10, 415, arcade.color.GREEN)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    arcade.draw_text("You measure my life in hours and I serve you by expiring.", 150, 280, arcade.color.GREEN)
    arcade.draw_text("I'm quick when I'm thin and slow when I'm fat.", 175, 260, arcade.color.GREEN)
    arcade.draw_text("The wind is my enemy. Obtain your key, what am I? ", 160, 240, arcade.color.GREEN)
    arcade.draw_text("A) Candle      B) Blanket      C) Mateo     D) BBQ", 175, 200, arcade.color.GREEN)


def draw_b1_rm1():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Box", 10, 455, arcade.color.GREEN)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    arcade.draw_text("I have no feet to dance, I have no eyes to see", 170, 280, arcade.color.GREEN)
    arcade.draw_text("I have no life to live or die, but yet", 205, 260, arcade.color.GREEN)
    arcade.draw_text("I do all three, what am I?", 235, 240, arcade.color.GREEN)
    arcade.draw_text("A) Ghost      B) Computer      C) Fire     D) BBQ", 167.5, 200, arcade.color.GREEN)


def draw_room_one_right():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_rectangle_filled(320, 450, 800, 300, arcade.color.GRAY)
    arcade.draw_rectangle_filled(320, 100, 100, 325, arcade.color.RED)
    arcade.draw_triangle_filled(370, 0, 500, 0, 370, 260, arcade.color.RED)
    arcade.draw_triangle_filled(270, 0, 140, 0, 270, 260, arcade.color.RED)
    arcade.draw_line(140, 0, 270, 260, arcade.color.YELLOW)
    arcade.draw_line(500, 0, 370, 260, arcade.color.YELLOW)
    # Throne
    arcade.draw_rectangle_filled(320, 315, 75, 126, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(280, 275, 20, 76, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(360, 275, 20, 76, arcade.color.YELLOW)
    arcade.draw_rectangle_filled(320, 315, 50, 100, arcade.color.RED)
    arcade.draw_triangle_filled(290, 265, 300, 265, 300, 325, arcade.color.RED)
    arcade.draw_triangle_filled(350, 265, 340, 265, 340, 325, arcade.color.RED)
    arcade.draw_line(270, 313, 290, 313, arcade.color.RED)
    arcade.draw_line(370, 313, 350, 313, arcade.color.RED)
    arcade.draw_triangle_filled(320, 400, 290, 378, 350, 378, arcade.color.YELLOW)
    arcade.draw_line(290, 290, 350, 290, arcade.color.YELLOW)
    # Crown
    arcade.draw_rectangle_filled(150, 250, 40, 10, arcade.color.YELLOW)
    arcade.draw_triangle_filled(150, 265, 140, 255, 160, 255, arcade.color.YELLOW)
    arcade.draw_triangle_filled(130, 265, 140, 255, 130, 255, arcade.color.YELLOW)
    arcade.draw_triangle_filled(170, 265, 170, 255, 160, 255, arcade.color.YELLOW)
    # Chest
    arcade.draw_rectangle_filled(580, 210, 20, 33, arcade.color.RED)
    arcade.draw_triangle_filled(580, 175, 590, 193, 580, 193, arcade.color.RED)
    arcade.draw_triangle_filled(480, 225, 490, 243, 490, 225, arcade.color.RED)
    arcade.draw_rectangle_filled(540, 233, 100, 20, arcade.color.RED)
    arcade.draw_rectangle_filled(530, 200, 100, 50, arcade.color.RED)
    arcade.draw_rectangle_outline(530, 200, 100, 50, arcade.color.GRAY)
    arcade.draw_rectangle_outline(530, 200, 99, 49, arcade.color.GRAY)
    arcade.draw_rectangle_outline(530, 200, 98, 48, arcade.color.GRAY)
    arcade.draw_line(480, 210, 580, 210, arcade.color.GRAY)
    arcade.draw_line(480, 209, 580, 209, arcade.color.GRAY)
    arcade.draw_line(480, 211, 580, 211, arcade.color.GRAY)
    arcade.draw_rectangle_filled(530, 210, 14, 8, arcade.color.GRAY)
    arcade.draw_line(480, 225, 490, 243, arcade.color.GRAY)
    arcade.draw_line(580, 225, 590, 243, arcade.color.GRAY)
    arcade.draw_line(590, 243, 490, 243, arcade.color.GRAY)
    arcade.draw_line(590, 243, 590, 193, arcade.color.GRAY)
    arcade.draw_line(580, 175, 590, 193, arcade.color.GRAY)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    arcade.draw_text("Throne Room - Lights On", 10, 455, arcade.color.GREEN)
    arcade.draw_text("Press Indicated Key To Interact", 10, 435, arcade.color.GREEN)
    arcade.draw_text("C", 470, 235, arcade.color.GREEN)

def draw_c1_rm1r():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    arcade.draw_text("Throne Room - Lights On", 10, 455, arcade.color.GREEN)
    arcade.draw_text("Press Indicated Key To Interact", 10, 435, arcade.color.GREEN)
    arcade.draw_text("If you see one flying around, you’d better be careful at", 160, 280, arcade.color.GREEN)
    arcade.draw_text("night, as some turn into vampires and will give your", 168, 260, arcade.color.GREEN)
    arcade.draw_text("neck a big bite. What are they?", 225, 240, arcade.color.GREEN)
    arcade.draw_text("A) Shaan      B) Bat     C) Witch     D) Yes", 200, 200, arcade.color.GREEN)

def draw_room_one_left():
    # Background Color
    arcade.set_background_color(arcade.color.BLACK)
    # Door
    arcade.draw_rectangle_outline(WIDTH / 2, HEIGHT / 2, 150, 300, arcade.color.GREEN)
    arcade.draw_rectangle_outline(WIDTH / 2, (HEIGHT / 2) - 5, 130, 290, arcade.color.GREEN)
    arcade.draw_circle_outline((WIDTH / 2) + 50, HEIGHT / 2, 5, arcade.color.GREEN)
    # Window 1
    arcade.draw_rectangle_outline(125, 300, 150, 150, arcade.color.GREEN)
    arcade.draw_rectangle_outline(125, 300, 160, 160, arcade.color.GREEN)
    arcade.draw_line(50, 300, 200, 300, arcade.color.GREEN)
    arcade.draw_line(125, 375, 125, 225, arcade.color.GREEN)
    # Window 2
    arcade.draw_rectangle_outline(WIDTH - 125, 300, 150, 150, arcade.color.GREEN)
    arcade.draw_rectangle_outline(WIDTH - 125, 300, 160, 160, arcade.color.GREEN)
    arcade.draw_line(WIDTH - 50, 300, WIDTH - 200, 300, arcade.color.GREEN)
    arcade.draw_line(WIDTH - 125, 375, WIDTH - 125, 225, arcade.color.GREEN)
    # Floor Line
    arcade.draw_line(0, 140, 245, 140, arcade.color.GREEN)
    arcade.draw_line(395, 140, 640, 140, arcade.color.GREEN)
    # Messages
    arcade.draw_text("Press Idicated Key To Interact", 10, 455, arcade.color.GREEN)
    arcade.draw_text("2nd Night Vision Room", 10, 435, arcade.color.GREEN)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    arcade.draw_text("D", 245, 400, arcade.color.GREEN)

def draw_d1_rm1l():
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    arcade.draw_text("Door -- Night Vision Room 2", 10, 455, arcade.color.GREEN)
    arcade.draw_text("The person who built it sold it. The person who bought it", 160, 280, arcade.color.GREEN)
    arcade.draw_text("never used it. The person who used it never saw it.", 175, 260, arcade.color.GREEN)
    arcade.draw_text("A) Yes      B) Skeleton      C) Coffin     D) BBQ", 195, 220, arcade.color.GREEN)

def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "menu":
        menu_keybinds(key, modifiers)
    if current_screen == "start":
        start_keybinds(key, modifiers)
    if current_screen == "room_one":
        room_one_keybinds(key, modifiers)
    if current_screen == "room_one_right":
        room_one_right_keybinds(key, modifiers)
    if current_screen == "room_one_left":
        room_one_left_keybinds(key, modifiers)
    if current_screen == "d1_rm1":
        d1_rm1_keybinds(key, modifiers)
    if current_screen == "b1_rm1":
        b1_rm1_keybinds(key, modifiers)
    if current_screen == "d1_rm1l":
        d1_rm1l_keybinds(key, modifiers)
    if current_screen == "c1_rm1r":
        c1_rm1r_keybinds(key, modifiers)

def menu_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "start"

def start_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "menu"
    if key == arcade.key.Y:
        current_screen = "room_one"
    if key == arcade.key.N:
        current_screen = "menu"

def room_one_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "start"
    if key == arcade.key.RIGHT:
        current_screen = "room_one_right"
    if key == arcade.key.LEFT:
        current_screen = "room_one_left"
    if key == arcade.key.W:
        current_screen = "d1_rm1"
    if key == arcade.key.B:
        current_screen = "b1_rm1"

def d1_rm1_keybinds(key, modifiers):
    global current_screen, score
    if key == arcade.key.ESCAPE:
        current_screen = "room_one"
    if key == arcade.key.A:
        score += 1
        current_screen = "room_one"
    else:
        pass

def b1_rm1_keybinds(key, modifiers):
    global current_screen, score
    if key == arcade.key.C:
        score += 1
        current_screen = "room_one"

def room_one_right_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.LEFT:
        current_screen = "room_one"
    if key == arcade.key.C:
        current_screen = "c1_rm1r"

def c1_rm1r_keybinds(key, modifiers):
    global current_screen, score
    if key == arcade.key.ESCAPE:
        current_screen = "room_one_right"
    if key == arcade.key.B:
        score += 1
        current_screen = "room_one_right"

def room_one_left_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.RIGHT:
        current_screen = "room_one"
    if key == arcade.key.D:
        current_screen = "d1_rm1l"

def d1_rm1l_keybinds(key, modifiers):
    global current_screen, score
    if key == arcade.key.ESCAPE:
        current_screen = "room_one_left"
    if key == arcade.key.C:
        score += 1
        current_screen = "room_one_left"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()

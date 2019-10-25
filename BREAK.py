import arcade
import os

WIDTH = 640
HEIGHT = 480

current_screen = "menu"
score = 0

def setup():
    global x1, y1
    x1 = 0
    y1 = 425
    arcade.open_window(WIDTH, HEIGHT, "Halloween Program")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)

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
        x1 = 0
    if score == 3:
        current_screen = "menu"
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

def draw_menu():
    arcade.draw_text("BREAK", 292.5, 240, arcade.color.WHITE, font_size=20)
    arcade.draw_text("Escape Or Be Spooked", 260, 220, arcade.color.WHITE)
    arcade.draw_text("Press Enter To Begin", 265, 200, arcade.color.WHITE)
    arcade.draw_text("I For Instructions", 10, 455, arcade.color.WHITE)

def draw_start():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_rectangle_outline(320, 240, 180, 300, arcade.color.WHITE)
    arcade.draw_line(230, 380, 410, 380, arcade.color.WHITE)
    arcade.draw_line(230, 120, 410, 120, arcade.color.WHITE)
    arcade.draw_circle_outline(320, 105, 8, arcade.color.WHITE)
    arcade.draw_text("EMERGENCY ALERT", x1, y1, arcade.color.WHITE, font_size=20)
    arcade.draw_text("Unknown Number", 275, 362, arcade.color.GREEN, font_size=9)
    arcade.draw_text("You've been assigned a mission...", 235, 338, arcade.color.GREEN, font_size = 9)
    arcade.draw_text("It has been discovered that", 235, 326, arcade.color.GREEN, font_size = 9)
    arcade.draw_text("Casa Loma has been taken over", 235, 314, arcade.color.GREEN, font_size = 9)
    arcade.draw_text("By an arsenal of ancient spirits.", 235, 302, arcade.color.GREEN, font_size=9)
    arcade.draw_text("It is your job to rescue the people", 235, 290, arcade.color.GREEN, font_size=9)
    arcade.draw_text("trapped in each room of the castle.", 235, 278, arcade.color.GREEN, font_size=9)
    arcade.draw_text("There are 3 keys in each room,", 235, 266, arcade.color.GREEN, font_size=9)
    arcade.draw_text("All keys need to be collected in", 235, 254, arcade.color.GREEN, font_size=9)
    arcade.draw_text("order to break from the spirits.", 235, 242, arcade.color.GREEN, font_size=9)
    arcade.draw_text("Do you accept this mission (y/n)?", 235, 230, arcade.color.GREEN, font_size=9)

def draw_room_one():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)
    arcade.draw_rectangle_outline(100, 160, 180, 300, arcade.color.WHITE)
    arcade.draw_circle_outline(160, 145, 8, arcade.color.WHITE)

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


def draw_room_one_right():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("ROOM ONE RIGHT FACING", x1, y1, arcade.color.WHITE, font_size=20)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)

def draw_room_one_left():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("ROOM ONE LEFT FACING", x1, y1, arcade.color.WHITE, font_size=20)
    arcade.draw_text(f"Keys: {score}", 585, 455, arcade.color.GREEN)

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

def d1_rm1_keybinds(key, modifiers):
    global current_screen, score
    if key == arcade.key.ESCAPE:
        current_screen = "room_one"
    if key == arcade.key.A:
        while score < 1:
            score += 1
    else:
        pass

def room_one_right_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.LEFT:
        current_screen = "room_one"

def room_one_left_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.RIGHT:
        current_screen = "room_one"

def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()

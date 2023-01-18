@namespace
class SpriteKind:
    snake_head_sprite = SpriteKind.create()
    snake_body_sprite = SpriteKind.create()
def move_right():
    move_last_body_sprite_towhere_head_was()
    snake_head.set_position(head_x_prior + s, head_y_prior)

def on_up_pressed():
    move_up()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def create_random_heart():
    global heart_sprite, x2, y2, heart
    for index in range(randint(1, 2)):
        if heart < 3:
            heart_sprite = sprites.create(heart_image, SpriteKind.food)
            x2 = randint(7, 160 - 7)
            y2 = randint(7, 120 - 7)
            heart_sprite.set_position(x2, y2)
            heart += 1

def on_up_repeated():
    move_up()
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def make_body_sprite(x: number, y: number):
    global body_sprite
    body_sprite = sprites.create(snake_body_image, SpriteKind.snake_body_sprite)
    body_sprite.set_position(x, y)
    snake_body_list.append(body_sprite)

def on_right_repeated():
    move_right()
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_left_pressed():
    move_left()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def create_snake_body():
    global snake_body_image, snake_body_list
    snake_body_image = image.create(s, s)
    snake_body_image.fill(9)
    snake_body_list = sprites.all_of_kind(SpriteKind.snake_body_sprite)
    for index2 in range(5):
        make_body_sprite(snake_head.x, snake_head.y + (index2 + 1) * s)
def move_last_body_sprite_towhere_head_was():
    global head_x_prior, head_y_prior
    head_x_prior = snake_head.x
    head_y_prior = snake_head.y
    snake_body_list[0] = snake_body_list.pop()
    snake_body_list[0].set_position(snake_head.x, snake_head.y)
def lengthen_snake_by_one_sprite():
    global body_last_sprite, body_next_to_last_sprite, dx, dy, x2, y2
    body_last_sprite = snake_body_list[len(snake_body_list) - 1]
    body_next_to_last_sprite = snake_body_list[len(snake_body_list) - 2]
    dx = body_next_to_last_sprite.x - body_last_sprite.x
    dy = body_next_to_last_sprite.y - body_last_sprite.y
    x2 = body_last_sprite.x + dx
    y2 = body_last_sprite.y + dy
    make_body_sprite(x2, y2)
def move_left():
    move_last_body_sprite_towhere_head_was()
    snake_head.set_position(head_x_prior - s, head_y_prior)

def on_right_pressed():
    move_right()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    global heart
    info.change_score_by(1)
    otherSprite.destroy(effects.spray, 500)
    heart += -1
    lengthen_snake_by_one_sprite()
    create_random_heart()
sprites.on_overlap(SpriteKind.snake_head_sprite, SpriteKind.food, on_on_overlap)

def move_down():
    move_last_body_sprite_towhere_head_was()
    snake_head.set_position(head_x_prior, head_y_prior + s)

def on_down_repeated():
    move_down()
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_down_pressed():
    move_down()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    game.over(False, effects.dissolve)
sprites.on_overlap(SpriteKind.snake_head_sprite,
    SpriteKind.snake_body_sprite,
    on_on_overlap2)

def create_snake_head():
    global snake_head_image, snake_head
    snake_head_image = image.create(s, s)
    snake_head_image.fill(4)
    snake_head = sprites.create(snake_head_image, SpriteKind.snake_head_sprite)
    snake_head.set_stay_in_screen(True)
def move_up():
    move_last_body_sprite_towhere_head_was()
    snake_head.set_position(head_x_prior, head_y_prior - s)

def on_left_repeated():
    move_left()
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

snake_head_image: Image = None
dy = 0
dx = 0
body_next_to_last_sprite: Sprite = None
body_last_sprite: Sprite = None
snake_body_list: List[Sprite] = []
snake_body_image: Image = None
body_sprite: Sprite = None
y2 = 0
x2 = 0
heart_sprite: Sprite = None
head_y_prior = 0
head_x_prior = 0
snake_head: Sprite = None
heart = 0
heart_image: Image = None
s = 0
scene.set_background_color(7)
s = 7
create_snake_head()
create_snake_body()
heart_image = img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . f f f . f f f . . . . 
        . . . . f 3 3 3 f 3 3 3 f . . . 
        . . . . f 3 3 3 3 3 1 3 f . . . 
        . . . . f 3 3 3 3 3 3 3 f . . . 
        . . . . . f 3 b b b 3 f . . . . 
        . . . . . f f b b b f f . . . . 
        . . . . . . f f b f f . . . . . 
        . . . . . . . f f f . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . .
""")
heart = 0
create_random_heart()
info.set_score(0)
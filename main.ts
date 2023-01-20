namespace SpriteKind {
    export const snake_head_sprite = SpriteKind.create()
    export const snake_body_sprite = SpriteKind.create()
}
/**
 * this snake game is different than others, when you eat the heart your body will left the heart place and youneed let you body completed fullof screen
 */
function move_right () {
    move_last_body_sprite_towhere_head_was()
    snake_head.setPosition(head_x_prior + s, head_y_prior)
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    move_up()
})
function create_random_heart () {
    for (let index = 0; index < randint(1, 2); index++) {
        if (heart < 3) {
            heart_sprite = sprites.create(heart_image, SpriteKind.Food)
            x = randint(7, 160 - 7)
            y = randint(7, 120 - 7)
            heart_sprite.setPosition(x, y)
            heart += 1
        }
    }
}
controller.up.onEvent(ControllerButtonEvent.Repeated, function () {
    move_up()
})
function make_body_sprite (x: number, y: number) {
    body_sprite = sprites.create(snake_body_image, SpriteKind.snake_body_sprite)
    body_sprite.setPosition(x, y)
    snake_body_list.push(body_sprite)
}
controller.right.onEvent(ControllerButtonEvent.Repeated, function () {
    move_right()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    move_left()
})
function create_snake_body () {
    snake_body_image = image.create(s, s)
    snake_body_image.fill(9)
    snake_body_list = sprites.allOfKind(SpriteKind.snake_body_sprite)
    for (let index = 0; index <= 4; index++) {
        make_body_sprite(snake_head.x, snake_head.y + (index + 1) * s)
    }
}
function move_last_body_sprite_towhere_head_was () {
    head_x_prior = snake_head.x
    head_y_prior = snake_head.y
    snake_body_list[0] = snake_body_list.pop()
    snake_body_list[0].setPosition(snake_head.x, snake_head.y)
}
function lengthen_snake_by_one_sprite () {
    let dy = 0
    let dx = 0
    body_last_sprite = snake_body_list[snake_body_list.length - 1]
    body_next_to_last_sprite = snake_body_list[snake_body_list.length - 2]
    x = body_last_sprite.x + dx
    y = body_last_sprite.y + dy
    make_body_sprite(x, y)
}
function move_left () {
    move_last_body_sprite_towhere_head_was()
    snake_head.setPosition(head_x_prior - s, head_y_prior)
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    move_right()
})
sprites.onOverlap(SpriteKind.snake_head_sprite, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    otherSprite.destroy(effects.spray, 500)
    heart += -1
    lengthen_snake_by_one_sprite()
    create_random_heart()
})
function move_down () {
    move_last_body_sprite_towhere_head_was()
    snake_head.setPosition(head_x_prior, head_y_prior + s)
}
controller.down.onEvent(ControllerButtonEvent.Repeated, function () {
    move_down()
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    move_down()
})
sprites.onOverlap(SpriteKind.snake_head_sprite, SpriteKind.snake_body_sprite, function (sprite, otherSprite) {
    game.over(false, effects.dissolve)
})
function create_snake_head () {
    snake_head_image = image.create(s, s)
    snake_head_image.fill(4)
    snake_head = sprites.create(snake_head_image, SpriteKind.snake_head_sprite)
    snake_head.setStayInScreen(true)
}
function move_up () {
    move_last_body_sprite_towhere_head_was()
    snake_head.setPosition(head_x_prior, head_y_prior - s)
}
controller.left.onEvent(ControllerButtonEvent.Repeated, function () {
    move_left()
})
let snake_head_image: Image = null
let body_next_to_last_sprite: Sprite = null
let body_last_sprite: Sprite = null
let snake_body_list: Sprite[] = []
let snake_body_image: Image = null
let body_sprite: Sprite = null
let y = 0
let x = 0
let heart_sprite: Sprite = null
let head_y_prior = 0
let head_x_prior = 0
let snake_head: Sprite = null
let heart = 0
let heart_image: Image = null
let s = 0
tiles.setCurrentTilemap(tilemap`level3`)
s = 7
create_snake_head()
create_snake_body()
heart_image = img`
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
    `
heart = 0
create_random_heart()
info.setScore(0)

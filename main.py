class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
    jewel = 3
    rock = 4
@namespace
class SpriteKind:
    jewel2 = SpriteKind.create()
def spawn_rocks():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . d d d . . . . . . 
                    . . . . d d d d d d d d . . . . 
                    . . d d d d d d d e d d d d . . 
                    . d d d d d d d d d d d d d d . 
                    . d d d e e e e d d d d d d d . 
                    d d d e d d d d d d d d d d d d 
                    d d d e d d d d d d e d d d d d 
                    d d d d d d d d d d e e e d e d 
                    d e d d d d d e d d d d e d d d 
                    d d d d d d d d d d d d e d d d 
                    d d d d e d d d d d d e e d d d 
                    . d d d e e e e d d d e d d d . 
                    . d d d d d d d d d d d d d d . 
                    . . d d d d d d d d d d d d . . 
                    . . . d d d d d e d d d d . . . 
                    . . . . . d d d d d d . . . . .
        """),
        SpriteKind.enemy)
    mySprite2.set_position(40, 5)
    mySprite2.ay = 200
    animation.attach_animation(mySprite2, rockanim2)
    animation.set_action(mySprite2, ActionKind.rock)
def spawn_jewels():
    global jewel22
    for value in scene.get_tiles_by_type(9):
        jewel22 = sprites.create(img("""
                . . . . . f f f f f . . . . . . 
                            . . . . f 9 9 9 9 9 f . . . . . 
                            . . . f 9 9 9 9 9 9 9 f . . . . 
                            . . f 9 9 9 9 9 9 9 9 9 f . . . 
                            . . f 9 9 9 9 1 9 9 9 9 f . . . 
                            . . f 9 9 9 9 1 9 9 9 9 f . . . 
                            . . f 9 9 9 1 1 1 9 9 9 f . . . 
                            . . f 9 9 9 1 1 1 9 9 9 f . . . 
                            . . f 9 9 9 1 1 1 9 9 9 f . . . 
                            . . f 9 9 9 1 1 1 9 9 9 f . . . 
                            . . f 9 9 9 1 1 1 9 9 9 f . . . 
                            . . f 9 9 9 9 1 9 9 9 9 f . . . 
                            . . f 9 9 9 9 1 9 9 9 9 f . . . 
                            . . . f 9 9 9 9 9 9 9 f . . . . 
                            . . . . f 9 9 9 9 9 f . . . . . 
                            . . . . . f f f f f . . . . . .
            """),
            SpriteKind.jewel2)
        value.place(jewel22)
        animation.attach_animation(jewel22, jewelanim2)
        animation.set_action(jewel22, ActionKind.jewel)
def spawn_player():
    global mySprite
    mySprite = sprites.create(img("""
            . . . . f f f f f f f f f . . . 
                    . . . f e e e e e e e e e f . . 
                    . f f f e e e e e e e e e f f . 
                    f e e e e e e e e e e e e e e f 
                    . f f 5 5 5 d d d 5 d d 5 f f . 
                    . . f 5 5 d 1 d d d d 1 d f . . 
                    . f f 5 d d f d d d d f d f . . 
                    f 5 f d d d d d d d d d d f . . 
                    f 5 f d d d d d d d d d d f . . 
                    . f f d d d d d d f d d f f . . 
                    f 5 4 f d d d d d d d f 4 . . . 
                    . f d f f f f f f f f f d f . . 
                    . . f f 4 4 4 4 4 4 4 f f . . . 
                    . . . f e e e f e e e f . . . . 
                    . . f e e e e f e e e e f . . . 
                    . . . f f f f . f f f f . . . .
        """),
        SpriteKind.player)
    mySprite.set_position(30, 230)
    scene.camera_follow_sprite(mySprite)
    controller.move_sprite(mySprite, 100, 0)
def rockanim():
    global rockanim2
    rockanim2 = animation.create_animation(ActionKind.rock, 200)
    rockanim2.add_animation_frame(img("""
        . . . . . f f f f f f . . . . . 
                . . . f f d d d d d d f f . . . 
                . . f d d d d d d e d d d f . . 
                . f d d d d d d d d d d d d f . 
                . f d d d d e e e e d d d d f . 
                f d d d d d d d d e e e d d d f 
                f d d d d d d d d d d d d d d f 
                f d d e d d d d d d d d d d d f 
                f d d d d d d d e d d d d d d f 
                f d d d d d d d d d d d e e d f 
                f d d d e e d d d d d d e d d f 
                . f d d d e e d d d d e e d f . 
                . f d d d d e e d d d d d d f . 
                . . f d d d d d d d d d d f . . 
                . . . f f d d d d e d f f . . . 
                . . . . . f f f f f f . . . . .
    """))
    rockanim2.add_animation_frame(img("""
        . . . . . f f f f f f . . . . . 
                . . . f f d d d d d d f f . . . 
                . . f d d d d d d d d d d f . . 
                . f d d d d e d d d d d d d f . 
                . f d d d e e d d d d d e d f . 
                f d d d e e d d d d d d e d d f 
                f d d d e d d d d d d d e d d f 
                f d d e d d d d d d d d e d e f 
                f d d d d d d d e d d e e d d f 
                f d d d d d d d d d d e d d d f 
                f d d d d d d e d d d e d d d f 
                . f d e d d d e e e d d d d f . 
                . f d d d d d d d e d d d d f . 
                . . f d d d d d d d d d d f . . 
                . . . f f d d d d d d f f . . . 
                . . . . . f f f f f f . . . . .
    """))
def new_level():
    global levelnum, speed, jewelnum, lvlcomplete, open2
    mySprite2.destroy()
    mysprite3.destroy()
    levelnum += 1
    effects.confetti.end_screen_effect()
    if levelnum == 2:
        speed = 6000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 9 b b b b b b 9 b b b b b 9 7 
                        2 4 4 4 b b 4 4 4 4 b b 4 4 4 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b b 9 b b b b b 7 
                        2 b b 4 4 4 b b 4 4 4 4 4 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 9 b b b b b b 9 b b b b b 9 7 
                        2 4 4 4 b b 4 4 4 4 4 4 b b 4 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b b b b b b b b b f 
                        2 4 4 4 4 4 4 b b 4 4 4 4 4 4 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b 9 b b 3 b b b b 7 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 3:
        speed = 5000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b 9 b b b b b b b b 9 b b 7 
                        2 4 4 4 b b b b b b b b 4 4 4 7 
                        2 b b 4 b b b 9 3 b b b 4 b b 7 
                        2 b b 4 b b 4 4 4 4 b b 4 b b 7 
                        2 b 9 4 b b b b b b b b 4 9 b 7 
                        2 b 4 4 b b b b b b b b 4 4 b 7 
                        2 b b 4 4 b b b b b b 4 4 b b 7 
                        2 b b b b b b b 9 b b b b b b 7 
                        2 4 b b b b b 4 4 b b b b b 4 7 
                        2 b b 9 b b b b b b b b 9 b b 7 
                        2 b b 4 b b 4 b b 4 b b 4 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b b b b b b b b b f 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 4:
        speed = 4000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 9 b b b b b b b b b b b b 9 7 
                        2 4 b b b b b 9 3 b b b b b 4 7 
                        2 b 4 b b b b 4 4 b b b b 4 b 7 
                        2 b b 4 b b b b b b b b 4 b b 7 
                        2 b b b 4 b b b 9 b b 4 b b b 7 
                        2 b b b b 4 b b b b 4 b b b b 7 
                        2 9 b b b b 4 b b 4 b b b b 9 7 
                        2 4 b b b b b b b b b b b b 4 7 
                        2 b b b b b b b 9 b b b b b b 7 
                        2 b b b b 4 4 4 4 4 4 b b b b 7 
                        2 b b 4 4 b b b b b b 4 4 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b b 9 b b b b b b f 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 5:
        speed = 4000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b 4 4 4 4 4 9 b 4 4 4 4 4 b 7 
                        2 b b b b b 4 b b 4 b b b b b 7 
                        2 9 b b b b 4 b 9 4 b b b b 9 7 
                        2 4 4 b b b 4 b b 4 b b b 4 4 7 
                        2 b b b b b 4 9 b 4 b b b b b 7 
                        2 b b b b 9 4 b b 4 9 b b b b 7 
                        2 b b b 4 4 4 b 9 4 4 4 b b b 7 
                        2 b b b b b 4 b b 4 b b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 4 4 b b b b b b b b b b 4 4 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b 3 b b b b b b b f 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 6:
        speed = 3000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b 9 9 b b b b b b b 9 9 b b 7 
                        2 b 4 4 b b b b b b b 4 4 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b 9 b b b 9 b b b b b 7 
                        2 b b b 4 4 b b b 4 4 b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b 9 b b b b b b b b 9 b b 7 
                        2 b b 4 b b 4 b b 4 b b 4 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 4 b b b b b 3 b b b b b b 4 7 
                        2 b b b b b b 4 4 b b b b b b 7 
                        f b b b b b b 4 4 b b b b b b f 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 7:
        speed = 3000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b 9 b b 9 b b b b b 7 
                        2 b 4 4 4 4 4 b b 4 4 4 4 b b 7 
                        2 b b b b 4 9 b b 9 4 b b b b 7 
                        2 b b b b 4 4 b b 4 4 b b b b 7 
                        2 4 b b b b b b b b b b b b 4 7 
                        2 9 b b b b b 3 b b b b b b 9 7 
                        2 4 4 4 b b b 4 4 b b b 4 4 4 7 
                        2 b b 4 b b b b b b b b 4 b b 7 
                        2 b 9 4 b b b b b b b b 4 9 b 7 
                        2 b 4 4 b b 4 4 4 4 b b 4 4 b 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b b b b b b b b b f 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 8:
        speed = 2000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b b b b b 9 b b 7 
                        2 b 4 4 4 4 4 b 9 b 4 4 4 b b 7 
                        2 b b b b 9 4 b b b 4 b b b b 7 
                        2 9 b b b b 4 b b b 4 b b b 9 7 
                        2 4 b b b b b b b b b b b b 4 7 
                        2 b b b b b b b 3 b b b b b b 7 
                        2 b b 9 b 4 4 4 4 4 4 b 9 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 4 b b b b b 9 b b b b b b 4 7 
                        2 b b b b b b 4 4 b b b b b b 7 
                        2 b b 4 b b b b b b b b 4 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b b b b b b b b b f 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 9:
        speed = 2000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b 9 b b b b 9 b b b b 9 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 4 9 b b b b 9 b b b b 9 b 4 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b 9 b b b b b b b b b 9 b b 7 
                        2 b 4 4 4 4 4 4 4 4 4 4 4 b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b b b b b b b b b f 
                        2 4 4 b b b b b b b b b b 4 4 7 
                        2 b b b b 4 b b b b 4 b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b 3 b b b b b b 7 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 10:
        speed = 1000
        scene.set_tile_map(img("""
            1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
                        2 b b b b b b b b b b b b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 9 b b b b b b b 3 b b b 9 b 7 
                        2 4 b b b 4 b b b 4 b b b 4 b 7 
                        2 b b 9 b b b 9 b b b 9 b b b 7 
                        2 b b 4 b b b 4 b b b 4 b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 4 b b b 4 b b b 4 b b b 4 b 7 
                        2 b b 9 b b b 9 b b b 9 b b b 7 
                        2 b b 4 b b b 4 b b b 4 b b b 7 
                        2 b b b b b b b b b b b b b b 7 
                        2 4 b b b 4 b b b 4 b b b 4 b 7 
                        2 b b b b b b b b b b b b b b 7 
                        f b b b b b b b b b b b b b b f 
                        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        """))
    if levelnum == 11:
        game.over(True)
    spawn_player()
    spawn_jewels()
    rockanim()
    jewelanim()
    jewelnum = 0
    lvlcomplete = 0
    open2 = 0
def spawn_rock2():
    global mysprite3
    mysprite3 = sprites.create(img("""
            . . . . . . . d d d . . . . . . 
                    . . . . d d d d d d d d . . . . 
                    . . d d d d d d d e d d d d . . 
                    . d d d d d d d d d d d d d d . 
                    . d d d e e e e d d d d d d d . 
                    d d d e d d d d d d d d d d d d 
                    d d d e d d d d d d e d d d d d 
                    d d d d d d d d d d e e e d e d 
                    d e d d d d d e d d d d e d d d 
                    d d d d d d d d d d d d e d d d 
                    d d d d e d d d d d d e e d d d 
                    . d d d e e e e d d d e d d d . 
                    . d d d d d d d d d d d d d d . 
                    . . d d d d d d d d d d d d . . 
                    . . . d d d d d e d d d d . . . 
                    . . . . . d d d d d d . . . . .
        """),
        SpriteKind.enemy)
    mysprite3.set_position(195, 5)
    mysprite3.ay = 200
    animation.attach_animation(mysprite3, rockanim2)
    animation.set_action(mysprite3, ActionKind.rock)

def on_hit_tile(sprite):
    mySprite2.vx = 50
    mysprite3.vx = -50
scene.on_hit_tile(SpriteKind.enemy, 4, on_hit_tile)

def jewelanim():
    global jewelanim2
    jewelanim2 = animation.create_animation(ActionKind.jewel, 100)
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 1 1 1 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))
    jewelanim2.add_animation_frame(img("""
        . . . . . f f f f f . . . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 1 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . f 9 9 9 9 9 9 9 9 9 f . . . 
                . . . f 9 9 9 9 9 9 9 f . . . . 
                . . . . f 9 9 9 9 9 f . . . . . 
                . . . . . f f f f f . . . . . .
    """))

def on_life_zero():
    game.over(False)
info.on_life_zero(on_life_zero)

def on_hit_tile2(sprite2):
    global lvlcomplete
    lvlcomplete = 1
scene.on_hit_tile(SpriteKind.player, 3, on_hit_tile2)

def on_hit_tile3(sprite3):
    sprite3.destroy(effects.ashes, 500)
scene.on_hit_tile(SpriteKind.enemy, 15, on_hit_tile3)

def on_on_overlap(sprite4, otherSprite):
    global jewelnum
    music.play_tone(659, music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.QUARTER))
    jewelnum += 1
    otherSprite.destroy(effects.trail, 100)
    otherSprite.y += -3
sprites.on_overlap(SpriteKind.player, SpriteKind.jewel2, on_on_overlap)

def music2():
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.DOUBLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.DOUBLE))

def on_on_overlap2(sprite5, otherSprite2):
    global releaserock
    mySprite.destroy()
    mySprite2.destroy()
    mysprite3.destroy()
    otherSprite2.destroy()
    mySprite.start_effect(effects.disintegrate)
    releaserock = 0
    info.change_life_by(-1)
    music.power_down.play()
    pause(2000)
    spawn_player()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

jump = 0
right = 0
releaserock = 0
open2 = 0
lvlcomplete = 0
mysprite3: Sprite = None
mySprite: Sprite = None
jewelanim2: animation.Animation = None
jewel22: Sprite = None
rockanim2: animation.Animation = None
mySprite2: Sprite = None
speed = 0
jewelnum = 0
levelnum = 0
music.set_volume(255)
scene.set_background_image(img("""
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccc96ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccc9996cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccc999996ccccccddddddddbcddddddddddbcddddbcccccccddddbcddddddddddbcddddbcccccccccccccdddddddddddbcdddddddddddbcddddbcddddddddddbcccddddddddddbcdddddddddddbccccc
        cc99999996cccccddddddddbcdddddddddbbcddddbcccccccddddbcddddddddddbcddddbcccccccccccccdddddddddddbcdddddddddddbcddddbcddddddddddbcccddddddddddbcdddddddddddbccccc
        cc99919996cccccddddddddbcddddddddddbcddddbcccccccddddbcddddddddddbcddddbcccccccccccccdddddddddddbcdddddddddddbcddddbcdddddddddddbbcddddddddddbcdddddddddddbccccc
        cc99919996cccccddddddddbcddddddddddbcddddbcccccccddddbcddddddddddbcddddbcccccccccccccddddbbdddddbcdddddddddddbcddddbcddddddddddddbcddddddddddbcdddddddddddbccccc
        cc99111996cccccbbbbddddbcddddbbbbbbbcddddbcccccccddddbcddddbbbbbbbcddddbcccccccccccccddddbbbddddbcddddbbbddddbcddddbcddddbbbbddddbcddddbbbbbbbcddddbbbddddbccccc
        cc99111996cccccccccddddbcddddddddddbcddddbcccccccddddbcddddddddddbcddddbcccccccccccccddddbccddddbcddddbccddddbcddddbcddddbcccddddbcddddddddddbcddddbccddddbccccc
        cc99111996cccccccccddddbcddddddddddbcddddbcddddbcddddbcddddddddddbcddddbcccccccccccccdddddddddddbcdddddddddddbcddddbcddddbcccddddbcddddddddddbcdddddddddddbccccc
        cc99111996cccccccccddddbcddddddddddbcddddbcddddbcddddbcddddddddddbcddddbcccccccccccccdddddddddddbcdddddddddddbcddddbcddddbcccddddbcdddddddddbbcdddddddddddbccccc
        cc99919996cccccccccddddbcdddddddddbbcddddddddddddddddbcdddddddbdbbcddddbcccccccccccccdddddddddddbcdddddddddddbcddddbcddddbcccddddbcdddddddbdbbcddddddddddbbccccc
        cc99919996cccccccccddddbcddddbbbbbbbcddddddddddddddddbcddddbbbbbbbcddddbcccccccccccccddddbccdddbccdddddddddddbcddddbcddddbcccddddbcddddbbbbbbbcddddbbbdddbcccccc
        cc99999996cccccccccddddbcddddccccccccddddddddddddddddbcddddccccccccddddbcccccccccccccddddbccddddbcddddbccddddbcddddbcdddbddddddddbcddddbcccccccddddbccddddbccccc
        cc6999996ccdddddddddddbbcddddddddddbcdddddddddddddddbbcddddddddddbcdddddddddddbccccccddddbccddddbcddddbccddddbcddddbcdddddddddddbbcddddddddddbcddddbccddddbccccc
        ccc69996cccddddddddddddbcddddddddddbcdddddddbcdddddddbcddddddddddbcdddddddddddbccccccddddbccddddbcddddbccdddbbcdddbbcdddddddddddbbcddddddddddbcddddbccddddbccccc
        cccc696ccccdddddddddddbbcddddddddddbcddddddbbcddddddbbcddddddddbbbcddddddddddbbccccccdddbbccdddbbbddddbccddddbcddddbcdddddddddbbbbcdddddddddbbcdddbbccddddbccccc
        ccccc6cccccddddddddbbbbbcddddbdddbbbcddddbbbbcbbbddbbbcddddddbbbbbcdddddddbdbbbccccccdbdbbccddbbbcbbbbbccddbbbbddbbbcddddddddbbbcccddddddbbdbbcddbbbccdddbbccccc
        cccccccccccbbbbbbbbbbbbbcbbbbbbbbbbbcbbbbbcccccccbbbbbcbbbbbbbbbbbcbbbbbbbbbbbbccccccbbbbbccbbbbbcbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbcccbbbbbbbbbbbcbbbbbccbbbbbccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccdddddddddddbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccccdddddddddddddbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccddddddddddddddddbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccdddddddddddddddddddbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccdddddddddddbddddddddddbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccdddddddddddbdddddddddddbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccdddddddddddbdddddddddddddbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccddbbdddddbbbbddddddddddddddbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccdddddddddbdddddddddddddddddddbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc96cccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccdddddddddbdddddddddbdddddddddbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc9996ccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccdddddddddbdddddddddbbddddddddbbccccccccccccccccccccccccccccccccccccceeeeeeccccccccccccccccccccccc999996cccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccddddddddddbdddddddddddbbbbdddddbbccccccccccccccccccccccccccccccccccceeeeeeeeccccccccccccccccccccc99999996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccddddddddddbddddddddddddbdbbddddbbccccccccccccccccccccccccccccccccccceeeeeeeeccccccccccccccccccccc99919996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccddddddddddddddddddddddddddbddddbbcccccccccccccccccccccccccccccccceeeeeeeeeeeeeecccccccccccccccccc99111996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccddddddddddddddddddddddddddbddddbbcccccccccccccccccccccccccccccccceeeeeeeeeeeeeecccccccccccccccccc99111996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccddddbdddddddddddddbddddddbbddddbbcccccccccccccccccccccccccccccc55cc4445555555cccccccccccccccccccc99111996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccdddddddddddddddddddddddddbdddddbbccccccccccccccccccccccccccccccc5555555ddddddcccccccccccccccccccc99111996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccdddddddddddddddddddddddddddddddbbcccccccccccccccccccccccccccccccc55555dddddddcccccccccccccccccccc99111996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccdddddddddddddddddddddddddddddddbbccccccccccccccccccccccccccccccc55c5dddd1dd1dcddccccccccccccccccc99111996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccdddddddddddddddddddddddddddddddbbccccccccccccccccccccccccccccdddccc5ddddfddfdcddccccccccccccccccc99111996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccddddddddbbddddddddddddbddddddddbbcccccccccccccccccccccccccccccdddcc5dddddddddce4ccccccccccccccccc99919996ccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccddddddddddbbdddddddddddddddddddbbccccccccccccccccccccccccccccc44eccdddddddfddce4ccccccccccccccccc99999996ccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccbdddddddddbbdbbddddddddddddddbbccccccccccccccccccccccccccccccc44ecdddddddddde44ccccccccccccccccc6999996cccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccbddddddddddbbbdddddddddddddddbbcccccccccccccccccccccccccccccccc44eeeeeeeeeee444cccccccccccccccccc69996ccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccbdddddddddddbbdddddddddddddddbbcccccccccccccccccccccccccccccccc4444444444eee44cccccccccccccccccccc696cccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccbddddddddddddddddddbdddddddbbccccccccccccccccccccccccccccccccccc444ee4444444cccccccccccccccccccccc6ccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccbddddddddddddddddddddddddbbcccccccccccccccccccccccccccccccccccc444ee4444444cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccbddddddddddddddddddddddbbcccccccccccccccccccccccccccccccccccccc4444444444ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccbbddddddddddddddddddddbbbcccccccccccccccccccccccccccccccccccccc444444ee4cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccbddddddddbdddddddddbbcccccccccccccccccccccccccccccccccccccccceeeeeeeeecccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccbdddddddddddddddbbbcccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccccbbbddddddddddbbbbcccccccccccccccccccccccccccccccccccccccccfeeeecceeeefcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccffeecccceffccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccc
        cccfdddddddddddddddddfddddddddddddddddddfdddddddddddddddddfdddddddddddddddddfddddddddddddddddddfdddddddddddddddddfddddddddddddddddddddfddddddddddddddddddfcccccc
        cccfdddeddeeddeeddeddfdeddeeedeeeddeedeefdddedeeeddeddededfdeddeeedddeedeeddfdeeeedddddddedddeefddddeedeeeddeddeefedddedeeddeddeededdefeddeedeeeddedeedddfcccccc
        cccfeeeeeeeeeeeeedeeefeeeeeeeeeeeeeeeeeefeddeeeeeeeeeeeeeefeeeeeeeeedeeeeeeefeeeeedeeeedeeeeeeefedeeeeeeeeeeeeeeefedeeeeeeeeeeeeeeedeefedeeeeeeeedeeeedeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeee5eeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeee5eeeeeeeeeeeeefee5eeeeeeeeeeee5eefeeeeeeeeeeeeeeeeefee5eeeeeeeeeeeeeeeeefeeeeeeeeeeeee5eeeefcccccc
        cccfeeeeeeeeee5eeeeeefeeeeeee5eeeeee5eeefeeeeee5eeeeeeeeeefeeeeeeeeeee5eeeeefeeeeeeeeeeeeeeeeeefeeeeee5eeeeeeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeee5eeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeee5eeeeeefeee5eeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeee5feeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeee5eeeeeeeeefeeeeeeeeeeeee5eeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeee5eeeeeeeeeeefeee5eeeeeeeeeeeeeefeee5eeeeeeeeeeeeefeeee5eeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeee5efeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeee5eeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeee5eeeeeeefcccccc
        cccfeeeeeeeeeeee5eeeefeeeeeeeeeeeeeeeeeefeeeeeee5eeeeee5eefeeeeeeeeeeee5eeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeee5eeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeee5eeeeeeeeeefeeeee5eeeeee5eeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeee5eeeeeeeeeeeeeefee5eeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeee5eeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeee5eeeeeeeeeeeee5eefeeeee5eeeeeeeee5eefcccccc
        cccfeee5eeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeee5eeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeee5eeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeee5efeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeefcccccc
        cccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
"""))
music2()
game.show_long_text("Journey through 10 acion packed levels collecting all the jewels in each. Press A to start",
    DialogLayout.BOTTOM)
info.set_life(3)
levelnum = 1
jewelnum = 0
speed = 7000
scene.set_background_image(img("""
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
"""))
scene.set_tile_map(img("""
    1 5 6 5 5 5 5 5 5 5 5 5 6 5 5 1 
        2 b b b b b b b b b b b b b b 7 
        2 b b 9 b b b b b b b b 9 b 3 7 
        2 b 4 4 4 b b b b b b b 4 4 4 7 
        2 b b 4 b b b b b b b b b b b 7 
        2 b b 4 b 9 b b b 4 4 4 b b b 7 
        2 b b 4 4 4 b b b b b b b b b 7 
        2 b b b b 9 b b b b b b b b b 7 
        2 b b b b 4 4 4 b b b 9 b b b 7 
        2 b b b b b b b b b b 4 b b b 7 
        2 b b b b b b b b b b b b b 9 7 
        2 b b b 9 b b b b b b b b b b 7 
        2 b b 4 4 b b b b 4 4 4 4 b b 7 
        2 b b b b b b b b b b b b b b 7 
        f b b b b b b b b b 9 b b b b f 
        1 4 4 4 4 4 4 4 4 4 4 4 4 4 4 1
"""))
scene.set_tile(4,
    img("""
        f f f f f f f f f f f f f f f f 
            f d d d d d d d d d d d d d d f 
            f d e d e d d e e d d e d d d f 
            f e e e e d e 5 e e e e e d e f 
            f e e e e e e e e e e e e e e f 
            f 5 5 e e e e e e e e e e 5 e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e 5 e e e e e 5 e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e 5 e f 
            f e e e e e 5 e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f f f f f f f f f f f f f f f f
    """),
    True)
scene.set_tile(2,
    img("""
        f f f f f f f f f f f f f f f f 
            f d e 5 e e e e e e e e e d d f 
            f d e e e e e e e e e e e e d f 
            f d e e e e e 5 e e e e e e d f 
            f d e e e e e e e e e e e d d f 
            f d 5 e e e e e e e e e d d d f 
            f d d e e e e e e e e e e e d f 
            f d e e e e e e e e e e e d d f 
            f d e e e e e e e e e e d d d f 
            f d e e 5 e e e e e 5 e e e d f 
            f d d e e e e e e e e e e d d f 
            f d e e e e e e e e e e e d d f 
            f d e e e e e e e e e e d d d f 
            f d e e e e 5 e e e e e e e d f 
            f d e e e e e e e e e e e d d f 
            f f f f f f f f f f f f f f f f
    """),
    True)
scene.set_tile(7,
    img("""
        f f f f f f f f f f f f f f f f 
            f d d 5 e e e e e e e e e e d f 
            f d e e e e e e e e e e e e d f 
            f d d e e e e 5 e e e e e e d f 
            f d d d e e e e e e e e e e d f 
            f d d e e e e e e e e 5 e d d f 
            f d e e e e e e e e e e e e d f 
            f d d e e e e e e e e e e e d f 
            f d d e e e e e e e e e e e d f 
            f d e e 5 e e e e e 5 e e e d f 
            f d d e e e e e e e e e e e d f 
            f d d d d e e e e e e e e d d f 
            f d d d d e e e e e e e e 5 d f 
            f d d e e e 5 e e e e e e e d f 
            f d d e e e e e e e e e e e d f 
            f f f f f f f f f f f f f f f f
    """),
    True)
scene.set_tile(5,
    img("""
        f f f f f f f f f f f f f f f f 
            f e e 5 e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e 5 e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e 5 e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e 5 e e e e e 5 e e e e f 
            f e e e e e e e e e e e e e e f 
            f e d e e e e e e e e e e e e f 
            f e d e e e d d e e e e d d e f 
            f e d d d d d d e d d e d d e f 
            f d d d d d d d d d d d d d d f 
            f f f f f f f f f f f f f f f f
    """),
    True)
scene.set_tile(1,
    img("""
        f f f f f f f f f f f f f f f f 
            f e e 5 e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e 5 e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e 5 e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e 5 e e e e e 5 e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f e e e e e e 5 e e e e e e e f 
            f e e e e e e e e e e e e e e f 
            f f f f f f f f f f f f f f f f
    """),
    True)
scene.set_tile(15,
    img("""
        f f f f f f f f f f f f f f f f 
            f d e e e e e e e e e e e e d f 
            f d e e e e e e e 5 e e e e d f 
            f d e e e e e e e e e e e d d f 
            f d e e e 5 e e e e e e e d d f 
            f d d e e e e e e e e e e e d f 
            f d e e e e e e e e e e e e d f 
            f d e e e e e e e 5 e e e d d f 
            f d 5 e e e e e e e e e e d d f 
            f d e e e e e e e e e e e e d f 
            f d e e e e e e e e e e e e d f 
            f d d e e e e e e e e e e e d f 
            f d d e e 5 e e e e e e e d d f 
            f d e e e e e e e e e e e e d f 
            f d e e e e e e e e e e e e d f 
            f f f f f f f f f f f f f f f f
    """),
    True)
scene.set_tile(3,
    img("""
        . . . . f f f f f f f f . . . . 
            . . . f 4 4 4 4 4 4 4 4 f . . . 
            . . f 4 4 4 5 5 5 5 4 4 4 f . . 
            . f 4 4 4 5 5 f f 5 5 4 4 4 f . 
            f 4 4 4 4 5 f f f f 5 4 4 4 4 f 
            f d 4 4 4 5 f f f f 5 4 4 4 d f 
            f d d 4 4 5 f f f f 5 4 4 d d f 
            f 4 d d d 5 5 f f 5 5 d d d 4 f 
            f 4 4 4 d 5 5 f f 5 5 d 4 4 4 f 
            f 4 4 4 4 5 5 f f 5 5 4 4 4 4 f 
            f 4 4 4 4 5 f f f f 5 4 4 4 4 f 
            f 4 4 4 4 5 f f f f 5 4 4 4 4 f 
            f 4 4 4 d 5 5 f f 5 5 d 4 4 4 f 
            f 4 4 d d 4 5 5 5 5 4 d d 4 4 f 
            f d d d 4 4 4 4 4 4 4 4 d d d f 
            f f f f f f f f f f f f f f f f
    """),
    False)
scene.set_tile(11,
    img("""
        b b b b b b b b c b b b b b b b 
            b b b c b b b b b b b b b c b b 
            b b b c b b b b b b b c c c b b 
            b b b c b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b c b b b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b c c b b 
            b b b c b b b b b b b b b b b b 
            b b b c b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b c c b b 
            b b b b b b b b b b b b b c b b 
            b b b b b b b b b b b b b b b b
    """),
    False)
scene.set_tile(6,
    img("""
        b b b b b b b b c b b b b b b b 
            b b b c b b b b b b b b b c b b 
            b b b c b b b b b b b c c c b b 
            b b b c b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b c b b b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b c c b b 
            b b b c b b b b b b b b b b b b 
            b b b c b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b b b b b 
            b b b b b b b b b b b b c c b b 
            b b b b b b b b b b b b b c b b 
            b b b b b b b b b b b b b b b b
    """),
    False)
scene.set_tile(9,
    img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . c . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . c . . . . 
            . . . . . . . . . . . c . . . . 
            . . . c c . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . c . . . . . . . . . 
            . . . . . . c . . . . . . . c . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    False)
jewelanim()
rockanim()
spawn_jewels()
spawn_rocks()
spawn_rock2()
spawn_player()

def on_forever():
    global right
    if mySprite.vx > 0 and mySprite.vy > 0:
        right = 0
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 5 d 1 d d d d 1 d f . . 
                        . f f 5 d d f d d d d f d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        . f f 5 d d d d d f d d f f . . 
                        f 5 4 f d d d d d d d f 4 f . . 
                        . f d f f f f f f f f f f d f . 
                        . . f f 4 4 4 4 4 4 4 f f f . . 
                        . . . f e e e f e e e f . . . . 
                        . . . f f f f f e e e e f . . . 
                        . . . . . . . . f f f f . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 5 d 1 d d d d 1 d f . . 
                        . f f 5 d d f d d d d f d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        . f f 5 d d d d d f d d f f . . 
                        f 5 4 f d d d d d d d f 4 f . . 
                        f d f f f f f f f f f f d f . . 
                        f f f f 4 4 4 4 4 4 4 f f f . . 
                        . . . f e e e f e e e f . . . . 
                        . . f e e e e f f f f f . . . . 
                        . . . f f f f . . . . . . . . .
        """))
        pause(100)
    if mySprite.vx == 0 and right == 0:
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 5 d 1 d d d d 1 d f . . 
                        . f f 5 d d f d d d d f d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        . f f 5 d d d d d f d d f f . . 
                        f 5 4 f d d d d d d d f 4 . . . 
                        . f d f f f f f f f f f d f . . 
                        . . f f 4 4 4 4 4 4 4 f f . . . 
                        . . . f e e e f e e e f . . . . 
                        . . f e e e e f e e e e f . . . 
                        . . . f f f f . f f f f . . . .
        """))
    if mySprite.vx < 0:
        right = 1
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 1 d d d d 1 d d d f . . 
                        . . f 5 f d d d d f d d d f f . 
                        . . f 5 d d d d d d d d d f 5 f 
                        . . f 5 d d d d d d d d d f 5 f 
                        . . f 5 d d f d d d d d f f f . 
                        . f 4 f f d d d d d d f 4 f 5 f 
                        . f d f f f f f f f f f f d f . 
                        . . f f 4 4 4 4 4 4 4 f f f . . 
                        . . . f e e e f e e e f . . . . 
                        . . . f f f f f e e e e f . . . 
                        . . . . . . . . f f f f . . . .
        """))
        pause(100)
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 1 d d d d 1 d d d f . . 
                        . . f 5 f d d d d f d d d f f . 
                        . . f 5 d d d d d d d d d f 5 f 
                        . . f 5 d d d d d d d d d f 5 f 
                        . . f 5 d d f d d d d d f f f . 
                        . f 4 f f d d d d d d f 4 f 5 f 
                        f d f 4 f f f f f f f f d f f . 
                        f f f f 4 4 4 4 4 4 4 f f . . . 
                        . . . f e e e f e e e f . . . . 
                        . . f e e e e f f f f f . . . . 
                        . . . f f f f f . . . . . . . .
        """))
        pause(100)
    if mySprite.vx == 0 and right == 1:
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 1 d d d d 1 d d d f . . 
                        . . f 5 f d d d d f d d d f f . 
                        . . f 5 d d d d d d d d d f 5 f 
                        . . f 5 d d d d d d d d d f 5 f 
                        . . f 5 d d f d d d d d f f f . 
                        . f 4 f f d d d d d d f 4 f 5 f 
                        . f d f f f f f f f f f d f f . 
                        . . f f 4 4 4 4 4 4 4 f f f . . 
                        . . . f e e e f e e e f . . . . 
                        . . f e e e e f e e e e f . . . 
                        . . . f f f f f f f f f . . . .
        """))
forever(on_forever)

def on_forever2():
    global jump
    if jump == 0:
        mySprite.ay = 350
    else:
        mySprite.vy = -200
        if mySprite.is_hitting_tile(CollisionDirection.TOP):
            jump = 0
            mySprite.vy = 100
forever(on_forever2)

def on_forever3():
    if mySprite2.x < 5 or mySprite2.x > 247:
        mySprite2.destroy()
    if mysprite3.x < 10 or mysprite3.x > 247:
        mysprite3.destroy()
forever(on_forever3)

def on_forever4():
    if open2 == 1:
        music.magic_wand.play()
        pause(20000)
forever(on_forever4)

def on_forever5():
    global open2
    if lvlcomplete == 0:
        if jewelnum == 8:
            open2 = 1
        if open2 == 1:
            scene.set_tile(3,
                img("""
                    . . . . f f f f f f f f . . . . 
                                    . . . f f f f f f f f f f . . . 
                                    . . f 4 f f f f f f f f 4 f . . 
                                    . f 4 4 f f f f f f f f 4 4 f . 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f 4 4 4 f f f f f f f f 4 4 4 f 
                                    f f f f f f f f f f f f f f f f
                """),
                True)
        else:
            scene.set_tile(3,
                img("""
                    . . . . f f f f f f f f . . . . 
                                    . . . f 4 4 4 4 4 4 4 4 f . . . 
                                    . . f 4 4 4 5 5 5 5 4 4 4 f . . 
                                    . f 4 4 4 5 5 f f 5 5 4 4 4 f . 
                                    f 4 4 4 4 5 f f f f 5 4 4 4 4 f 
                                    f d 4 4 4 5 f f f f 5 4 4 4 d f 
                                    f d d 4 4 5 f f f f 5 4 4 d d f 
                                    f 4 d d d 5 5 f f 5 5 d d d 4 f 
                                    f 4 4 4 d 5 5 f f 5 5 d 4 4 4 f 
                                    f 4 4 4 4 5 5 f f 5 5 4 4 4 4 f 
                                    f 4 4 4 4 5 f f f f 5 4 4 4 4 f 
                                    f 4 4 4 4 5 f f f f 5 4 4 4 4 f 
                                    f 4 4 4 d 5 5 f f 5 5 d 4 4 4 f 
                                    f 4 4 d d 4 5 5 5 5 4 d d 4 4 f 
                                    f d d d 4 4 4 4 4 4 4 4 d d d f 
                                    f f f f f f f f f f f f f f f f
                """),
                False)
    else:
        music.power_up.play()
        effects.confetti.start_screen_effect()
        mySprite.destroy()
        mySprite2.destroy()
        mysprite3.destroy()
        scene.set_tile(3,
            img("""
                . . . . f f f f f f f f . . . . 
                            . . . f f f f f f f f f f . . . 
                            . . f 4 f f e e e e f f 4 f . . 
                            . f 4 4 f e e e e e e f 4 4 f . 
                            f 4 4 4 e e e e e e e e 4 4 4 f 
                            f 4 4 4 f 5 5 5 5 5 5 f 4 4 4 f 
                            f 4 4 4 f 5 5 5 5 5 5 f 4 4 4 f 
                            f 4 4 4 f 5 5 5 5 5 5 f 4 4 4 f 
                            f 4 4 4 f f f 5 5 f f f 4 4 4 f 
                            f 4 4 4 f f 5 4 4 5 f f 4 4 4 f 
                            f 4 4 4 f 4 4 4 4 4 4 f 4 4 4 f 
                            f 4 4 4 d 4 4 4 4 4 4 d 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f e e f f e e f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f f f f f f f f f f f f f f f f
            """),
            True)
        pause(1000)
        scene.set_tile(3,
            img("""
                . . . . f f f f f f f f . . . . 
                            . . . f f f f f f f f f f . . . 
                            . . f 4 f f f f f f f f 4 f . . 
                            . f 4 4 f f f f f f f f 4 4 f . 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f 4 4 4 f f f f f f f f 4 4 4 f 
                            f f f f f f f f f f f f f f f f
            """),
            True)
        pause(1000)
        scene.set_tile(3,
            img("""
                . . . . f f f f f f f f . . . . 
                            . . . f f 4 4 4 4 4 4 f f . . . 
                            . . f 4 4 4 4 4 4 4 4 4 4 f . . 
                            . f 4 4 4 4 4 4 4 4 4 4 4 4 f . 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 5 4 4 5 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                            f f f f f f f f f f f f f f f f
            """),
            True)
        pause(2000)
        new_level()
forever(on_forever5)

def on_forever6():
    global releaserock
    if releaserock == 2:
        pause(2000)
        spawn_rock2()
        releaserock = 0
forever(on_forever6)

def on_forever7():
    global releaserock
    if releaserock == 1:
        spawn_rocks()
        releaserock = 2
forever(on_forever7)

def on_forever8():
    global jump
    if controller.A.is_pressed() and jump == 0 and mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        music.play_tone(523, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(587, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(659, music.beat(BeatFraction.SIXTEENTH))
        jump = 1
        pause(200)
        jump = 0
forever(on_forever8)

def on_forever9():
    if mySprite.vy < 10 and right == 1:
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 1 d d d d 1 d d d f . . 
                        . . f 5 f d d d d f d d d f f . 
                        . . f 5 d d d d d d d d d f 5 f 
                        . . f 5 d d d d d d d d d f 5 f 
                        . f f 5 d d f d d d d d f f f . 
                        f d 4 f f d d d d d d f 4 d 5 f 
                        . f f f f f f f f f f f f f f . 
                        . . . f 4 4 4 4 4 4 4 f . . . . 
                        . . . f e e e f e e e f . . . . 
                        . . . f f e e f f e e f . . . . 
                        . . . . f f f f f f f f . . . .
        """))
    if mySprite.vy < 10 and right == 0:
        mySprite.set_image(img("""
            . . . . f f f f f f f f f . . . 
                        . . . f e e e e e e e e e f . . 
                        . f f f e e e e e e e e e f f . 
                        f e e e e e e e e e e e e e e f 
                        . f f 5 5 5 5 d d 5 d d 5 f f . 
                        . . f 5 5 d 1 d d d d 1 d f . . 
                        . f f 5 d d f d d d d f d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        f 5 f 5 d d d d d d d d d f . . 
                        . f f 5 d d d d d f d d f f . . 
                        f d 4 f d d d d d d d f 4 d . . 
                        . f f f f f f f f f f f f f . . 
                        . . . f 4 4 4 4 4 4 4 f . . . . 
                        . . . f e e e f e e e f . . . . 
                        . . . f e e f f e e f . . . . . 
                        . . . f f f . f f f . . . . . .
        """))
forever(on_forever9)

def on_forever10():
    global releaserock
    if releaserock == 0:
        pause(speed)
        releaserock = 1
forever(on_forever10)

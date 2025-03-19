import play  # oyun kütüphanesi 
frames = 48  # çerçeve
step = 5   # adım

# sprite tanımlama  # daire sprite oluşturuldu
player = play.new_circle(color='green', x=0, y=-290, radius=10, border_color='light green')

# engellerin tanımlanması  # box=kutu, dikdörtgen width ve height
walls = [
    play.new_box(color='black', x=0, y=0, width=100, height=10),
    play.new_box(color='black', x=-50, y=10, width=10, height=200),
    play.new_box(color='black', x=50, y=-10, width=10, height=200),
    play.new_box(color='black', x=100, y=-110, width=10, height=130),
    play.new_box(color='black', x=145, y=-180, width=140, height=10),
    play.new_box(color='black', x=-140, y=-150, width=120, height=10),
    play.new_box(color='black', x=-175, y=-200, width=300, height=10),
    play.new_box(color='black', x=-195, y=-50, width=10, height=300),
    play.new_box(color='black', x=-300, y=10, width=200, height=10),
    play.new_box(color='black', x=-300, y=-40, width=10, height=100),
    play.new_box(color='black', x=-290, y=100, width=200, height=10),
    play.new_box(color='black', x=290, y=120, width=150, height=10),
    play.new_box(color='black', x=100, y=50, width=10, height=300),
    play.new_box(color='black', x=0, y=100, width=150, height=10),
    play.new_box(color='black', x=-130, y=100, width=10, height=300),
    # 10 yeni duvar
    play.new_box(color='black', x=200, y=-50, width=10, height=200),
    play.new_box(color='black', x=-220, y=60, width=100, height=10),
    play.new_box(color='black', x=80, y=180, width=150, height=10),
    play.new_box(color='black', x=160, y=120, width=10, height=100),
    play.new_box(color='black', x=-110, y=240, width=210, height=10),
    play.new_box(color='black', x=250, y=-100, width=100, height=10),
    play.new_box(color='black', x=-260, y=-80, width=10, height=210),
    play.new_box(color='black', x=130, y=-210, width=200, height=10),
    play.new_box(color='black', x=-90, y=-270, width=10, height=100),
    play.new_box(color='black', x=40, y=-260, width=500, height=10),
    # Sol üst köşe duvarları
    play.new_box(color='black', x=-330, y=250, width=10, height=190),
    play.new_box(color='black', x=-250, y=220, width=60, height=10),
    play.new_box(color='black', x=-210, y=150, width=100, height=10),
    # Sağ üst köşe duvarları
    play.new_box(color='black', x=300, y=250, width=10, height=220),
    play.new_box(color='black', x=250, y=210, width=100, height=10),
    play.new_box(color='black', x=220, y=50, width=100, height=10),
    # En sağ, sol ve üst kısma düz duvarlar
    play.new_box(color='black', x=360, y=0, width=10, height=600),  # En sağ
    play.new_box(color='black', x=-360, y=0, width=10, height=600),  # En sol
    play.new_box(color='black', x=0, y=300, width=630, height=10)  # En üst
]

# bitiş noktası
finish = play.new_text(words='Finish', x=0, y=270, font=None, font_size=50, color='red')

@play.when_program_starts
def start():
    player.start_physics(bounciness=0.2)
    for wall in walls:
        wall.start_physics(can_move=False)

@play.repeat_forever
async def game():
    player.physics.x_speed = 0
    player.physics.y_speed = 0

    if play.key_is_pressed('w', 'up'):
        player.physics.y_speed = step
        player.y += 10
    if play.key_is_pressed('s', 'down'):
        player.physics.y_speed = -step
        player.y -= 10
    if play.key_is_pressed('a', 'left'):
        player.physics.x_speed = -step
        player.x -= 10
    if play.key_is_pressed('d', 'right'):
        player.physics.x_speed = step
        player.x += 10

    # Top duvarlara çarptığında başlangıç noktasına dönsün
    for wall in walls:
        if player.is_touching(wall):
            player.x = 0
            player.y = -280

    if player.is_touching(finish):
        for wall in walls:
            wall.hide()
        finish.hide()
        play.new_text(words='YOU WIN!', x=0, y=0, font=None, font_size=100, color='yellow')

    await play.timer(seconds=1/48)

play.start_program()

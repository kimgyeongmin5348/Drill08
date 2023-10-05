from pico2d import *


# Game object class here
class Grass:  # 클래스 이름은 대문자로 작성을 해야 한다.
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = 0,90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global boy
    running = True
    grass = Grass()  # 클래스를 이용해서 객체를 찍어냄.
    boy = Boy()


def render_world():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


def update_world():
    grass.update()
    boy.update()
    pass


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # 객체들의 상호작용을 결과 업데이트
    render_world()
    delay(0.05)
# finalization code

close_canvas()

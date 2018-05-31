import pygame
from pygame.locals import *
import random
import time
#定义一个表示子弹的公共类
class PublicBullet(object):
    def __init__(self,x,y,screen,plane_name):
        self.screen = screen
        self.plane_name = plane_name
        if plane_name == "hero":
            self.x = x + 40
            self.y = y - 20
            image_name = './bullet.gif'
        elif plane_name == "enemy":
            self.x = x + 22
            self.y = y + 30
            image_name = "./bullet_en.gif"
        self.image = pygame.image.load(image_name).convert()
    def move(self):
        if self.plane_name == "hero":
            self.y -= 2
        elif self.plane_name == "enemy":
            self.y += 2
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def judge(self):
        if self.y > 700 or self.y < 0:
            return True
        else:
            return False
class Plane(object):
    def __init__(self,screen,name):
        #飞机的名称
        self.name = name
        #设置要显示内容的窗口
        self.screen = screen
        # 用来保存英雄飞机需要的图片名字
        # 根据名字生成飞机图片
        self.image = pygame.image.load(self.image_name).convert()
        #用来存储英雄飞机发射的所有子弹
        self.bullet_list = []
    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))
        # 用来存放需要删除的对象信息
        need_del_list = []
        # 保存需要删除的对象
        for i in self.bullet_list:
            if i.judge():
                need_del_list.append(i)
        # 删除self.bullet_list中需要删除的对象
        for i in need_del_list:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    # 定义发射子弹的方法
    def launch_bullet(self):
        new_bullet = PublicBullet(self.x, self.y, self.screen, self.name)
        self.bullet_list.append(new_bullet)
#定义英雄飞机的类
class HeroPlane(Plane):
    def __init__(self,screen,name):
        self.x = 230
        self.y = 600
        self.image_name = "./hero.gif"
        #调用父类的__init__方法
        super().__init__(screen,name)
    def move_left(self):
        self.x -= 10
        if self.x < 0:
            self.x = 0
    def move_right(self):
        self.x += 10
        if self.x > 380:
            self.x = 380
#定义敌人飞机类
class EnemyPlane(Plane):
    #重写父类的__init__方法
    def __init__(self,screen,name):
        #设置飞机默认的位置
        self.x = 0
        self.y = 0
        self.image_name = "./enemy.gif"
        #调用父类的__init__方法
        super().__init__(screen,name)
        self.direction = "right"
    #定义一个飞机的移动
    def move(self):
        #如果碰到了右边的边界，那么就向左走，如果碰到了左边的边界，那么就向右走
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"
    def launch_bullet(self):
        number = random.randint(1,100)
        if number == 88 or number == 50:
            super().launch_bullet()
#开始游戏
def start():
    #1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,700),0,32)
    #2.创建一个和窗口大小的图片，用来充当背景
    image_file_path = './background.png'
    background = pygame.image.load(image_file_path).convert()
    #3.创建一个飞机对象
    hero_plane = HeroPlane(screen,"hero")
    #4.创建一个敌人飞机
    enemy_plane = EnemyPlane(screen,"enemy")
    #5.把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        hero_plane.display()
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.launch_bullet()
        #判断是否点击了退出按钮
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    #print("left")
                    hero_plane.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    #print("right")
                    hero_plane.move_right()
                elif event.key == K_SPACE:
                    #print("space")
                    hero_plane.launch_bullet()
        #通过延时的方式，来降低这个while循环的循环速度，从而降低了CPU的占用率
        time.sleep(0.04)
        pygame.display.update()
if __name__ == '__main__':
    start()
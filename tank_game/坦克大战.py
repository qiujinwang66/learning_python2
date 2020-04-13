import pygame,sys,time
from pygame.locals import *
from random import randint
class  TankMain(object):
    '''坦克大战的主窗口'''
    width=600
    height=500
    my_tank_missile_list = []
    #enemy_list = []
    wall=None
    enemy_list=pygame.sprite.Group()#地方坦克的族群
    explode_list=[]
    enemy_missile_list=pygame.sprite.Group()
    my_tank = None
    #开始游戏的方法
    def starGame(self):
        pygame.init()#pygame模块初始化，加载系统的资源
        #创建一个屏幕，屏幕（窗口）的大小（宽，高），窗口特性（0，RESIZABLE,FULLSCREEN）
        screem=pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
        #给窗口设置一个标题
        pygame.display.set_caption("坦克大战")
        #创建墙
        TankMain.wall=Wall(screem,65,160,30,120)

        TankMain.my_tank= My_Tank(screem)  # 创建一个我方坦克，在屏幕中下方展示
        if len(TankMain.enemy_list)==0:
            for i in range(1,6):#游戏开始的时候初始化5个地方坦克
                TankMain.enemy_list.add(Enemy_Tank(screem))#把地方坦克放到组里面

        while True:
            if len(TankMain.enemy_list) < 5:
                TankMain.enemy_list.add(Enemy_Tank(screem))  # 把地方坦克放到组里面
            #color RGB(0,100,200)红绿蓝
            #设置屏幕的背景色为黑色
            screem.fill((0,0,0))
            #显示左上角的文字
            for i,text in enumerate(self.write_text(),0):
                screem.blit(text,(0,5+(20*i)))

            #显示游戏中的墙,并且对墙和其他对象进行碰撞检测
            TankMain.wall.display()
            TankMain.wall.hit_other()
            self.get_event(TankMain.my_tank,screem)#获取事件,根据获取的事件做相应处理
            if TankMain.my_tank:
                TankMain.my_tank.hit_enemy_missille()#我方的坦克和地方的炮弹进行碰撞检测

            if TankMain.my_tank and TankMain.my_tank.live:
                TankMain.my_tank.display()#在屏幕上显示我方坦克
                TankMain.my_tank.move()#在屏幕上移动我方坦克
            else:
                TankMain.my_tank=None
            # 显示和随机移动所有的敌方坦克
            for enemy in TankMain.enemy_list:
                enemy.display()
                enemy.randow_move()
                enemy.randow_fire()
            # 显示所有的我方炮弹
            for m in TankMain.my_tank_missile_list:
                if m.live:
                    m.display()
                    m.hit_tank()#炮弹打中地方坦克
                    m.move()
                else:
                    TankMain.my_tank_missile_list.remove(m)
            # 显示所有的敌方炮弹
            for m in TankMain.enemy_missile_list:
                if m.live:
                    m.display()
                    m.move()
                else:
                    TankMain.enemy_missile_list.remove(m)

            for explode in TankMain.explode_list:
                explode.display()

            #显示重置
            time.sleep(0.05)#每次等待0.05秒一贞
            pygame.display.update()
    #获取所有的事件（敲击键盘，鼠标点击等）
    def get_event(self,my_tank,screem):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()#程序退出
            if event.type ==KEYDOWN and (not my_tank) and event.key==K_n:
                TankMain.my_tank=My_Tank(screem)
            if event.type == KEYDOWN and my_tank:
                if event.key == K_LEFT or event.key == K_a:
                    my_tank.direction="L"
                    my_tank.stop=False
                    #my_tank.move()
                if event.key == K_RIGHT or event.key == K_d:
                    my_tank.direction="R"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key == K_UP or event.key == K_w:
                    my_tank.direction="U"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key == K_DOWN or event.key == K_s:
                    my_tank.direction="D"
                    my_tank.stop = False
                    #my_tank.move()
                if event.key == K_ESCAPE:#点击键盘ESC，程序退出
                    self.stopGame()
                if event.key == K_SPACE:
                    m=my_tank.fire()
                    m.good=True #我方坦克发射的炮弹，好的
                    TankMain.my_tank_missile_list.append(m)
            if event.type == KEYUP and my_tank:
                if event.key==K_LEFT or event==K_RIGHT or event==K_UP or event==K_DOWN:
                    my_tank.stop=True


    #关闭游戏的方法
    def stopGame(self):
        sys.exit()


    #设计游戏窗口的标题
    def set_title(self):
        pass
    #在屏幕的左上角显示文字内容
    def write_text(self):
        font = pygame.font.SysFont("simsunnsimsun",15)#定义一个字体
        text_sf1=font.render("敌方坦克数量为：%d"%len(TankMain.enemy_list),True,(255,0,0))#根据字体创建一个文件图像
        text_sf2=font.render("我方坦克炮弹的数量：%d"%len(TankMain.my_tank_missile_list),True,(255,0,0))#根据字体创建一个文件图像
        return text_sf1,text_sf2

#坦克大战游戏中所有对象的父类
class BaseItem(pygame.sprite.Sprite):
    def __init__(self,screem):
        pygame.sprite.Sprite.__init__(self)
        #所有对象共享的属性
        self.screem=screem#坦克在移动或者显示过程中需要用到当前游戏的窗口

    # 在游戏屏幕中显示当前游戏对象
    def display(self):
        if self.live:
            self.image = self.images[self.direction]
            self.screem.blit(self.image, self.rect)
#坦克的公共父类
class Tank(BaseItem):
    #定义类属性，所有坦克的高和宽都是一样
    whidth=40
    heigt=40
    def __init__(self,screem,left,top):
        super().__init__(screem)#调用父类 init方法
        self.direction="D"#坦克的方向，默认方向往下
        self.speed=5#坦克移动的速度
        self.stop=False
        self.images={}#坦克的所有图片  key 方向， 值为图片
        self.images["L"]=pygame.image.load("images/p1Tankimages/p1tank1L.gif")
        self.images["R"]=pygame.image.load("images/p1Tankimages/p1tank1R.gif")
        self.images["U"]=pygame.image.load("images/p1Tankimages/p1tank1U.gif")
        self.images["D"]=pygame.image.load("images/p1Tankimages/p1tank1D.gif")
        self.image=self.images[self.direction]#坦克的图片 由方向决定
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.live=True #决定坦克是否消灭了
        self.oldtop=self.rect.top
        self.oldleft=self.rect.left

    def stay(self):
        self.rect.top=self.oldtop
        self.rect.left=self.oldleft


    #移动
    def move(self):
        self.oldleft=self.rect.left
        self.oldtop=self.rect.top
        if not self.stop:#如果坦克不是停止状态
            if self.direction=="L":
                if self.rect.left>0:#判断坦克是否在屏幕左边的边界上
                    self.rect.left-=self.speed
                else:
                    self.rect.left=0
            elif self.direction=="R":
                if self.rect.right < TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.rect.right=TankMain.width
            elif self.direction=="U":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                else:
                    self.rect.top=0
            elif self.direction=="D":
                if self.rect.bottom<TankMain.height:
                    if self.rect.bottom < TankMain.height:
                        self.rect.bottom+=self.speed
                    else:
                        self.rect.bottom=TankMain.height


    #发射炮弹
    def fire(self):
        m=Missile(self.screem,self)
        return m

class My_Tank(Tank):
    def __init__(self,screem):
        super().__init__(screem,275,400)#创建一个我方坦克，在屏幕中下方展示
        self.stop=True
        self.live=True

    def hit_enemy_missille(self):
        hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_missile_list,False)
        for m in hit_list:#我方坦克中弹了
            m.live=False
            TankMain.enemy_missile_list.remove(m)
            self.live=False
            explde=Explode(self.screem,self.rect)
            TankMain.explode_list.append(explde)


class Enemy_Tank(Tank):
    def __init__(self,screem):
        super().__init__(screem,randint(1,5)*100,200)
        self.speed=4
        self.step=8#坦克按照某个方向连续移动的步数
        self.get_random_direction()

    def get_random_direction(self):
        r = randint(0, 4)  # 得到一个坦克移动方向和停止的随机数
        if r == 4:
            self.stop = True
        elif r == 1:
            self.direction = "L"
            self.stop = False
        elif r == 2:
            self.direction = "R"
            self.stop = False
        elif r == 3:
            self.direction = "U"
            self.stop = False
        elif r == 4:
            self.direction = "D"
            self.stop = False
    #敌方坦克按照一个确定的随机方向，连续移动6步，然后才能再次改变方向
    def randow_move(self):
        if self.live:
            if self.step==0:
                self.get_random_direction()
                self.step=6
            else:
                self.move()
                self.step-=1

    def randow_fire(self):
        r=randint(0,50)
        if r==10 or r==20 or r==30 or r==40:
            m=self.fire()
            TankMain.enemy_missile_list.add(m)
        else:
            return
#炮弹
class Missile(BaseItem):
    width=12
    height=12
    def __init__(self,screem,tank):
        super().__init__(screem)
        self.tank=tank
        self.direction = tank.direction  # 炮弹的方向由所发射的坦克决定
        self.speed = 12  # 炮弹移动的速度
        self.images = {}  # 炮弹的所有图片  key 方向， 值为图片
        self.images["L"] = pygame.image.load("images/1.png")
        self.images["R"] = pygame.image.load("images/1.png")
        self.images["U"] = pygame.image.load("images/1.png")
        self.images["D"] = pygame.image.load("images/1.png")
        self.image = self.images[self.direction]  # 坦克的图片 由方向决定
        self.rect = self.image.get_rect()
        self.rect.left = tank.rect.left+(tank.whidth-self.width)/2
        self.rect.top =tank.rect.top + (tank.heigt - self.height) /2
        self.live = True  # 炮弹是否消灭了
        self.good=False

    def move(self):
        if self.live:#如果炮弹还存在
            if self.direction=="L":
                if self.rect.left>0:#判断坦克是否在屏幕左边的边界上
                    self.rect.left-=self.speed
                else:
                    self.live=False
            elif self.direction=="R":
                if self.rect.right < TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.live = False
            elif self.direction=="U":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                else:
                    self.live = False
            elif self.direction=="D":
                if self.rect.bottom<TankMain.height:
                    if self.rect.bottom < TankMain.height:
                        self.rect.bottom+=self.speed
                else:
                    self.live = False
    #炮弹击中坦克,第一种，我方炮弹击中敌方坦克
    def hit_tank(self):
        if self.good:#如果炮弹是我方的炮弹
            hit_list = pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
            for e in hit_list:
                e.live=False
                TankMain.enemy_list.remove(e)#如果敌方坦克被击中，则从列表中删除敌方坦克
                self.live=False
                explode = Explode(self.screem,e.rect)#产生了一个爆炸对象
                TankMain.explode_list.append(explode)

#爆炸类
class Explode(BaseItem):
    def __init__(self,screen,rect):
        super().__init__(screen)
        self.live=True
        self.images=[pygame.image.load("images/explode1.bmp"),\
                     pygame.image.load("images/explode2.bmp")]
        self.step=0
        self.rect=rect#爆炸的位置和发生爆炸前，炮弹碰到的坦克位置一样.在构建爆炸的时候把坦克的rect作为参数传递进来
    #display整个游戏过程中，循环调用,每隔0.05秒调用一次
    def display(self):
        if self.live:
            if self.step == len(self.images):#最后一张爆炸图片已经显示了
                self.live=False
            else:
                self.image=self.images[self.step]
                self.screem.blit(self.image,self.rect)
                self.step+=1
        else:
            pass#删除该对象

#游戏中的墙
class Wall(BaseItem):
    def __init__(self,screen,left,top,width,heigh):
        super().__init__(screen)
        self.rect=Rect(left,top,width,heigh)
        self.color=(255,0,0)
    def display(self):
        self.screem.fill(self.color,self.rect)

    #针对墙和其他坦克或炮弹的碰撞检测
    def hit_other(self):
        if TankMain.my_tank:
            is_hit = pygame.sprite.collide_rect(self,TankMain.my_tank)
            if is_hit:
                TankMain.my_tank.stop=True
                TankMain.my_tank.stay()
            if len(TankMain.enemy_list)!=0:
                hit_list = pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
                for e in hit_list:
                    e.stop=True
                    e.stay()



if __name__ == "__main__":
    game=TankMain()
    game.starGame()
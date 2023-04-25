import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)  # 練習1
    bb_img.set_colorkey((0,0,0))  #四隅を透明に
    x=random.randint(10,1590)
    y=random.randint(10,890)
    #screen.blit(bb_img, [x,y])
    vx=+5 ; vy=+5  # 速度の設定
    bb_rct=bb_img.get_rect()
    bb_rct.center= x, y
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
        tmr += 1
        bb_rct.move_ip(vx,vy)  # 爆弾を動かす
        if x+10>=1600 or 0>=x-10:
            vx*=-1
        if y+10>=900 or 0>=y-10:
            vy*=-1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bb_img, bb_rct)
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
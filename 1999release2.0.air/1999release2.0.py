# -*- encoding=utf8 -*-
__author__ = "lxc"

from airtest.core.api import *

auto_setup(__file__)


#from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

import random

# 生成一个随机整数
sjs = random.randint(1, 8)

we,hi=device().get_current_resolution()
hsjg=5
xjg=3
cjg=200

def zhuye():
    sleep(hsjg)
    fanhui=exists(Template(r"tpl1696933958735.png", record_pos=(-0.389, -0.245), resolution=(1600, 900)))
    while fanhui:
        touch(fanhui)
        sleep(hsjg)
        fanhui=exists(Template(r"tpl1696933958735.png", record_pos=(-0.389, -0.245), resolution=(1600, 900)))
        
#左滑函数
def zhuadong(cishu=0):
    sleep(hsjg)
    zana=0
    swipe([0.34*we,0.82*hi],vector=(0.5,0),duration=1)
    while zana<cishu:
        sleep(xjg)
        swipe([0.13*we,0.8*hi],vector=(1,0),duration=0.1)
        zana+=1
def yhuadong(cishu=0):
    sleep(hsjg)
    zana=0
    if cishu==0:
        swipe([0.13*we,0.8*hi],vector=(-0.25,0),duration=0.1)
    while zana<cishu:
        sleep(xjg)
        swipe([0.13*we,0.8*hi],vector=(-0.5,0),duration=0.1)
        zana+=1

def ruchanga(zhangjie):
    sleep(hsjg)
    if zhangjie==1:
        touch([0.16*we,0.50*hi])
    elif zhangjie==2:
        touch([0.4*we,0.4*hi])
    elif zhangjie==3:
        touch([0.6*we,0.43*hi])
    elif zhangjie==4:
        touch([0.84*we,0.46*hi])
#入场
def ruchang(dixia=0):
    sleep(hsjg)
    touch([0.840*we,0.400*hi])
    sleep(xjg)
    if dixia==1:
        touch([0.235*we,0.913*hi])
    elif dixia==2:
        touch([0.365*we,0.916*hi])        
    elif dixia==3:
        touch([0.487*we,0.916*hi])

def yizhijiexi():
    sleep(5)
    ruchang(1)
    #选关
    sleep(xjg)
    touch([0.26*we,0.48*hi])
    sleep(xjg)
    touch([0.33*we,0.82*hi])
    #开始行动
    sleep(xjg)
    touch([0.8*we,0.83*hi])
    wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
    sleep(xjg)
    touch([0.8*we,0.9*hi])
    wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
    touch([0.4*we,0.2*hi])
    zhuye()
    
def weichen():
    sleep(5)
    ruchang(1)
    #选关
    sleep(xjg)
    touch([0.26*we,0.48*hi])
    sleep(xjg)
    touch([0.33*we,0.82*hi])
    #开始行动
    sleep(xjg)
    touch([0.8*we,0.83*hi])
    wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
    sleep(xjg)
    touch([0.8*we,0.9*hi])
    wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
    touch([0.4*we,0.2*hi])
    zhuye()

def lichi():
    sleep(5)
    ruchang(1)
    #选关
    sleep(xjg)
    touch([0.65*we,0.45*hi])
    sleep(xjg)
    touch([0.33*we,0.82*hi])
    #开始行动
    sleep(xjg)
    touch([0.8*we,0.83*hi])
    wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
    sleep(xjg)
    touch([0.8*we,0.9*hi])
    wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
    touch([0.4*we,0.2*hi])
    zhuye()
    
def huangyuan():
    sleep(hsjg)
    touch([0.8*we,0.55*hi])
    wait(Template(r"tpl1696865573680.png", record_pos=(-0.387, -0.246), resolution=(1600, 900)),200)
    touch([0.41*we,0.22*hi])
    sleep(xjg)
    touch([0.584*we,0.157*hi])
    sleep(xjg)
    touch([0.04*we,0.289*hi])
    zhuye()
    
def renwu():
    sleep(hsjg)
    touch(Template(r"tpl1697122406176.png", record_pos=(-0.438, -0.069), resolution=(1600, 900)))
    #touch([0.06*we,0.37*hi])
    sleep(xjg)
    touch([0.68*we,0.09*hi])
    sleep(xjg)
    touch([0.92*we,0.2*hi])
    sleep(xjg)
    touch([0.06*we,0.37*hi])
    sleep(xjg)
    
    touch([0.85*we,0.08*hi])
    sleep(xjg)
    touch([0.92*we,0.2*hi])
    sleep(xjg)
    touch([0.06*we,0.37*hi])
    sleep(xjg)
    zhuye()
    
def cailiao(canshu):
        if canshu==1:#金爪灵摆
            sleep(hsjg)
            ruchang()
            ruchanga(3)
            #滑动
            zhuadong(1)
            sleep(xjg)
            touch(Template(r"tpl1697119680467.png", record_pos=(-0.069, 0.177), resolution=(1600, 900)))
            #调次数刷
            sleep(xjg)
            touch([0.85*we,0.37*hi])
            sleep(xjg)
            touch([0.8*we,0.84*hi])
            wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
            sleep(xjg)
            touch([0.49*we,0.91*hi])
            sleep(xjg)
            touch([0.65*we,0.91*hi])
            sleep(xjg)
            touch([0.648*we,0.578*hi])
            sleep(xjg)
            touch([0.8*we,0.89*hi])
            wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
            touch([0.4*we,0.2*hi])
            zhuye()
        elif canshu==2:#啃咬盒
            sleep(hsjg)
            ruchang()
            ruchanga(4)
            #滑动
            zhuadong(2)
            sleep(xjg)
            touch(Template(r"tpl1697119789679.png", record_pos=(-0.113, 0.172), resolution=(1600, 900)))
            #调次数刷
            sleep(xjg)
            touch([0.85*we,0.37*hi])
            sleep(xjg)
            touch([0.8*we,0.84*hi])
            wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
            sleep(xjg)
            touch([0.49*we,0.91*hi])
            sleep(xjg)
            touch([0.65*we,0.91*hi])
            sleep(xjg)
            touch([0.648*we,0.578*hi])
            sleep(xjg)
            touch([0.8*we,0.89*hi])
            wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
            touch([0.4*we,0.2*hi])
            zhuye()
        elif canshu==3:#鸟
            sleep(hsjg)
            ruchang()
            ruchanga(3)
            #滑动
            zhuadong(1)
            sleep(xjg)
            touch(Template(r"tpl1697119545488.png", record_pos=(-0.096, 0.179), resolution=(1600, 900)))
            #调次数刷
            sleep(xjg)
            touch([0.85*we,0.37*hi])
            sleep(xjg)
            touch([0.8*we,0.84*hi])
            wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
            sleep(xjg)
            touch([0.49*we,0.91*hi])
            sleep(xjg)
            touch([0.65*we,0.91*hi])
            sleep(xjg)
            touch([0.648*we,0.578*hi])
            sleep(xjg)
            touch([0.8*we,0.89*hi])
            wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
            touch([0.4*we,0.2*hi])
            zhuye()
        elif canshu==4:#曼德拉
            sleep(hsjg)
            ruchang()
            ruchanga(3)
            #滑动
            zhuadong(1)
            yhuadong(1)
            sleep(xjg)
            touch(Template(r"tpl1697120517331.png", record_pos=(-0.07, 0.176), resolution=(1600, 900)))
            #调次数刷
            sleep(xjg)
            touch([0.85*we,0.37*hi])
            sleep(xjg)
            touch([0.8*we,0.84*hi])
            wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
            sleep(xjg)
            touch([0.49*we,0.91*hi])
            sleep(xjg)
            touch([0.65*we,0.91*hi])
            sleep(xjg)
            touch([0.648*we,0.578*hi])
            sleep(xjg)
            touch([0.8*we,0.89*hi])
            wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
            touch([0.4*we,0.2*hi])
            zhuye()
        elif canshu==5:#秘银
            sleep(hsjg)
            ruchang()
            ruchanga(3)
            #滑动
            zhuadong(1)
            sleep(xjg)
            touch(Template(r"tpl1697121391808.png", record_pos=(-0.276, 0.176), resolution=(1600, 900)))
            #调次数刷
            sleep(xjg)
            touch([0.85*we,0.37*hi])
            sleep(xjg)
            touch([0.8*we,0.84*hi])
            wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
            sleep(xjg)
            touch([0.49*we,0.91*hi])
            sleep(xjg)
            touch([0.65*we,0.91*hi])
            sleep(xjg)
            touch([0.648*we,0.578*hi])
            sleep(xjg)
            touch([0.8*we,0.89*hi])
            wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
            touch([0.4*we,0.2*hi])
            zhuye()
        elif canshu==6:#骨架
            sleep(hsjg)
            ruchang()
            ruchanga(3)
            #滑动
            zhuadong(2)
            yhuadong(1)
            sleep(xjg)
            touch(Template(r"tpl1697121565145.png", record_pos=(-0.077, 0.181), resolution=(1600, 900)))
            #调次数刷
            sleep(xjg)
            touch([0.85*we,0.37*hi])
            sleep(xjg)
            touch([0.8*we,0.84*hi])
            wait(Template(r"tpl1697110307176.png", record_pos=(0.329, 0.23), resolution=(1600, 900)),cjg)
            sleep(xjg)
            touch([0.49*we,0.91*hi])
            sleep(xjg)
            touch([0.65*we,0.91*hi])
            sleep(xjg)
            touch([0.648*we,0.578*hi])
            sleep(xjg)
            touch([0.8*we,0.89*hi])
            wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
            touch([0.4*we,0.2*hi])
            zhuye()
            
def huodong():
    sleep(hsjg)
    touch([0.81*we,0.304*hi])
    sleep(hsjg)
    touch([0.83*we,0.79*hi])
    sleep(xjg)
    touch([0.345*we,0.813*hi])
    sleep(xjg)
    touch([0.8*we,0.855*hi])
    sleep(xjg)
    touch([0.8*we,0.905*hi])
    wait(Template(r"tpl1696846705026.png", record_pos=(0.052, 0.181), resolution=(1600, 900)),200)
    touch([0.4*we,0.2*hi])
    zhuye()
    
def xuanze(xuans):
    if xuans==1:
        cailiao(1)
    elif xuans==2
        cailiao(2)
    elif xuans==3:
        cailiao(3)
    elif xuans==4:
        cailiao(4)
    elif xuans==5:
        cailiao(5)
    elif xuans==6:
        cailiao(6)
    elif xuans==7:
        weichen()
    elif xuans==8:
        lichi()
    elif xuans==9:
def dgxh():
    
def kaishua():
        #poco(text="重返未来：1999").click()
        ruk=exists(Template(r"tpl1696860366382.png", record_pos=(0.002, -0.122), resolution=(1600, 900)))
        zy=exists(Template(r"tpl1697029665047.png", record_pos=(0.327, 0.111), resolution=(1600, 900)))
        if ruk:
            touch(ruk)
            sleep(30)
            chongshi=exists(Template(r"tpl1696864897608.png", record_pos=(0.128, 0.082), resolution=(1600, 900)))
            while chongshi:
                touch([0.63*we,0.64*hi],times=2)
                sleep(10)
                chongshi=exists(Template(r"tpl1696864897608.png", record_pos=(0.128, 0.082), resolution=(1600, 900)))
                sleep(10)
            tishi=exists(Template(r"tpl1696845772281.png", record_pos=(-0.448, 0.214), resolution=(1600, 900)))
            while tishi==False:
                tishi=exists(Template(r"tpl1696845772281.png", record_pos=(-0.448, 0.214), resolution=(1600, 900)))
            if tishi:
                touch([0.504*we,0.746*hi],times=2)
            else:
                touch([0.917*we,0.153*hi],times=2)
                sleep(1)
                touch([0.504*we,0.746*hi],times=2)
            sleep(15)
            diyici=exists(Template(r"tpl1696893306720.png", record_pos=(-0.149, -0.169), resolution=(1600, 900)))
        
            if diyici:
                touch([0.654*we,0.3*hi],times=2)
                sleep(3)
                touch([0.654*we,0.3*hi],times=2)
                sleep(3)
                touch([0.654*we,0.3*hi],times=2)
                sleep(3)
                yizhijiexi()
                xuanze(sjs)
                huangyuan()
                renwu()
            else :
                xuanze(sjs)
                huangyuan()
                renwu()
        elif zy:
            #yizhijiexi()
            xuanze(sjs)
            huangyuan()
            renwu()
kaishua()
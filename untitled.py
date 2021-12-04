# -*- encoding=utf8 -*-
__author__ = "眭"

from airtest.core.api import *
import fengyao
import time
import disha
import chenxing
import hall

auto_setup(__file__)

last_yaowang_start_time = 20;

localtime = time.localtime(time.time())
if localtime.tm_wday == 2 or localtime.tm_wday == 5:
    keju = 0
    xiangshi = 0
    huishi = 0
    dianshi = 0

wangyang_jieshu = 0
while 1:
    localtime = time.localtime(time.time())
    hour = localtime.tm_hour
    min = localtime.tm_min
    if hour % 2 == 0 and min == 30:
        #地煞
        disha.start()
    
    if not wangyang_jieshu and min > 0 and min < 20 and min < last_yaowang_start_time:
        #封妖
        wangyang_jieshu = fengyao.start()
        last_yaowang_start_time = 1
        
    if not wangyang_jieshu and min > 40 and min < 50 and min > last_yaowang_start_time:
        #封妖
        wangyang_jieshu = fengyao.start()
        last_yaowang_start_time = 50
        
    if hour == 11 and min == 20 or hour == 11 and last_yaowang_start_time == 1:
        #开启飞贼
        hall.dianji_feizei()
        
    if hour == 19 and min == 20 or hour == 19 and last_yaowang_start_time == 1:
        #校场演兵
        hall.jiaochang_yanbing()
        
    if hour == 11 and min == 55 or hour == 19 and min == 55:
        #小龟赛跑
        hall.dianji_xiaogui()
    
    if hour == 1:
        #辰星
        chenxing.start()
        
    if keju:
        if hour > 11 and not xiangshi and hall.xiangshi():
            print("------------------已完成乡试")
            #乡试
            xiangshi = 1
        elif hour == 21 and not huishi and hall.xiangshi():
            print("------------------已完成会试")
            #会试
            huishi = 1
        elif hour == 21 and min == 5 and not dianshi and hall.xiangshi():
            print("------------------已完成殿试")
            #殿试
            dianshi = 1
            
    
    if hour % 2 == 0 and min == 29:
        sleep(1.0)
    else:
        sleep(60.0)




# fengyao.start()
#封妖
# fengyao.fengyao()

# disha.start()
# chenxing.start()

# if exists(Template(r"tpl1638586068389.png", record_pos=(0.003, 0.291), resolution=(547, 974))):
#     print("-----------------------")



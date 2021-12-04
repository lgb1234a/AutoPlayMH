# -*- encoding=utf8 -*-
__author__ = "眭"

from airtest.core.api import *
import random

def dianji_chucheng():
    touch(Template(r"tpl1638596981318.png", record_pos=(-0.248, 0.788), resolution=(547, 974)))

    
def dianji_fengyao():
    touch(Template(r"tpl1638581777557.png", record_pos=(0.299, 0.521), resolution=(548, 975)))

    
def dianji_feizei():
    touch(Template(r"tpl1638586473161.png", record_pos=(-0.412, 0.786), resolution=(547, 974)))
    touch(Template(r"tpl1638586500146.png", record_pos=(-0.425, -0.603), resolution=(547, 974)))
    
def jiaochang_yanbing():
    touch(Template(r"tpl1638586473161.png", record_pos=(-0.412, 0.786), resolution=(547, 974)))
    touch(Template(r"tpl1638604435734.png", record_pos=(-0.425, -0.596), resolution=(548, 975)))



def dianji_xiaogui():
    touch(Template(r"tpl1638589887447.png", record_pos=(-0.41, 0.781), resolution=(547, 974)))
    touch(Template(r"tpl1638589909358.png", record_pos=(-0.292, -0.596), resolution=(547, 974)))
    touch(Template(r"tpl1638590153321.png", record_pos=(-0.003, 0.077), resolution=(547, 974)))
    touch(Template(r"tpl1638590164340.png", record_pos=(0.003, 0.282), resolution=(547, 974)))
    touch(Template(r"tpl1638590172115.png", record_pos=(0.182, -0.097), resolution=(547, 974)))
    touch(Template(r"tpl1638590180940.png", record_pos=(0.187, 0.256), resolution=(547, 974)))
    touch(Template(r"tpl1638590263853.png", record_pos=(0.394, 0.419), resolution=(547, 974)))
    touch(Template(r"tpl1638590272959.png", record_pos=(0.317, -0.254), resolution=(547, 974)))
    touch(Template(r"tpl1638590281753.png", record_pos=(0.42, 0.313), resolution=(547, 974)))


def _touchRandomPoint(count):
    if count % 4 == 1:
        touch((100, 600))
        sleep(2.0)
    
    if count % 4 == 2:
        touch((400, 600))
        sleep(2.0)
        
    if count % 4 == 3:
        touch((100, 700))
        sleep(2.0)
    
    if count % 4 == 0:
        touch((400, 700))
        sleep(2.0)

def xiangshi():
    touch(Template(r"tpl1638594917694.png", record_pos=(-0.409, 0.786), resolution=(547, 974)))
    if exists(Template(r"tpl1638594932820.png", record_pos=(-0.165, -0.601), resolution=(547, 974))):
        touch(Template(r"tpl1638594942076.png", record_pos=(-0.162, -0.594), resolution=(547, 974)))
        if exists(Template(r"tpl1638595860684.png", record_pos=(0.383, 0.537), resolution=(547, 974))):
            touch(Template(r"tpl1638595938499.png", record_pos=(0.396, 0.536), resolution=(547, 974)))

            return 1

        touch(Template(r"tpl1638594950067.png", record_pos=(0.324, 0.642), resolution=(547, 974)))
        
        
        count = 1
        while not exists(Template(r"tpl1638595393507.png", record_pos=(0.385, 0.528), resolution=(547, 974))):
            _touchRandomPoint(count)
            count = count + 1

        
        touch(Template(r"tpl1638595401399.png", record_pos=(0.392, 0.53), resolution=(547, 974)))
        return 1
    return 0


# -*- encoding=utf8 -*-
__author__ = "眭"

from airtest.core.api import *
import hall


def start():
    hall.dianji_chucheng()
    hall.dianji_fengyao()
    touch(Template(r"tpl1638582742924.png", record_pos=(-0.211, 0.633), resolution=(547, 974)))

    attack_190()

def attack_190():
    if exists(Template(r"tpl1638601755485.png", record_pos=(-0.077, -0.661), resolution=(548, 975))):
        return 1
    
    
    
    swipe(Template(r"tpl1638582640978.png", record_pos=(-0.074, -0.508), resolution=(547, 974)), vector=[0.4973, -0.0092])
    swipe(Template(r"tpl1638582774594.png", record_pos=(-0.012, -0.373), resolution=(547, 974)), vector=[0.3656, -0.0205])

    swipe(Template(r"tpl1638583517375.png", record_pos=(-0.37, -0.194), resolution=(547, 974)), vector=[0.5978, -0.0133])

    if exists(Template(r"tpl1638583403162.png", record_pos=(-0.215, -0.099), resolution=(547, 974))):
        touch(Template(r"tpl1638583403162.png", record_pos=(-0.215, -0.099), resolution=(547, 974)))
        touch(Template(r"tpl1638583452992.png", record_pos=(0.352, 0.492), resolution=(547, 974)))
        if exists(Template(r"tpl1638583564874.png", record_pos=(0.003, 0.329), resolution=(547, 974))):
            touch(Template(r"tpl1638583582717.png", record_pos=(-0.001, 0.327), resolution=(547, 974)))
        sleep(20.0)
        touch((288, 95), times=2)
        
        
    if exists(Template(r"tpl1638584290412.png", record_pos=(-0.114, -0.417), resolution=(547, 974))):

        touch(Template(r"tpl1638584290412.png", record_pos=(-0.114, -0.417), resolution=(547, 974)))
        touch(Template(r"tpl1638583452992.png", record_pos=(0.352, 0.492), resolution=(547, 974)))
        if exists(Template(r"tpl1638583564874.png", record_pos=(0.003, 0.329), resolution=(547, 974))):
            touch(Template(r"tpl1638583582717.png", record_pos=(-0.001, 0.327), resolution=(547, 974)))    
        sleep(20.0)
        touch((288, 95), times=2)
        
    if exists(Template(r"tpl1638584328859.png", record_pos=(-0.229, 0.097), resolution=(547, 974))):
    
        touch(Template(r"tpl1638584328859.png", record_pos=(-0.229, 0.097), resolution=(547, 974)))
        touch(Template(r"tpl1638583452992.png", record_pos=(0.352, 0.492), resolution=(547, 974)))
        if exists(Template(r"tpl1638583564874.png", record_pos=(0.003, 0.329), resolution=(547, 974))):
            touch(Template(r"tpl1638583582717.png", record_pos=(-0.001, 0.327), resolution=(547, 974)))    
        sleep(15.0)
        touch((288, 95), times=2)
    
    if exists(Template(r"tpl1638584344500.png", record_pos=(0.001, -0.166), resolution=(547, 974))):
        touch(Template(r"tpl1638584344500.png", record_pos=(0.001, -0.166), resolution=(547, 974)))
        touch(Template(r"tpl1638583452992.png", record_pos=(0.352, 0.492), resolution=(547, 974)))
        if exists(Template(r"tpl1638583564874.png", record_pos=(0.003, 0.329), resolution=(547, 974))):
            touch(Template(r"tpl1638583582717.png", record_pos=(-0.001, 0.327), resolution=(547, 974)))    
        sleep(15.0)
        touch((288, 95), times=2)
    
    if exists(Template(r"tpl1638584356727.png", record_pos=(-0.164, -0.457), resolution=(547, 974))):
        touch(Template(r"tpl1638584356727.png", record_pos=(-0.164, -0.457), resolution=(547, 974)))
        touch(Template(r"tpl1638583452992.png", record_pos=(0.352, 0.492), resolution=(547, 974)))
        if exists(Template(r"tpl1638583564874.png", record_pos=(0.003, 0.329), resolution=(547, 974))):
            touch(Template(r"tpl1638583582717.png", record_pos=(-0.001, 0.327), resolution=(547, 974)))    
        sleep(10.0)
        touch((288, 95), times=2)
    
    if exists(Template(r"tpl1638584367106.png", record_pos=(0.005, 0.097), resolution=(547, 974))):
        touch(Template(r"tpl1638584367106.png", record_pos=(0.005, 0.097), resolution=(547, 974)))
        touch(Template(r"tpl1638583452992.png", record_pos=(0.352, 0.492), resolution=(547, 974)))
        if exists(Template(r"tpl1638583564874.png", record_pos=(0.003, 0.329), resolution=(547, 974))):
            touch(Template(r"tpl1638583582717.png", record_pos=(-0.001, 0.327), resolution=(547, 974)))    
        sleep(10.0)
        touch((288, 95), times=2)
    
    if exists(Template(r"tpl1638584375782.png", record_pos=(-0.149, -0.196), resolution=(547, 974))):
        touch(Template(r"tpl1638584375782.png", record_pos=(-0.149, -0.196), resolution=(547, 974)))
        touch(Template(r"tpl1638583452992.png", record_pos=(0.352, 0.492), resolution=(547, 974)))
        sleep(10.0)
        touch((288, 95), times=2)
    return 0

def fengyao():
    hall.dianji_chucheng()
    hall.dianji_fengyao()
    touch(Template(r"tpl1638592496845.png", record_pos=(0.324, -0.472), resolution=(547, 974)))
    touch(Template(r"tpl1638592503477.png", record_pos=(0.259, 0.325), resolution=(547, 974)))
    touch(Template(r"tpl1638592563937.png", record_pos=(-0.003, 0.32), resolution=(547, 974)))


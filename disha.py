# -*- encoding=utf8 -*-
__author__ = "眭"

from airtest.core.api import *
import hall


def start():
    hall.dianji_chucheng()
    hall.dianji_fengyao()
    touch(Template(r"tpl1638583820532.png", record_pos=(-0.036, 0.631), resolution=(547, 974)))
    if exists(Template(r"tpl1638583912512.png", record_pos=(-0.288, -0.428), resolution=(547, 974))):
        touch(Template(r"tpl1638585021910.png", record_pos=(0.33, -0.411), resolution=(547, 974)))


#     if exists(Template(r"tpl1638584144616.png", record_pos=(-0.284, -0.122), resolution=(547, 974))):
#         touch(Template(r"tpl1638585021910.png", record_pos=(0.33, -0.411), resolution=(547, 974)))
    
    if exists(Template(r"tpl1638584153570.png", record_pos=(-0.288, 0.172), resolution=(547, 974))):
        touch((460,620))
        

    


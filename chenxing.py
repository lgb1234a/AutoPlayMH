# -*- encoding=utf8 -*-
__author__ = "眭"

from airtest.core.api import *
import hall

def start():
    hall.dianji_chucheng()
    hall.dianji_fengyao()
    touch(Template(r"tpl1638585962563.png", record_pos=(0.136, 0.631), resolution=(547, 974)))
    zhu()


def ji():
    if exists(Template(r"tpl1638585979462.png", record_pos=(-0.416, -0.186), resolution=(547, 974))):
        touch(Template(r"tpl1638585991382.png", record_pos=(-0.414, -0.194), resolution=(547, 974)))
        touch(Template(r"tpl1638586003486.png", record_pos=(0.337, 0.472), resolution=(547, 974)))
        if exists(Template(r"tpl1638586068389.png", record_pos=(0.003, 0.291), resolution=(547, 974))):

            touch(Template(r"tpl1638586053865.png", record_pos=(-0.001, 0.293), resolution=(547, 974)))
            sleep(600)
        else:
            touch(Template(r"tpl1638586248288.png", record_pos=(0.432, 0.293), resolution=(547, 974)))
            touch(Template(r"tpl1638586331957.png", record_pos=(0.22, 0.101), resolution=(547, 974)))
            if exists(Template(r"tpl1638586397739.png", record_pos=(0.006, -0.505), resolution=(547, 974))):
                touch(Template(r"tpl1638586405074.png", record_pos=(-0.001, 0.243), resolution=(547, 974)))


            
def gou():
    if exists(Template(r"tpl1638586160661.png", record_pos=(0.021, -0.19), resolution=(547, 974))):
        touch(Template(r"tpl1638586160661.png", record_pos=(0.021, -0.19), resolution=(547, 974)))
        touch(Template(r"tpl1638586003486.png", record_pos=(0.337, 0.472), resolution=(547, 974)))
        if exists(Template(r"tpl1638586068389.png", record_pos=(0.003, 0.291), resolution=(547, 974))):
            touch(Template(r"tpl1638586053865.png", record_pos=(-0.001, 0.293), resolution=(547, 974)))
            sleep(600)
        else:
            touch(Template(r"tpl1638586248288.png", record_pos=(0.432, 0.293), resolution=(547, 974)))
            touch(Template(r"tpl1638586331957.png", record_pos=(0.22, 0.101), resolution=(547, 974)))
            if exists(Template(r"tpl1638586397739.png", record_pos=(0.006, -0.505), resolution=(547, 974))):
                touch(Template(r"tpl1638586405074.png", record_pos=(-0.001, 0.243), resolution=(547, 974)))

def zhu():
    if exists(Template(r"tpl1638600269239.png", record_pos=(0.308, -0.032), resolution=(548, 975))):
        touch(Template(r"tpl1638600269239.png", record_pos=(0.308, -0.032), resolution=(548, 975)))
        touch(Template(r"tpl1638586003486.png", record_pos=(0.337, 0.472), resolution=(547, 974)))
        if exists(Template(r"tpl1638586068389.png", record_pos=(0.003, 0.291), resolution=(547, 974))):
            touch(Template(r"tpl1638586053865.png", record_pos=(-0.001, 0.293), resolution=(547, 974)))
            sleep(600)
        else:
            touch(Template(r"tpl1638586248288.png", record_pos=(0.432, 0.293), resolution=(547, 974)))
            touch(Template(r"tpl1638586331957.png", record_pos=(0.22, 0.101), resolution=(547, 974)))
            if exists(Template(r"tpl1638586397739.png", record_pos=(0.006, -0.505), resolution=(547, 974))):
                touch(Template(r"tpl1638586405074.png", record_pos=(-0.001, 0.243), resolution=(547, 974)))


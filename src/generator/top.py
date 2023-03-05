#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Infinite Music Discs datapack + resourcepack generator module
#Generation tool, datapack design, and resourcepack design by link2_thepast

from src.generator.v1 import GeneratorV1
from src.generator.v2 import GeneratorV2

def get_generator(user_settings: dict):
    if(user_settings.get('dp_version', False)):
        return GeneratorV1()
    else:
        return GeneratorV2()



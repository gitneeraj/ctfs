#!/usr/bin/env python3

from wand.image import Image

with Image(filename='kiddie_pool.png') as img:
    img.swirl(degree=-900)
    img.save(filename='fx-swirl.png')


# flag{whirlpool_in_a_cinch}
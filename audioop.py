# SPDX-FileCopyrightText: © 2024 Shaun Wilson
# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
#
# audioop.py
#
# Copyright (C) Shaun Wilson, all rights reserved.
# This code is dual-licensed under MIT License and
# Python Software Foundation License 2.0
#
# If used in whole or in part under the MIT License
# the Copyright notice must be retained.
#
# This is a stub module to allow `discord.py`
# to work in python 3.13 or later. Ultimately
# "it can't be in Python because this is
# low latency" is just an impertinent excuse
# to hold everyone hostage, either that or
# "sounds like a skill issue."
#
# Proceed to seething and writhing. I'm used to it, and DGAF.
#
# type: ignore
##

__clamp = [0] + [((1<<(v*8))>>1)-1 for v in range(1,5)]
def mul(fragment:bytes, width:int, factor:float):
    global __clamp
    hi = __clamp[width]
    lo = -hi
    k = bytearray(len(fragment))
    for i in range(0, len(fragment), width):
        v:float = factor * int.from_bytes(fragment[i:i+width], 'little', signed = True)
        if v < lo:
            v = lo
        elif v > hi:
            v = hi
        r = int.to_bytes(int(v), width, 'little', signed = True)
        for j in range(width):
            k[i+j] = r[j]
    return bytes(k)
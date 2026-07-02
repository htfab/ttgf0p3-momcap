#!/usr/bin/env python3

WIDTH = 612
HEIGHT = 562

magic_file = f"""
magic
tech gf180mcuD
magscale 1 5
timestamp 1782900000

use metal_stack  metal_stack_0
array 0 {HEIGHT-1} 56 0 0 112
timestamp 1782900000
transform 0 -1 28 1 0 0
box 0 0 84 28

use metal_stack  metal_stack_1
array 0 {HEIGHT-1} 56 0 0 112
timestamp 1782900000
transform 0 -1 {28*(2*WIDTH+1)} 1 0 0
box 0 0 84 28

use metal_stack  metal_stack_2
array 0 {WIDTH-2} 56 0 {HEIGHT//2} 112
timestamp 1782900000
transform 1 0 0 0 1 0
box 0 0 84 28

use metal_stack  metal_stack_3
array 0 {WIDTH-2} 56 0 {(HEIGHT-1)//2} 112
timestamp 1782900000
transform 1 0 56 0 1 56
box 0 0 84 28

use via_stack  via_stack_0
array 0 {(HEIGHT-2)//2} 112 0 0 112
timestamp 1782900000
transform 0 -1 28 1 0 {84 if HEIGHT%2 == 1 else 56}
box -14 0 42 28

use via_stack  via_stack_1
array 0 {(HEIGHT-2)//2} 112 0 0 112
timestamp 1782900000
transform 0 -1 {28*(2*WIDTH+1)} 1 0 {84 if HEIGHT%2 == 1 else 56}
box -14 0 42 28

use via_stack  via_stack_2
array 0 {(WIDTH-5)//2} 112 0 {(HEIGHT)//2} 112
timestamp 1782900000
transform 1 0 168 0 1 0
box -14 0 42 28

use via_stack  via_stack_3
array 0 {(WIDTH-4)//2} 112 0 {(HEIGHT-1)//2} 112
timestamp 1782900000
transform 1 0 112 0 1 56
box -14 0 42 28

<< end >>
"""

print(magic_file.replace("\n\n", "\n").strip())


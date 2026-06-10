#!/usr/bin/env python3

WIDTH = 612
HEIGHT = 562

print("""magic
tech gf180mcuD
magscale 1 5
timestamp 1871000000""")

for layer in ("metal1", "via1", "metal2", "via2", "metal3", "via3", "metal4"):
    print(f"<< {layer} >>")

    if layer.startswith("metal"):
        print(f"rect 0 0 28 {28*(2*HEIGHT+1)}")
        print(f"rect {28*(2*WIDTH)} 0 {28*(2*WIDTH+1)} {28*(2*HEIGHT+1)}")
        for i in range(HEIGHT+1):
            if i % 2 == 0:
                print(f"rect 28 {28*(2*i)} {28*(2*WIDTH-1)} {28*(2*i+1)}")
            else:
                print(f"rect 56 {28*(2*i)} {28*(2*WIDTH)} {28*(2*i+1)}")

    elif layer == "via1":
        print(f"rect 1 6 27 {28*(2*HEIGHT+1)-6}")
        print(f"rect {28*(2*WIDTH)+1} 6 {28*(2*WIDTH+1)-1} {28*(2*HEIGHT+1)-6}")
        for i in range(HEIGHT+1):
            print(f"rect 62 {28*(2*i)+1} {28*(2*WIDTH-1)-6} {28*(2*i+1)-1}")

    elif layer.startswith("via"):
        print(f"rect 0 5 28 {28*(2*HEIGHT+1)-5}")
        print(f"rect {28*(2*WIDTH)} 5 {28*(2*WIDTH+1)} {28*(2*HEIGHT+1)-5}")
        for i in range(HEIGHT+1):
            print(f"rect 61 {28*(2*i)} {28*(2*WIDTH-1)-5} {28*(2*i+1)}")

    else:
        raise NotImplementedError

print("<< end >>")


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

    elif layer.startswith("via"):
        for j in range(HEIGHT+1):
            for i in range(WIDTH+1):
                if i == 1 or i == WIDTH-1:
                    continue
                if (i == 0 or i == WIDTH) and (j == 0 or j == HEIGHT):
                    continue
                if (i+j) % 2 == 0:
                    continue
                if layer == "via1":
                    print(f"rect {28*(2*i)+1} {28*(2*j)+1} {28*(2*i+1)-1} {28*(2*j+1)-1}")
                else:
                    print(f"rect {28*(2*i)} {28*(2*j)} {28*(2*i+1)} {28*(2*j+1)}")

    else:
        raise NotImplementedError

print("<< end >>")


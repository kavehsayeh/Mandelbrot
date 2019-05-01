import cmath
from PIL import Image, ImageDraw

def mandelbrot(c):
    maxIterations = 75
    z = 0
    i = 0
    while i < maxIterations:
        z = (abs(z.real) + abs(z.imag)*1j)**2 + c
        if abs(z) > 2:
            break
        i += 1
    if i == maxIterations:
        return True
    return False
        
im = Image.open(r"base.png").convert("RGBA")

xvalues = list(range(im.size[0]))
yvalues = list(range(im.size[1]))
points = []
for r in xvalues:
    for i in yvalues:
        points.append(((3*r/im.size[0] - 2) + (2*i/im.size[1] - 1)*1j, (r, i)))
print(len(xvalues), len(yvalues), len(points))

mask = Image.new('RGBA', im.size, (0,0,0,255))
d = ImageDraw.Draw(mask)

for z in points:
    if not mandelbrot(z[0]):
        d.point(z[1], fill=(255, 255, 255, 255))
out = Image.alpha_composite(im, mask)
out.save(r"fractal.png")

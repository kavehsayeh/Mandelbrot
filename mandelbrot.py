import cmath, numpy
from PIL import Image, ImageDraw

def mandelbrot(c, maxIterations):
    """
    The generating function to be used for the fractal. Returns the number of iterations it takes for the value to escape.
    """
    z = 0
    i = 0
    while i < maxIterations:
        z = z**2 + c
        if abs(z) > 2:
            break
        i += 1
    return i


def plot_fractal(res, bottom_left, top_right, maxIter):
    """
    Plots the fractal using PIL. res specifies the number of pixels per one unit. bottom_left and top_right are complex numbers specifying the corners of the image.
    """
    dim = (int(res * (top_right.real - bottom_left.real)),
           int(res * (top_right.imag - bottom_left.imag)))
    im = Image.new('RGBA', dim)

    xvalues = numpy.linspace(bottom_left.real, top_right.real, num=dim[0], retstep=True, endpoint=False)
    yvalues = numpy.linspace(bottom_left.imag, top_right.imag, num=dim[1], retstep=True, endpoint=False)

    xvalues_real = xvalues[0]
    xvalues_image = list(range(dim[0]))

    yvalues_real = yvalues[0]
    yvalues_image = list(range(dim[1]))

    print(xvalues_image)
    points_real = [x + y*1j for x in xvalues_real for y in yvalues_real]
    points_image = [(x, y) for x in xvalues_image for y in yvalues_image]
    points = zip(points_real, points_image)

    mask = Image.new('RGBA', dim, (0,0,0,255)) # creates a black base image
    d = ImageDraw.Draw(mask)

    for z in points:
        if mandelbrot(z[0], maxIter) != maxIter:
            d.point(z[1], fill=(255, 255, 255, 255))
            # if the point is not in the mandelbrot set, color it white
    out = Image.alpha_composite(im, mask)
    out.save(r"fractal.png")

if __name__ == '__main__':
    plot_fractal(1000, -2 - 1*1j, 1 + 1*1j, 75)

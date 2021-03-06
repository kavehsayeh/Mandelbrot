import numpy
from PIL import Image, ImageDraw

def mandelbrot(c, maxIterations):
    """
    The generating function to be used for the Mandelbrot set. Returns the 
    number of iterations it takes for the value to escape, or the maximum 
    number of iterations.
    """
    z = 0
    i = 0
    while i < maxIterations:
        z = z**2 + c
        if abs(z) > 2:
            break
        i += 1
    return i

def burning_ship(c, maxIterations):
    """
    The generating function to be used for the burning ship fractal. Returns 
    the number of iterations it takes for the value to escape, or the maximum 
    number of iterations.
    """
    z = 0
    i = 0
    while i < maxIterations:
        z = (complex(abs(z.real), abs(z.imag)))**2 + c
        if abs(z) > 2:
            break
        i += 1
    return i

def plot_fractal(res, bottom_left, top_right, maxIter, gen_func):
    """
    Plots the fractal using PIL. res specifies the number of pixels per one 
    unit. bottom_left and top_right are complex numbers specifying the corners 
    of the image. maxIter is the number of iterations to run the generating
    function.
    """
    dim = (int(res * (top_right.real - bottom_left.real)),
           int(res * (top_right.imag - bottom_left.imag)))

    xvalues = numpy.linspace(bottom_left.real, top_right.real, num=dim[0], 
    						 retstep=True, endpoint=False)
    yvalues = numpy.linspace(bottom_left.imag, top_right.imag, num=dim[1], 
    						 retstep=True, endpoint=False)

    xvalues_real = xvalues[0]
    xvalues_image = list(range(dim[0]))

    yvalues_real = yvalues[0]
    yvalues_image = list(range(dim[1]))

    points_real = [x + y*1j for x in xvalues_real for y in yvalues_real]
    points_image = [(x, y) for x in xvalues_image for y in yvalues_image]
    points = zip(points_real, points_image)

    mask = Image.new('L', dim, 0) # creates a black base image
    d = ImageDraw.Draw(mask)

    for z in points:
        test = gen_func(z[0], maxIter)
        if test != maxIter:
            d.point(z[1], fill=int(255*((maxIter - test) / maxIter)))
            # if the point is not in the fractal, color it white
    mask.save(r"fractal.tif")


if __name__ == '__main__':
    while True:
        fractal = input("Fractal: ")
        if fractal not in ('mandelbrot', 'burning_ship'):
            print("Invalid")
        else:
            break
    
    resolution = int(input("Resolution (pixels/unit): "))

    c1_r = float(input("Bottom left real: "))
    c1_i = float(input("Bottom left imaginary: "))
    c1 = complex(c1_r, c1_i)
    
    c2_r = float(input("Top right real: "))
    c2_i = float(input("Top right imaginary: "))
    c2 = complex(c2_r, c2_i)
    
    iterations = int(input("Iterations: "))

    plot_fractal(resolution, c1, c2, iterations, fractal)
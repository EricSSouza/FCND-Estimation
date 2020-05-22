import math;

def fmt(value):
    return "%.3f" % value

period = 4
radius = 0.5
timestep = 0.05
maxtime = period*6
z = -1

with open('NewSpiralNoFF.txt', 'w') as the_file:
    t=0;
    while t <= maxtime:
        x = math.sin(t * 2 * math.pi / period) * radius;
        y = math.cos(t * 2 * math.pi / period) * radius;
        the_file.write(fmt(t) + "," + fmt(x) + "," + fmt(y) + "," + fmt(z) + "\n");
        t += timestep;
        radius += 0.01;
        z -= 0.01

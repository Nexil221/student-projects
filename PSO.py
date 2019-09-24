import math
import random
import matplotlib.pyplot as plt

def rosenbrock(x):
    result = 0
    for i in range(size_of_problem-1):
        result = result + 100.0 * (x[i] ** 2.0 - x[i+1])**2.0 + (x[i] - 1)**2.0
    return result

def easom(x):
    result = -math.cos(x[0]) * math.cos(x[1]) * math.exp(-pow((x[0]-math.pi), 2) - pow((x[1] - math.pi), 2))
    return result


def griewank(xs):
    sum = 0
    for x in xs:
        sum += x * x
    product = 1
    for i in xrange(len(xs)):
        product *= math.cos(xs[i] / math.sqrt(i + 1))
    return 1 + sum / 4000 - product


max_iter = 1000
population_size = 30 # ilosc czastek
environment = 0.5 #wplyw srodowiska
inertia = 0.5  #bezwladnosc
personal_impact = 1
particles = list()
best_global = [600, 600]
all_particles = []


class particle:
    def __init__(self, position):
        self.position = position
        self.velocity = []
        self.best_local = position

        for i in range(size_of_problem):
            self.velocity.append(random.uniform(-1, 1))

    def update_velocity(self):
        for i in range(size_of_problem):
            random_value_one = random.random()
            random_value_two = random.random()

            velocity_one = random_value_one * personal_impact * (self.best_local[i] - self.position[i])
            velocity_two = random_value_two * environment * (best_global[i] - self.position[i])
            self.velocity[i] = inertia * self.velocity[i] + velocity_one + velocity_two

    def update_position(self):
        for i in range(size_of_problem):
            self.position[i] = self.position[i] + self.velocity[i]
        y = fun(self.position)
        # y = func1(self.position)
        if y < fun(self.best_local): #func1(self.best_local):
            self.best_local = self.position
            return self.position
        return self.position


def init_particles(domain):
    # ustaw best global
    global best_global
    all_particles = []
    for i in range(population_size):
        x = []
        # wylosuj pozycje
        # x1 = random.randint(domain[0][0], domain[0][-1])
        # x2 = random.randint(domain[0][0], domain[0][-1])
        for j in range(size_of_problem):
            x.append(random.randint(domain[0][0], domain[0][-1]))
        # ustaw best local
        best_local = x
        # przekaz  parametry do konstrktora particle:
        all_particles.append(particle(position= x ))
        if fun(best_local) < fun(best_global): #func1(best_local) < func1(best_global):
            best_global = best_local
    return all_particles



def search(all_particles):
    global best_global

    x = 0
    while x < max_iter:
        for particle in all_particles:
            particle.update_velocity()
            position = particle.update_position()
            # print ("check", particle)
            if fun(position) != None: #func1(position)
                if fun(position) < fun(best_global): #func1(position) < func1(best_global):
                    best_global = position
        print (best_global)
        plt.plot(best_global[0], best_global[1], 'x')
        plt.show()
        # plt.hist(best_global)
        x += 1



# def func1(x):
#     total = 0
#     for i in range(len(x)):
#         total += x[i]**2
#     return total

# bounds=[(-10,10),(-10,10)]
# all_particles_ = init_particles(bounds)
size_of_problem = 2 # wym problemu

rosenbrock_dom = []
griewank_dom = []
for i in range(size_of_problem):
    rosenbrock_dom.append(range(-5, 11))
    griewank_dom.append(range(-600, 601))
easom_dom = (range(-100, 101), range(-100, 101)) ## i=1,2

fun = griewank
dom = griewank_dom

all_particles_ = init_particles(dom)
search(all_particles_)


print(best_global)


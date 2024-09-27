import turtle

# screen settings

WIDTH, HEIGHT = 1920, 1080
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# turtle settings

tortol = turtle.Turtle()
tortol.pensize(3)
tortol.speed(0) 
tortol.setpos(-WIDTH // 3, -HEIGHT // 2)
tortol.color('gold')

# l-system settings

gens = 7
axiom = 'F'
chr_1, rule_1 = 'F', 'F-G+F+G-F'
chr_2, rule_2 = 'G', 'GG'
step = 8
angle = 120


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else 
                    rule_2 if chr == chr_2 else chr for chr in axiom]) 


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=("Arial", 60, "normal"))

axiom = get_result(gens, axiom)
for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        tortol.forward(step)
    elif chr == '+':
        tortol.right(angle)
    elif chr == '-':
        tortol.left(angle)



screen.exitonclick()
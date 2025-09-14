import turtle

def main():
    window = turtle.Screen()
    window.title("Langton\'s Ant")
    window.bgcolor("white")

    map = {}

    ant = turtle.Turtle()
    ant.shape("square")
    ant.fillcolor("black")
    ant.shapesize(0.5, 0.5, 0.5)
    ant.speed(10)
    ant.penup()

    step_size = 10.0

    while True:
        ant_pos = (round(ant.xcor()), round(ant.ycor()))
        if ant_pos not in map or map[ant_pos] == "white":
            ant.fillcolor("black")
            ant.stamp()
            map[ant_pos] = "black"
            ant.right(90)
            ant.forward(step_size)
        elif map[ant_pos] == "black":
            ant.fillcolor("white")
            ant.stamp()
            map[ant_pos] = "white"
            ant.left(90)
            ant.forward(step_size)


if __name__ == "__main__":
    main()
# Create an animation where a person is shocked
# after seeing a ghost

import turtle

BACKGROUND_DAY = "#FFFFFF"

# A person walking out during the day
screen = turtle.Screen()
screen.bgcolor(BACKGROUND_DAY)

# Person appears
pen = turtle.Turtle()
pen.hideturtle()
pen.up()
pen.setposition(-200, -150)
pen.down()

# Drawing the head
pen.circle(50)

# Drawing the girl's body as triangle
pen.setheading(250)
pen.forward(30)
right_arm_pos = pen.pos()  # Return position for right arm placement
print(right_arm_pos)
pen.forward(70)

pen.setheading(0)
pen.forward(20)
right_leg_pos = pen.pos()  # Right leg position
pen.forward(40)
left_leg_pos = pen.pos()  # Left leg position
pen.forward(20)

pen.setheading(110)
pen.forward(70)
left_arm_pos = pen.pos()  # Left arm position
pen.forward(30)

# Drawing the arm and hands
pen.up()
pen.setposition(right_arm_pos)
pen.setheading(145)
pen.down()
pen.forward(40)






turtle.done()



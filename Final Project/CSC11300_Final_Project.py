#Python final project (CSC11300)
#Contributors: Kartikeya Sharma, Denny Liang
import tkinter as tk
import turtle
import math
import Frequency_class as Frequency



def key_maxval(dic):  # return key of dictionary dic with max value, helper fucntion
    val = list(dic.values())
    key = list(dic.keys())
    return key[val.index(max(val))]

def draw():

    n_FrequentLetters = int(n) # stored global variable value into local variable: "n_FrequentLetters"

    t = turtle.RawTurtle(canvas)
    t.radians() # Since pie chart (Circle)

    angles = myFrequency.angle_dict.copy()  # copy of letter_angle dictionary we can safely alter

    # Color list to alternate turtle fill
    colors = ["blue", "orange", "purple", "black", "pink", "red",
              "brown", "navy", "cyan", "chocolate", "green", "tan",
              "violet", "b", "g", "c", "lime", "lightslategrey", "orchid",
              ]
    index = 0 # To help iterate through colors list
    radius = 100 # our pie chart radius
    total = 0
    label_radius = radius * 1.25  # radius to write labels too
    t.color(colors[index])  # initial color
    t.setpos(0, radius * -1)  # initial position of turtle
    while n_FrequentLetters >= 0:
        key = key_maxval(angles)  # save key of max value in angles dic

        t.fillcolor(colors[index])  # set slice color
        t.color(colors[index])  # set pen color
        if(index > 12):
            index = -1
        index += 1 # Move onto next color
        t.begin_fill() # Turtle instance to start filling pie chart

        if n_FrequentLetters == 0:  # final iteration uses 2pi - sum as the angle
            # draw final pie slice
            position = t.position()  # save position to draw next arc from
            t.circle(radius, 2 * math.pi - total)  # draw arc
            t.home()  # send turtle back to origin to create pie shape

            # label
            t.setheading(total - math.pi/2 + (2 * math.pi - total)/2)  # set direction of where label needs to be
            t.penup()
            t.forward(label_radius + 100)  # move turtle to label loaction
            t.write("All other letters" + ", " + str(round((2 * math.pi - total) / (2 * math.pi) * 100, 2)) + "%")
            t.home()
            t.pendown()

        else:
            # draw pie slice
            t.circle(radius, angles[key])  # draw arc
            position = t.position()  # save position to draw next arc from
            t.home()

            # label
            t.setheading(total - math.pi/2 + (angles[key] / 2))  # set direction of where label needs to be
            t.penup()
            t.forward(label_radius)  # move turtle to label location
            t.write(key + ", " + str(round((myFrequency.prob_dict[key] * 100), 2)) + "%")
            t.home()
            t.pendown()

        total = total + angles[key]
        t.end_fill()  # Fill pie slice with color to current color of turtle

        t.setpos(position) # Bring turtle back to position
        t.setheading(total) # Turn turtle head to correct direction

        angles.pop(key)  # After frequentWord has been used, it is removed from key. So letter doesn't repeat
        n_FrequentLetters = n_FrequentLetters - 1 # Decrement n_FrequentLetters


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=600, background='grey') # used tk.Canvas() object to set canvas
                                                                   # size for turtle to draw on
canvas.grid(column=0, row=3)

myFrequency = Frequency.Frequency() # uses Frequency() class to store most frequent letters in "myFrequency"

n = input("Enter desired n most frequent letters to display:") # Takes in user input for "n"
draw() # Once input has been taken in, draw is called to allow turtle to draw
root.mainloop() # To make sure that the turtle window doesn't automatically close after draw completion

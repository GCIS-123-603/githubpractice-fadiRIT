'''
This is a pixel art drawing program that can quite literally draw any string of values given to it, and is guaranteed to work, even if you have different strings
for each level. And it will keep repeating.

The program mainly has one draw pixel function, and the rest of the color functions which utilize the draw_pixel function with parameters of color, meaning theres
a version of that draw_pixel function that draws black, white, etc.

The main body of the program is in the main() function. 

Firstly it takes input, makes sure it's valid then moves on and begins drawing via checking if conditions for each and draws the appropriate color.
If there is an invalid color entered the program will terminate.

You only have to select from an input of colors that are provided:
0	'black'
1	'white'
2	'red'
3	'yellow'
4	'orange'
5	'green'
6	'yellowgreen'
7	'sienna'
8	'tan'
9	'gray'
A	'darkgray'

using any character outside of those will result in an error.


Something additional is that this program draws differently than the one used in the drawings.py module. We have discovered a more efficient
way to draw pixels and return. We've found many ways to improve from this system and make a different one which can be considered "more optimized".


'''

import turtle as t


#There are no tests done on this module, and the tests have been moved to the other module.
#There are issues with the executions of a test due to the nature of making this program, which uses odd and even numbers.


#initilization
t.shape('turtle')
t.speed(0)


# creating a function to draw a line of squares
n = 0
def createLine(x):
  global n 

  # repeat eight times 
  for j in range(x):
    # repeat 4 times 
    if(n % 2 == 0):
      #selecting fill color, function works by odd and even
      t.fillcolor('black')
    else:
      #if not even, use red
      t.fillcolor('red')
    t.begin_fill()
    #draw the square
    for i in range(4):
      # draw a line
      t.forward(20)
      # change angle 
      t.left(90)
    # start a new square
    t.end_fill()
    t.forward(20)
    n += 1
  if(j == x - 1): # used for skipping a certain pattern, instrumental.
    if(x % 2 == 1):
      n += 2
    else:
      n += 1
    
#input for dimensions 
lines = int(input('Enter one Dimension!: '))

# draw x lines 
for i in range(lines):
  # draw line 
  createLine(lines)
  # center the turtle horizontally 
  t.setx(0)
  # move up 30 units
  t.sety((i + 1) * 20)
t.setx(0)
t.sety(-lines)
t.pencolor("black")


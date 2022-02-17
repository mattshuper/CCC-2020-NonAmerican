# The first line of input will be an integer N with N ≥ 2. The second line will be the positive
# integer T where T < N2
# . The remaining input will be T lines, each representing the location
# of a single tree. The location is given by two positive integers, R and then C, separated by
# a single space. Each tree is located at row R and column C where rows are numbered from
# top to bottom from 1 to N and columns are numbered from left to right from 1 to N. No
# two trees are at the same location.

done = False
N = int(input())
T = int(input())
for x in range(0,T):
    x_axis,y_axis = [x for x in input().split()]
    x_axis = int(x_axis)
    y_axis = int(y_axis)

if (x_axis - 1) > (N - x_axis):
    width = (x_axis-1) 
if (x_axis - 1) < (N - x_axis):
    width = (N - x_axis)
if (x_axis - 1) == (N - x_axis):
    width = (N - x_axis)

if (y_axis - 1) > (N - y_axis):
    height = (y_axis-1) 
if (y_axis - 1) < (N - y_axis):
    height = (N - y_axis)
if (y_axis - 1) == (N - y_axis):
    height = (N - y_axis)


if height > width:
    if N/2 > (N-height):
        print(height)
    else:
        print(width)


else:
    if N/2 > (N-width):
        print(width)
    else:
        print(height)

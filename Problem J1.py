# The input consists of two lines.
# • The first line contains an integer R ≥ 0, representing the number of regular boxes.
# • The second line contains an integer S ≥ 0, representing the number of small boxes.

students = 28
regular = int(input())
small = int(input())

cupcakes = regular * 8 + small * 3
remaining = cupcakes - students
print(remaining)
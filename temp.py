import sys

if len(sys.argv) == 2:
    temp = float(sys.argv[1])
    print("User provided temperature:")
else:
    temp = 20.0
    print("No input given — using default temperature (20°C):")

if temp < 15:
    print("Cold")
elif 15 <= temp <= 30:
    print("Normal")
else:
    print("Hot")

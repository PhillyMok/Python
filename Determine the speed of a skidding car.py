## Determine the speed of a skidding car.
distance = float(input("Enter distance skidded (in feet): "))
speed = (24 * distance) ** .5
speed = round(speed, 2)
print("Estimated speed:", speed, "miles per hour")
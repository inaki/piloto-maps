import fileinput


array_of_points = []
for line in fileinput.input():
	if len(line) >= 6 and line[:6] == "<trkpt":
		parts = line.split('"')
		x = parts[1]
		y = parts[3]
		array_of_points.append((x, y))

print array_of_points
f = open("parsed-Lupulo.js", "w")

f.write("points = [")
for i in range(len(array_of_points)):
	item = array_of_points[i]
	f.write("(%s," % item[0])
	if i == len(array_of_points) - 1:
		f.write(" %s)]" % item[1])
	else:
		f.write(" %s), " % item[1])

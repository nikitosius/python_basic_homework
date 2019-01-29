# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
points = [(0, 0),  (4, 0),  (1, 3),  (5, 3)]
	
def get_midpoint(point1, point2):
	return ((point1[0] + point2[0])/2, (point1[1] + point2[1])/2)
	
def is_parallelogram(points):
midpoints = {}
P = 4 # 4 точки параллелограмма
for i in range(P):
	for j in range(P):
		if j <= i: continue
			midpoint = get_midpoint(points[i], points[j])
			if midpoint in midpoints:
				midpoints[midpoint] += 1
			else:
				midpoints[midpoint] = 1
				ones, twos = 0, 0
				for v in midpoints.values():
				if v == 1: ones += 1
				if v == 2: twos += 1
			return ones == 4 and twos == 1
		print(is_parallelogram(points))
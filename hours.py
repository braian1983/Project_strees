import time

hours_points = []

def Hours(range)
hours = range(1, 13) 
points = [5* h for in hours]
for h, p in zip (hours, points):
 print('hour %2i: %2i points' % (h, p))
 hours = range(6, 21)
 points = [10 * h for h in hours]
 for h, p in zip(hours, points):
  print('Hour %2i: %2i points' % (h, p))

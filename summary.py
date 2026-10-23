import sys
from collections import Counter
filename = sys.argv[1] # the first thing after the program name
position = int(sys.argv[2])# the position of the field to count

with open(filename) as f:
	lines = f.readlines()
print("Total lines:", len(lines))

counts = Counter()
for line in lines:
	fields = line.split()
	if len(fields) > int(position):
		key = fields[int(position)]
		counts[key] += 1
print("Top",position,":")
for item, n in counts.most_common(position):
	print(item, n)

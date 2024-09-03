import math

x = 8
y = 8
n =  8
section_root = int(math.sqrt(n))
for i in range(n):
    for j in range(n):
        section = (i // section_root) * section_root + (j // section_root)
        print(section, end=' ')
    print("\n")
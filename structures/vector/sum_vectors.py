# O(n)

v = [4, 5, 1]  # v = vector 1
w = [5, 3, 2]  # w = vector 2
sv = []  # sv = Sum of both vectors 1 and 2

s = 0  # sum itself

for i in range(len(v)):
    s += v[i] + w[i]
    sv.append(v[i] + w[i])

print(sv)
print(f"Sum of all vectors elements: {s}")

nombres = {3, 4, 2, 0, 2, 1, 3}

print(nombres)

try:
    print(nombres[2])
except TypeError:
    print("On ne peut pas acceder a un set avec des crochets")


nombres.add(5)
nombres.remove(3)
nombres.pop()

set_1 = {0, 1, 2}
set_2 = {2, 3, 4}

print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.difference(set_2))

print(dir(set_1))
print(help(set_1))

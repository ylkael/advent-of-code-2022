
# a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52

with open("03-rucksack/rucksacks_contents.txt") as file:
    contents = file.read()
    contents = contents.split("\n")
    for rucksack in contents:
        rucksack = rucksack.split("\n")
        rucksack = ' '.join(rucksack)
        print('rucksack:',rucksack)
        first_compartment = rucksack[:len(rucksack) // 2]
        print('first half:',first_compartment)
        second_compartment = rucksack[len(rucksack) // 2:]
        print('second half:',second_compartment)

    # contents = [int(i) for i in contents]
    # contents.sort()
    # contents.reverse()
    # print(contents)
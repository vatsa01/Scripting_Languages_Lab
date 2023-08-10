# Reverse 3 strings based on descending order of number of vowels in them.
l = []


class Reverse:
    def __init__(self, s):
        self.s = s

    def reverse(self):
        n = 0
        for i in self.s:
            if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'o' or i == 'O' or i == 'i' or i == 'I' or i == 'u' or i == 'U':
                n = n + 1

        r = ' '.join(reversed(self.s.split(' ')))
        tup = (n, r)
        l.append(tup)


for i in range(0, 3):
    x = str(input("Enter string :"))
    obj = Reverse(x)
    obj.reverse()
l.sort(reverse=True)
print(l)
for i in range(0, 3):
    print(l[i][1])

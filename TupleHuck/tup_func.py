
a = (4, 5, 2, 1, 7)

try:
    class Tuple:

        # Append new el
        def tup_append(a, x):
            a = list(a)
            a.append(x)
            a = tuple(a)
            return a

        # Delete the el in tuple
        def tup_del(a, x):
            a = list(a)
            for i in range(len(a)):
                if i == x:
                    a.pop(a[i])
                else:
                    continue
            a = tuple(a)
            return a

        # Change el in tuple
        def tup_change(a, x, y):
            a = list(a)
            for i in range(len(a)):
                if a[i] == x:
                    a[i] = y
            a = tuple(a)
            return a

        # Sort tuple with bubble sort method
        def tup_sort(a):
            a = list(a)
            n = len(a)
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if a[j] > a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]
            a = tuple(a)
            return a


except TypeError:
    print("TypeError")
except NameError:
    print("NameError")

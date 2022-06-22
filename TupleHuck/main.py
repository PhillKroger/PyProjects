from tup_func import *
from texts_inputs import *

t = Tuple

a = (3, 5, 7, 2, 2, 9)
print(out_t, a)

a = t.tup_append(a, 4)
print(append, a)

a = t.tup_change(a, 2, 5)
print(change, a)

a = t.tup_sort(a)
print(sort, a)

a = t.tup_del(a, 2)
print(del_t, a)
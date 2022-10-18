# Tuple 

# 1
from re import S


def func(ls,k):
    return  [ele for ele in ls if len(ele) != k]

# 2
def func2(tu):
    return tuple(set(tu))

# 3
def func3(s):
    res=[]
    for i in s:
        res.extend(i)
    return tuple(res)

# 4
def func4(s):
    res=[]
    for i in s:
        if not type(i) is tuple:
            res.append(i)
    return tuple(res)

# 5
def binary(s):
    sum = 0
    for i in range(len(s)):
        n = len(s) - 1
        sum += (s[i] * (2 ** (n-i)))
    return sum

# 6
def sort(tup):
    def count_digs(tup):
        return sum([len(str(ele)) for ele in tup ])
    tup.sort(key = count_digs)
    return tup

# Map

#1
def func(l1,l2,l3):
    map_obj = map(lambda x , y, z : x + y + z, l1,l2,l3)
    return list(map_obj)

# 2
def func2(ls):
    map_obj = map(lambda x: ' '.join(x),ls)
    return  list(map_obj)

# 3
def func3(l1,l2):
    map_obj = map(lambda x, y:(x+y , x-y),l1,l2)
    return  list(map_obj)

# 4
def fibonacci(count):
    sequence = [0, 1]

    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count)))

    return sequence[:count]

# print(fibonacci(10))

#5 
def intersect(l1,l2):
    result = list(filter(lambda x: x in l1, l2))
    return result

# 6
def pallindrome(ls):
    def func(s):
        i = 0
        while(i < len(s)//2):
            if (s[i] != s[len(s)-i-1]):
                return False
            i += 1
        return True
    result  = list(filter(lambda x : func(x) ,ls))
    return result

# print(pallindrome(['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']))

#7
def max_len(ls):
    max_l = max(len(x) for x in ls )   
    max_ls = max(ls, key = lambda i: len(i))    
    return (max_l, max_ls)
    
def min_len(ls):
    min_l = min(len(x) for x in ls )  
    min_ls = min(ls, key = lambda i: len(i))
    return (min_l, min_ls)
    
#8 
def triple(ls):
    obj = map(lambda x : 3 * x ,ls)
    return list(obj)

# list comprehension

# 1
def nested():
    ## 
    return [i  for i in range(1,1001) if any([1 for j in range(2,10) if i % j == 0])]

# 2
def new_list(ls):
    return [6 + num for num in ls]

# 3
def dict_comp(ls):
    return {num : num ** 3 for num in ls}

# 4
def map(ls1,ls2):
    return {ls1[i] : ls2[i] for i in range(len(ls1))}

# 5
def transpose(ls):
    return [[ls[j][i] for j in range(len(ls))]for i in range(len(ls[0])) ]

# 6
def function(s):
    return [i for i in s if i.isnumeric()]

# 7
def funct1(ls):
    return [i for i in ls if len(i) > 2 and i[-1] == 'b']

#8
def func_rev(ls):
    return [s[::-1] for s in ls]


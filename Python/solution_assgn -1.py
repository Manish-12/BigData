# List Solutions
# Q1

from operator import truediv
from re import S
import re


def sum_arr(arr,i,j):
    s = 0
    for k in range(i,j+1):
        s += arr[k]
    return s

# 2

def reverse(arr,i,j):
    while(i < j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1
    
def rotate_arr(arr,d):
    reverse(arr,0,d-1)
    reverse(arr,d,len(arr)-1)
    reverse(arr,0,len(arr) - 1)

    return arr

# 3
def second_most(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    fmax = 0
    smax = 0
    for k,v in d.items():
        if v > fmax:
            smax = fmax
            fmax = v
        elif v > smax and v != fmax:
            smax = v
    
    for k , v in d.items():
        if(v == smax):
            return k

    return ""


# 4
def differ(arr1,arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    return list(s1 - s2)

# 5
def printpositive(arr):
    for i in arr:
        if i >= 0:
            print(i, end = ",")
        

# 6
def flat(arr):
    out = []
    for i in arr:
        if (type(i) == list):
            out  += i
        else:
            out.append(i)
    return out

#7
def triplet(arr,s):
    arr.sort()

    for i in range(len(arr)-2):
        rem = s - arr[i]
        st = i+1
        end = len(arr) -1
        while(st < end):
            req = arr[st] + arr[end]

            if (req == rem):
                return [arr[i],arr[st],arr[end]]
            
            elif (req < rem):
                st += 1

            else:
                end -= 1
        
    return False

# String

# 1

# assuming small letters only
def missing(s):
    arr = [0]*26
    s = s.replace(' ','')
    for i in s:
        # technique to check ascii of character
        arr[ord(i) - 97] = 1
    
    for i in range(len(arr)):
        if (arr[i] == 0):
            print(chr(i + 97),end = "")

# 2
def totalnosubstring(s):
    l = len(s)
    return ((l+1)*l)/2


# 3
def sort(s):
    pass

# 4
def func(s):
    ls = s.split(", ")
    ls.sort()
    return ', '.join(ls)

# 5
def count(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

# 6
def least(s):
    from collections import Counter

    # counts hashable objects
    result= Counter(s)
    # equivalent to  min(d, key=lambda k: d[k])
    result= min(result, key=result.get)
    
    return result
# print(least('pppppghhhijeuupffe'))


# 8
def odd_occ(s):
    d ={}
    s = s.replace(' ','')
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ls = []
    for k,v in d.items():
        if v % 2 != 0:
            ls.append(v)

    return ls

# dictionary

# 1
def ordercheck(s,pattern):
    d = {}
    for i in range(len(pattern)):
        d[pattern[i]] = i
    
    res = ""
    for i in s:
        if (i in d):
            res = res + str(d[i])
    for i in range(len(res) -1):
        if res[i] > res[i+1]:
            return False
    return True

# 2
def mapele(ls,d):
    res = []
    for i in d:
        res.append({i : d[i]})
    
    
    return dict(zip(ls,res))

# 3
def sort_keys_val(d):
    # technique to sort the dict based on keys
    return {k: sorted(v) for k, v in sorted(d.items(), key=lambda item: item[0])}

# 4

def remove_dup(s):
    return ' '.join(set(s.split()))

# 5
def replacekeys(d):
    out = {}
    # updating keys 
    for key in d:
        new_key = list(d[key].keys())[0]
        new_val = {key : {}}
        out[new_key] = new_val

    return out

# 6

def largest(s):
    ls = s.split()
    d = {}
    mx = 0
    for i in ls:
        #technique to sort the string
        val = ''.join(sorted(i))
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
        mx = max(mx,d[val])
    return mx

# sets

# 1
def common(a,b):
    s1 = set(a)
    s2 = set(b)

    if len(s1.intersection(s2)):
        return True
    else:
        return False

# 2
def common_ele(a,b):
    s1 = set(a)
    s2 = set(b)

    return list(s1 & s2)

# 3
def max_min(s):
    maxn = float('-inf')
    minn = float('inf')

    for i in s:
        if i < minn:
            minn = i
        if i > maxn:
            maxn = i
    
    print(maxn)
    print(minn)

#4
def check(setx,sety,setz):
    print("If x is subset of y")
    # print(setx <= sety) --- another way to check subset
    print(setx.issubset(sety))
    print("If y is subset of x")
    # print(sety <= setx)
    print(sety.issubset(setx))
    print("\nIf y is subset of z")
    # print(sety <= setz)
    print(sety.issubset(setz))
    print("If z is subset of y")
    # print(setz <= sety)
    print(setz.issubset(sety))


# 5
def remove_common(s1,s2):
    s1 = s1 - s2
    print(s1)
    print(s2)

# 6

# It will result in set of all keys present in dictionary.

from collections import Counter

def countOccurancesOfAnagram(str, ptr):
    ptrDict = Counter(ptr) 
    dict = Counter(str[:len(ptr):])
    count = 0

    if ptrDict == dict:
        count += 1

    for idx in range(len(ptr), len(str)):
        ch = str[idx]

        # add current char
        dict[ch] += 1 if dict.get(ch) != None else dict.setdefault(ch, 1)

        # remove the count of prev char
        rch = str[idx - len(ptr)]
        if len(dict) and dict.get(rch) > 1:
            dict[rch] -= 1
        else:
            del dict[rch]

        if ptrDict == dict:
            count += 1

    return count


print(countOccurancesOfAnagram('aabaabaa', 'aaba'))
print(countOccurancesOfAnagram('avadhut', 'avds'))
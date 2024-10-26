from itertools import permutations
def num(num_list):
    arr = permutations(num_list, len(num_list))

    return list(arr)

arr = num([1,2,3,4])
for i in arr:
    print(f"[{', '.join(map(str, i))}]")
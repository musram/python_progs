import pdb
def max(lst):
    max_num = -float("inf")
    for num in lst:
        pdb.set_trace();
        if num > max_num:
            max_num = num
    return max_num

print(max([-1,-2,-4]))

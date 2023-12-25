# %%
with open("input.txt", "r") as input:
    d = int(input.readline().split()[1])
    arr = input.readline().split()


def rotateLeft(d, arr):
    for _ in range(d):
        arr.append(arr.pop(0))
    return arr


print(rotateLeft(d, arr))

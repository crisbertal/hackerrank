""" 
Solution for this hackerrank problem:
https://www.hackerrank.com/challenges/2d-array/problem
"""

with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")
    arr = [list(map(lambda x: int(x), line.split())) for line in lines]


def hourglassSum(arr):
    result = []
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[0]) - 2):
            result.append(
                sum(arr[i][j : j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j : j + 3])
            )
    return max(result)


print(hourglassSum(arr))

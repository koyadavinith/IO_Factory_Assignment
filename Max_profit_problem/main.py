def find(n):
    pr = 0
    prof = [0, 0, 0]
    if n < 4:
        return 0
    else:
        temp = n - 4
        prof[0] = temp * 1000
        if n >= 5:
            temp = n - 5
            prof[1] = temp * 1500
            if n >= 10:
                temp = n - 10
                prof[2] = temp * 3000
    max_index = getMax(prof)
    pr += prof[max_index]
    arr[max_index] += 1
    return pr + find(n - time_unit[max_index])

def getMax(prof):
    if prof[0] >= prof[1]:
        if prof[0] >= prof[2]:
            return 0
        else:
            return 2
    elif prof[1] >= prof[2]:
        return 1
    else:
        return 2

def solString():
    return "T: " + str(arr[1]) + ", P: " + str(arr[0]) + ", C: " + str(arr[2])

arr = [0, 0, 0]
time_unit = [4, 5, 10]

n = int(input("Enter the Time unit: "))
print("Earnings: $" + str(find(n)))
print("Solution:\n" + solString())

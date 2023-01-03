import statistics as stats
numbers = [1, 2, 3, 4, 5]
length = len(numbers)

get_sum = sum(numbers)
mean = get_sum/length

print("Mean is : ", mean)

numbers = [1, 2, 3, 4, 5]
n = len(numbers)
numbers.sort()

if length % 2 == 0:
    median1 = numbers[n//2]
    median2 = numbers[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = numbers[n//2]

print("Median is : " + str(median))

y = [11, 8, 3, 4, 5, 6, 8, 4, 5, 8]
y.sort()
l1 = []
i = 0

while i < len(y):
    l1.append(y.count(y[i]))
    i += 1

d1 = dict(zip(y, l1))
d2 = {k for (k, v) in d1.items() if v == max(l1)}

print("Mode is : " + str(d2))



# Using lib
n = [1, 4, 7, 8, 5, 2, 4, 0, 3]

n_mean = stats.mean(n)
n_median = stats.median(n)
n_mode = stats.mode(n)

print("Mean is : ", n_mean)
print("Median is : ", n_median)
print("Mode is : ", n_mode)





# Taking inputs
list = []

n = int(input("Enter number of elements : "))

for i in range(0, 10):
    print("Enter elements : ")
    ele = int(input())
    list.append(ele)

list_mean = stats.mean(list)
list_median = stats.median(list)
list_mode = stats.mode(list)

print("Mean is : ", list_mean)
print("Median is : ", list_median)
print("Mode is : ", list_mode)

import numpy

random_num = numpy.random.rand(1,50).tolist()[0]

def sort_(to_be_sorted):
    sorted_num = []
    for num in to_be_sorted:

        if len(sorted_num) == 0:
            sorted_num.append(num)
        elif len(sorted_num) == 1:
            if num > sorted_num[0]:
                sorted_num.insert(1, num)
            else:
                sorted_num.insert(0,num)
        elif num < sorted_num[0]:
            sorted_num.insert(0, num)
        else:
            for x in range(len(sorted_num) - 1):
                if sorted_num[x] <= num <= sorted_num[x + 1]:
                    sorted_num.insert(x + 1, num)
                    break
                elif num >= sorted_num[-1]:
                    sorted_num.append(num)
                    break

    return sorted_num

print(sort_(random_num))

random_num.sort()
print(random_num)

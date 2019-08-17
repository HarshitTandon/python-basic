class Rainwater:
    def __init__(self, test_cases):
        self.cases = test_cases

    def extra_space_method(self, list, size):
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = list[0]
        right_max[size - 1] = list[size - 1]
        for index in range(1, size):
            left_max[index] = max(left_max[index - 1], list[index])

        for index in range(size-2, -1, -1):
            right_max[index] = max(right_max[index + 1], list[index])

        result = 0
        for index in range(0, size):
            result += min(right_max[index], left_max[index]) - list[index]
        return result


t = Rainwater(int(input()))
while t.cases is not 0:
    size = int(input())
    list = []
    for index in range(0, size):
        list.append(int(input()))
    print(t.extra_space_method(list, size))
    t.cases -= 1
    # print(t.optimized_method)












    # solution which got submitted

class Rainwater:
    def __init__(self, test_cases):
        self.cases = test_cases

    def extra_space_method(self, list, size):
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = list[0]
        right_max[size - 1] = list[size - 1]
        for index in range(1, size):
            left_max[index] = max(left_max[index - 1], list[index])

        for index in range(size-2, -1, -1):
            right_max[index] = max(right_max[index + 1], list[index])

        result = 0
        for index in range(0, size):
            result += min(right_max[index], left_max[index]) - list[index]
        return result


t = Rainwater(int(input()))
while t.cases is not 0:
    size = int(input())
    list = []
    ele = input("")
    list = ele.split()
    for index in range(0, size):
        # ele = int(input())
        list[index] = int(list[index])
    print(t.extra_space_method(list, size))
    t.cases -= 1
    # print(t.optimized_method)


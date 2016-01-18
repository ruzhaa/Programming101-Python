def count_words(arr):
    result = dict()
    for word in arr:
        result[word] = arr.count(str(word))
    return result


def nan_expand(times):
    if times <= 0:
        return ""
    not_a = "Not a "
    result_str = ""
    while times != 0:
        result_str += not_a
        times -= 1
    return result_str + "NaN"


def iterations_of_nan_expand(expanded):
    not_a = "Not a"
    if expanded == "":
        return 0
    elif not_a in expanded:
        return expanded.count(not_a, 0, len(expanded))
    else:
        return False


def group(numbers):
    result = []
    group_num = [numbers[0]]
    for num in range(1, len(numbers)):
        if numbers[num] == numbers[num - 1]:
            group_num.append(numbers[num])
        else:
            result.append(group_num)
            group_num = [numbers[num]]

    result.append(group_num)
    return result


def max_consecutive(items):
    group_items = group(items)
    count = 0
    for it in range(0, len(group_items)):
        if count >= len(group_items[it]):
            continue
        else:
            count = len(group_items[it])
    return count


def gas_stations(distance, tank_size, stations):
    result = [0]
    stations.append(distance)
    for i in range(0, len(stations) - 1):
        # razlikata dali ima dostatachno mejdu dve stancii
        temp = stations[i + 1] - stations[i]
        # ot stanciita do prednoto zarejdane
        a = stations[i] - result[-1]
        size = tank_size - a

        if size < temp:
            result.append(stations[i])
            # otnowo e zareden na max
            size = tank_size
    # bez purvoto zarejdane na [0]
    return result[1:]
    
    
def dictionary(number, count):
    phone = {}
    phone[0] = [" "]
    phone[2] = ["a", "b", "c"]
    phone[3] = ["d", "e", "f"]
    phone[4] = ["g", "h", "i"]
    phone[5] = ["j", "k", "l"]
    phone[6] = ["m", "n", "o"]
    phone[7] = ["p", "q", "r", "s"]
    phone[8] = ["t", "u", "v"]
    phone[9] = ["w", "x", "y", "z"]
    
    if count >= len(phone[number]):
        return phone[number][count - len(phone[number]) - 1]
        
    return phone[number][count - 1]
    

def numbers_to_message(sequence):
    group_of_numbers = group(sequence)
    message = ""
    count = 0
    next_index = 0
    up = False
    
    for gr in group_of_numbers:
        count = len(gr)
        if gr[0] == 1:
            up = True
            continue
        
        if gr[0] == -1:
            continue
        
        if up:
            i = group_of_numbers.index(gr)
            next_list = group_of_numbers[i]
            message += dictionary(next_list[0], count).upper()
            up = False
        else:
            message += dictionary(gr[0], count)
  
    return message

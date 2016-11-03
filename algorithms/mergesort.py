from collections import defaultdict


split_steps = defaultdict(list)
merge_steps = defaultdict(list)


def reset_steps():
    split_steps.clear()
    merge_steps.clear()


def mergesort(arr, n=1):
    size = len(arr)

    if n == 1:
        reset_steps()

    if size == 1:
        return arr

    split_steps[n].append(arr[:size // 2])
    split_steps[n].append(arr[size // 2:])

    l_arr = mergesort(arr[:size // 2], n + 1)
    r_arr = mergesort(arr[size // 2:], n + 1)

    l_size = len(l_arr)
    r_size = len(r_arr)

    i, j = 0, 0

    merged = []

    while i < l_size and j < r_size:
        if l_arr[i] < r_arr[j]:
            merged.append(l_arr[i])
            i += 1
        else:
            merged.append(r_arr[j])
            j += 1

    merged.extend(l_arr[i:])
    merged.extend(r_arr[j:])

    merge_steps[n].append(merged)

    return merged


def get_split_steps():
    return split_steps


def get_merge_steps():
    return merge_steps

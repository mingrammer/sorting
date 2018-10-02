def qsort(a):

    def sort_part(first, last):

        if last <= first:
            return
        pivot_index = first + (last - first)/2
        pivot_value = a[int(pivot_index)]
        a[int(pivot_index)], a[int(first)] = a[int(first)], a[int(pivot_index)]
        low = first + 1
        high = last
        while low <= high:
            while low <= high and a[low] <= pivot_value:
                low += 1
            while low <= high and a[high] >= pivot_value:
                high -= 1
            assert low != high
            if low < high:
                assert a[low] > a[high]
                a[low], a[high] = a[high], a[low]
                low += 1
                high -= 1
        assert low == high + 1
        pivot_index = high

        a[first], a[pivot_index] = a[pivot_index], a[first]

        sort_part(first, pivot_index - 1)
        sort_part(pivot_index + 1, last)

    sort_part(0, len(a) - 1)


if __name__ == "__main__":
    lista_entrada = [72, 35, 8, 90, 65, 44, 31, 22, 29, 78, 83]

    qsort(lista_entrada)
    print(lista_entrada)

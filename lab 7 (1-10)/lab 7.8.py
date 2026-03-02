def max_element(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]

    max_rest = max_element(arr, index + 1)
    return arr[index] if arr[index] > max_rest else max_rest
# Quick sort implementation
def sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i <= pivot]
        greater = [i for i in data[1:] if i > pivot]
        return sort(less) + [pivot] + sort(greater)

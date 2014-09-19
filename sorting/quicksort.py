def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def quicksort(seq):
    if len(seq) <= 1: return seq #Base case
    lo, pi, hi = partition(seq)  #
    return quicksort(lo) + [pi] + quicksort(hi)

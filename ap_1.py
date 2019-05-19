#https://codingbat.com/prob/p100369
def commonTwo(a, b):
    return len(set(a) | set(b)) - len(set(a) ^ set(b))


assert commonTwo(["a", "c", "x"], ["b", "c", "d", "x"]) == 2
assert commonTwo(["a", "c", "x"], ["a", "b", "c", "x", "z"]) == 3
assert commonTwo(["a", "b", "c"], ["a", "b", "c"]) == 3
assert commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "c"]) == 3
assert commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "b", "c"]) == 3
assert commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "c", "c"]) == 3
assert commonTwo(["b", "b", "b", "b", "c"], ["a", "b", "b", "b", "c"]) == 2
assert commonTwo(["a", "b", "c", "c", "d"], ["a", "b", "b", "c", "d", "d"]) == 4
assert commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b"]) == 1
assert commonTwo(["a", "a", "b", "b", "c"], ["c", "c"]) == 1
assert commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b", "x"]) == 1
assert commonTwo(["a", "a", "b", "b", "c"], ["b", "b"]) == 1
assert commonTwo(["a"], ["a", "b"]) == 1
assert commonTwo(["a"], ["b"]) == 0
assert commonTwo(["a", "a"], ["b", "b"]) == 0
assert commonTwo(["a", "b"], ["a", "b"]) == 2
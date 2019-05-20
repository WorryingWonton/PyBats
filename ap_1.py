def mergeTwo(a, b, n):
    return sorted(set(a) | set(b))[:n]

def commonTwo(a, b):
    return len(set(a) | set(b)) - len(set(a) ^ set(b))


assert mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3) == ["a", "b", "c"]
assert mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3) == ["a", "c", "f"]
assert mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3) == ["c", "f", "g"]
assert mergeTwo(["a", "c", "z"], ["a", "c", "z"], 3) == ["a", "c", "z"]
assert mergeTwo(["a", "b", "c", "z"], ["a", "c", "z"], 3) == ["a", "b", "c"]
assert mergeTwo(["a", "c", "z"], ["a", "b", "c", "z"], 3) == ["a", "b", "c"]
assert mergeTwo(["a", "c", "z"], ["a", "c", "z"], 2) == ["a", "c"]
assert mergeTwo(["a", "c", "z"], ["a", "c", "y", "z"], 3) == ["a", "c", "y"]
assert mergeTwo(["x", "y", "z"], ["a", "b", "z"], 3) == ["a", "b", "x"]

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
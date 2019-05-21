def mapBully(map):
    if 'a' in map.keys():
        map['b'], map['a'] = map['a'], ''
    return map

def mapShare(map):
    if 'a' in map.keys():
        map['b'] = map['a']
    del map['c']
    return map

def mapAB(map):
    if 'a' in map.keys() and 'b' in map.keys():
        map['ab'] = map['a'] + map['b']
    return map

def topping1(map):
    if 'ice cream' in map.keys():
        map['ice cream'] = 'cherry'
    map['bread'] = 'butter'
    return map

def topping2(map):
    if 'ice cream' in map.keys():
        map['yogurt'] = map['ice cream']
    if 'spinach' in map.keys():
        map['spinach'] = 'nuts'
    return map

def topping3(map):
    if 'potato' in map.keys():
       map['fries'] = map['potato']
    if 'salad' in map.keys():
        map['spinach'] = map['salad']
    return map

def mapAB2(map):
    if 'a' in map.keys() and 'b' in map.keys() and map['a'] == map['b']:
        del map['a']
        del map['b']
    return map

def mapAB3(map):
    if 'a' in map.keys() and 'b' not in map.keys():
        map['b'] = map['a']
    elif 'b' in map.keys() and 'a' not in map.keys():
        map['a'] = map['b']
    return map

def mapAB4(map):
    if 'a' in map.keys() and 'b' in map.keys() and len(map['a']) != len(map['b']):
        map['c'] = max(map['a'], map['b'], key=len)
    elif 'a' in map.keys() and 'b' in map.keys():
        map['a'], map['b'] = '', ''
    return map


assert mapBully({"a": "candy", "b": "dirt"}) == {"a": "", "b": "candy"}
assert mapBully({"a": "candy"}) == {"a": "", "b": "candy"}
assert mapBully({"a": "candy", "b": "carrot", "c": "meh"}) == {"a": "", "b": "candy", "c": "meh"}
assert mapBully({"b": "carrot"}) == {"b": "carrot"}
assert mapBully({"c": "meh"}) == {"c": "meh"}
assert mapBully({"a": "sparkle", "c": "meh"}) == {"a": "", "b": "sparkle", "c": "meh"}

assert mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) == {"a": "aaa", "b": "aaa"}
assert mapShare({"b": "xyz", "c": "ccc"}) == {"b": "xyz"}
assert mapShare({"a": "aaa", "c": "meh", "d": "hi"}) == {"a": "aaa", "b": "aaa", "d": "hi"}
assert mapShare({"a": "xyz", "b": "1234", "c": "yo", "z": "zzz"}) == {"a": "xyz", "b": "xyz", "z": "zzz"}
assert mapShare({"a": "xyz", "b": "1234", "c": "yo", "d": "ddd", "e": "everything"}) == {"a": "xyz", "b": "xyz", "d": "ddd", "e": "everything"}

assert mapAB({"a": "Hi", "b": "There"}) == {"a": "Hi", "ab": "HiThere", "b": "There"}
assert mapAB({"a": "Hi"}) == {"a": "Hi"}
assert mapAB({"b": "There"}) == {"b": "There"}
assert mapAB({"c": "meh"}) == {"c": "meh"}
assert mapAB({"a": "aaa", "ab": "nope", "b": "bbb", "c": "ccc"}) == {"a": "aaa", "ab": "aaabbb", "b": "bbb", "c": "ccc"}
assert mapAB({"ab": "nope", "b": "bbb", "c": "ccc"}) == {"ab": "nope", "b": "bbb", "c": "ccc"}

assert topping1({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}
assert topping1({}) == {"bread": "butter"}
assert topping1({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}
assert topping1({"bread": "dirt", "ice cream": "strawberries"}) == {"bread": "butter", "ice cream": "cherry"}
assert topping1({"bread": "jam", "ice cream": "strawberries", "salad": "oil"}) == {"bread": "butter", "ice cream": "cherry", "salad": "oil"}

assert topping2({"ice cream": "cherry"}) == {"yogurt": "cherry", "ice cream": "cherry"}
assert topping2({"spinach": "dirt", "ice cream": "cherry"}) == {"yogurt": "cherry", "spinach": "nuts", "ice cream": "cherry"}
assert topping2({"yogurt": "salt"}) == {"yogurt": "salt"}
assert topping2({"yogurt": "salt", "bread": "butter"}) == {"yogurt": "salt", "bread": "butter"}
assert topping2({}) == {}
assert topping2({"ice cream": "air", "salad": "oil"}) == {"yogurt": "air", "ice cream": "air", "salad": "oil"}

assert topping3({"potato": "ketchup"}) == {"potato": "ketchup", "fries": "ketchup"}
assert topping3({"potato": "butter"}) == {"potato": "butter", "fries": "butter"}
assert topping3({"salad": "oil", "potato": "ketchup"}) == {"spinach": "oil", "salad": "oil", "potato": "ketchup", "fries": "ketchup"}
assert topping3({"toast": "butter", "salad": "oil", "potato": "ketchup"}) == {"toast": "butter", "spinach": "oil", "salad": "oil", "potato": "ketchup", "fries": "ketchup"}
assert topping3({}) == {}
assert topping3({"salad": "pepper", "fries": "salt"}) == {"spinach": "pepper", "salad": "pepper", "fries": "salt"}

assert mapAB2({"a": "aaa", "b": "aaa", "c": "cake"}) == {"c": "cake"}
assert mapAB2({"a": "aaa", "b": "bbb"}) == {"a": "aaa", "b": "bbb"}
assert mapAB2({"a": "aaa", "b": "bbb", "c": "aaa"}) == {"a": "aaa", "b": "bbb", "c": "aaa"}
assert mapAB2({"a": "aaa"}) == {"a": "aaa"}
assert mapAB2({"b": "bbb"}) == {"b": "bbb"}
assert mapAB2({"a": "", "b": "", "c": "ccc"}) == {"c": "ccc"}
assert mapAB2({}) == {}
assert mapAB2({"a": "a", "b": "b", "z": "zebra"}) == {"a": "a", "b": "b", "z": "zebra"}

assert mapAB3({"a": "aaa", "c": "cake"}) == {"a": "aaa", "b": "aaa", "c": "cake"}
assert mapAB3({"b": "bbb", "c": "cake"}) == {"a": "bbb", "b": "bbb", "c": "cake"}
assert mapAB3({"a": "aaa", "b": "bbb", "c": "cake"}) == {"a": "aaa", "b": "bbb", "c": "cake"}
assert mapAB3({"ccc": "ccc"}) == {"ccc": "ccc"}
assert mapAB3({"c": "a", "d": "b"}) == {"c": "a", "d": "b"}
assert mapAB3({}) == {}
assert mapAB3({"a": ""}) == {"a": "", "b": ""}
assert mapAB3({"b": ""}) == {"a": "", "b": ""}
assert mapAB3({"a": "", "b": ""}) == {"a": "", "b": ""}
assert mapAB3({"aa": "aa", "a": "apple", "z": "zzz"}) == {"aa": "aa", "a": "apple", "b": "apple", "z": "zzz"}

assert mapAB4({"a": "aaa", "b": "bb", "c": "cake"}) == {"a": "aaa", "b": "bb", "c": "aaa"}
assert mapAB4({"a": "aa", "b": "bbb", "c": "cake"}) == {"a": "aa", "b": "bbb", "c": "bbb"}
assert mapAB4({"a": "aa", "b": "bbb"}) == {"a": "aa", "b": "bbb", "c": "bbb"}
assert mapAB4({"a": "aaa"}) == {"a": "aaa"}
assert mapAB4({"b": "bbb"}) == {"b": "bbb"}
assert mapAB4({"a": "aaa", "b": "bbb", "c": "cake"}) == {"a": "", "b": "", "c": "cake"}
assert mapAB4({"a": "a", "b": "b", "c": "cake"}) == {"a": "", "b": "", "c": "cake"}
assert mapAB4({"a": "", "b": "b", "c": "cake"}) == {"a": "", "b": "b", "c": "b"}
assert mapAB4({"a": "a", "b": "", "c": "cake"}) == {"a": "a", "b": "", "c": "a"}
assert mapAB4({"c": "cat", "d": "dog"}) == {"c": "cat", "d": "dog"}
assert mapAB4({"ccc": "ccc"}) == {"ccc": "ccc"}
assert mapAB4({"c": "a", "d": "b"}) == {"c": "a", "d": "b"}
assert mapAB4({}) == {}
assert mapAB4({"a": "", "z": "z"}) == {"a": "", "z": "z"}
assert mapAB4({"b": "", "z": "z"}) == {"b": "", "z": "z"}
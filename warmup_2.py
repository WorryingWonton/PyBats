def string_times(str, n):
    return n*str

def front_times(str, n):
    return str[:3] * n

def countXX(str):
    return sum([1 for idx in range(len(str)) if str[idx:idx + 2] == 'xx'])

def doubleX(str):
    for idx in range(len(str) - 1):
        if str[idx] == 'x':
            return str[idx + 1] == 'x'
    return False

def string_bits(str):
    return ''.join([str[idx] for idx in range(0, len(str), 2)])

def string_splosion(str):
    return ''.join([str[:idx] for idx in range(len(str) + 1)])

def last2(str):
    count = 0
    for idx in range(len(str[:-2])):
        if str[idx:idx + 2] == str[-2:]:
            count += 1
    return count

def array_count9(nums):
    return len([x for x in nums if x == 9])

def array_front9(nums):
    return 9 in nums[:4]

def array123(nums):
    return len([x for x in range(len(nums) - 2) if nums[x:x + 3] == [1, 2, 3]]) > 0

def string_match(a, b):
    return sum([1 for idx, x in enumerate(min(a, b, key=len)[:-1]) if a[idx:idx + 2] == b[idx:idx + 2]])

def stringX(str):
    return ('x' if str[:1] == 'x' else '') + ''.join(str.split('x')) + ('x' if str[-1:] == 'x' and str != 'x' else '')

def altPairs(str):
    return ''.join([str[idx:idx + 2] for idx in range(0, len(str), 4)])

def stringYak(str):
    new_str = ''
    index = 0
    while index < len(str):
        if str[index:index + 1] + str[index + 2:index + 3] == 'yk':
            index += 3
        else:
            new_str += str[index]
            index += 1
    return new_str

def array667(nums):
    return sum([1 for idx in range(len(nums) - 1) if nums[idx] == 6 and nums[idx + 1] in [6, 7]])

def noTriples(nums):
    return not sum([1 for idx, x in enumerate(nums[:-2]) if nums[idx:idx + 3] == [x] * 3])

def has271(nums):
    return sum([1 for i, x in enumerate(nums[:-2]) if x == nums[i + 1] - 5 and nums[i + 2] in range(x - 3, x + 2)]) > 0


assert string_times('Hi', 2) == 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'
assert string_times('Hi', 0) == ''
assert string_times('Hi', 5) == 'HiHiHiHiHi'
assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
assert string_times('x', 4) == 'xxxx'
assert string_times('', 4) == ''
assert string_times('code', 2) == 'codecode'
assert string_times('code', 3) == 'codecodecode'

assert front_times('Chocolate', 2) == 'ChoCho'
assert front_times('Chocolate', 3) == 'ChoChoCho'
assert front_times('Abc', 3) == 'AbcAbcAbc'
assert front_times('Ab', 4) == 'AbAbAbAb'
assert front_times('A', 4) == 'AAAA'
assert front_times('', 4) == ''
assert front_times('Abc', 0) == ''

assert countXX("abcxx") == 1
assert countXX("xxx") == 2
assert countXX("xxxx") == 3
assert countXX("abc") == 0
assert countXX("Hello there") == 0
assert countXX("Hexxo thxxe") == 2
assert countXX("") == 0
assert countXX("Kittens") == 0
assert countXX("Kittensxxx") == 2

assert doubleX("axxbb") == True
assert doubleX("axaxax") == False
assert doubleX("xxxxx") == True
assert doubleX("xaxxx") == False
assert doubleX("aaaax") == False
assert doubleX("") == False
assert doubleX("abc") == False
assert doubleX("x") == False
assert doubleX("xx") == True
assert doubleX("xax") == False
assert doubleX("xaxx") == False

assert string_bits('Hello') == 'Hlo'
assert string_bits('Hi') == 'H'
assert string_bits('Heeololeo') == 'Hello'
assert string_bits('HiHiHi') == 'HHH'
assert string_bits('') == ''
assert string_bits('Greetings') == 'Getns'
assert string_bits('Chocoate') == 'Coot'
assert string_bits('pi') == 'p'
assert string_bits('Hello Kitten') == 'HloKte'
assert string_bits('hxaxpxpxy') == 'happy'

assert string_splosion('Code') == 'CCoCodCode'
assert string_splosion('abc') == 'aababc'
assert string_splosion('ab') == 'aab'
assert string_splosion('x') == 'x'
assert string_splosion('fade') == 'ffafadfade'
assert string_splosion('There') == 'TThTheTherThere'
assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
assert string_splosion('Bye') == 'BByBye'
assert string_splosion('Good') == 'GGoGooGood'
assert string_splosion('Bad') == 'BBaBad'

assert last2('hixxhi') == 1
assert last2('xaxxaxaxx') == 1
assert last2('axxxaaxx') == 2
assert last2('xxaxxaxxaxx') == 3
assert last2('xaxaxaxx') == 0
assert last2('xxxx') == 2
assert last2('13121312') == 1
assert last2('11212') == 1
assert last2('13121311') == 0
assert last2('1717171') == 2
assert last2('hi') == 0
assert last2('h') == 0
assert last2('') == 0

assert array_count9([1, 2, 9]) == 1
assert array_count9([1, 9, 9]) == 2
assert array_count9([1, 9, 9, 3, 9]) == 3
assert array_count9([1, 2, 3]) == 0
assert array_count9([]) == 0
assert array_count9([4, 2, 4, 3, 1]) == 0
assert array_count9([9, 2, 4, 3, 1]) == 1

assert array_front9([1, 2, 9, 3, 4]) == True
assert array_front9([1, 2, 3, 4, 9]) == False
assert array_front9([1, 2, 3, 4, 5]) == False
assert array_front9([9, 2, 3]) == True
assert array_front9([1, 9, 9]) == True
assert array_front9([1, 2, 3]) == False
assert array_front9([1, 9]) == True
assert array_front9([5, 5]) == False
assert array_front9([2]) == False
assert array_front9([9]) == True
assert array_front9([]) == False
assert array_front9([3, 9, 2, 3, 3]) == True

assert array123([1, 1, 2, 3, 1]) == True
assert array123([1, 1, 2, 4, 1]) == False
assert array123([1, 1, 2, 1, 2, 3]) == True
assert array123([1, 1, 2, 1, 2, 1]) == False
assert array123([1, 2, 3, 1, 2, 3]) == True
assert array123([1, 2, 3]) == True
assert array123([1, 1, 1]) == False
assert array123([1, 2]) == False
assert array123([1]) == False
assert array123([]) == False

assert string_match('xxcaazz', 'xxbaaz') == 3
assert string_match('abc', 'abc') == 2
assert string_match('abc', 'axc') == 0
assert string_match('hello', 'he') == 1
assert string_match('he', 'hello') == 1
assert string_match('h', 'hello') == 0
assert string_match('', 'hello') == 0
assert string_match('aabbccdd', 'abbbxxd') == 1
assert string_match('aaxxaaxx', 'iaxxai') == 3
assert string_match('iaxxai', 'aaxxaaxx') == 3

assert stringX("xxHxix") == "xHix"
assert stringX("abxxxcd") == "abcd"
assert stringX("xabxxxcdx") == "xabcdx"
assert stringX("xKittenx") == "xKittenx"
assert stringX("Hello") == "Hello"
assert stringX("xx") == "xx"
assert stringX("x") == "x"
assert stringX("") == ""

assert altPairs("kitten") == "kien"
assert altPairs("Chocolate") == "Chole"
assert altPairs("CodingHorror") == "Congrr"
assert altPairs("yak") == "ya"
assert altPairs("ya") == "ya"
assert altPairs("y") == "y"
assert altPairs("") == ""
assert altPairs("ThisThatTheOther") == "ThThThth"

assert stringYak("yakpak") == "pak"
assert stringYak("pakyak") == "pak"
assert stringYak("yak123ya") == "123ya"
assert stringYak("yak") == ""
assert stringYak("yakxxxyak") == "xxx"
assert stringYak("HiyakHi") == "HiHi"
assert stringYak("xxxyakyyyakzzz") == "xxxyyzzz"

assert array667([6, 6, 2]) == 1
assert array667([6, 6, 2, 6]) == 1
assert array667([6, 7, 2, 6]) == 1
assert array667([6, 6, 2, 6, 7]) == 2
assert array667([1, 6, 3]) == 0
assert array667([6, 1]) == 0
assert array667([]) == 0
assert array667([3, 6, 7, 6]) == 1
assert array667([3, 6, 6, 7]) == 2
assert array667([6, 3, 6, 6]) == 1
assert array667([6, 7, 6, 6]) == 2
assert array667([1, 2, 3, 5, 6]) == 0
assert array667([1, 2, 3, 6, 6]) == 1

assert noTriples([1, 1, 2, 2, 1]) == True
assert noTriples([1, 1, 2, 2, 2, 1]) == False
assert noTriples([1, 1, 1, 2, 2, 2, 1]) == False
assert noTriples([1, 1, 2, 2, 1, 2, 1]) == True
assert noTriples([1, 2, 1]) == True
assert noTriples([1, 1, 1]) == False
assert noTriples([1, 1]) == True
assert noTriples([1]) == True
assert noTriples([]) == True

assert has271([1, 2, 7, 1]) == True
assert has271([1, 2, 8, 1]) == False
assert has271([2, 7, 1]) == True
assert has271([3, 8, 2]) == True
assert has271([2, 7, 3]) == True
assert has271([2, 7, 4]) == False
assert has271([2, 7, -1]) == True
assert has271([2, 7, -2]) == False
assert has271([4, 5, 3, 8, 0]) == True
assert has271([2, 7, 5, 10, 4]) == True
assert has271([2, 7, -2, 4, 9, 3]) == True
assert has271([2, 7, 5, 10, 1]) == False
assert has271([2, 7, -2, 4, 10, 2]) == False
assert has271([1, 1, 4, 9, 0]) == False
assert has271([1, 1, 4, 9, 4, 9, 2]) == True
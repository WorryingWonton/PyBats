#https://codingbat.com/java/String-3
def countYZ(str1):
    return len(list(filter(lambda x: x[-1] in 'yz', [x for x in ''.join(map(lambda x: ' ' if not x.isalpha() else x, str1.lower())).split(' ') if x])))

def withoutString(base, remove):
    idx = base.lower().find(remove.lower())
    if idx >= 0:
        return (base[0:idx] if base[0:idx] != ' ' else '') + withoutString(base=base[idx + len(remove):len(base)], remove=remove)
    else:
        return base

def notReplace(str1):
    idx = 0
    while idx < len(str1) - 1:
        if str1[idx:idx + 2] == 'is' and (len(str1) == 2 or (((idx == 0 and not str1[idx + 2].isalpha()) or (idx == len(str1) - 2 and not str1[idx - 1].isalpha())) or (not str1[idx - 1].isalpha() and not str1[idx + 2].isalpha()))):
            str1 = str1[0:idx + 2] + ' not' + str1[idx + 2:]
            idx += 6
        else:
            idx += 1
    return str1

def mirrorEnds(my_string):
    mir_str = ''
    for idx in range(len(my_string)):
        if my_string[idx] == my_string[-idx - 1]:
            mir_str += my_string[idx]
        else:
            break
    return mir_str

def countTriple(my_string):
    return (1 if (len(my_string) > 2 and (my_string[0] == my_string[1] and my_string[1] == my_string[2])) else 0) + countTriple(my_string[1:]) if my_string else 0

def gHappy(my_string):
    return len([x for x in ''.join(map(lambda x: ' ' if x != 'g' else x, my_string)).split() if len(x) == 1]) == 0

def equalIsNot(my_string):
    return len(my_string.split('is')) == len(my_string.split('not'))

def sumDigits(my_string):
    return sum(map(lambda x: int(x), filter(lambda x: x.isdigit(), my_string)))

def sameEnds(my_string):
    lh = my_string[0:int(len(my_string) / 2)]
    rh = my_string[int(len(my_string) / 2) + len(my_string) % 2:len(my_string)]
    new_s = ''
    while rh:
        if lh[0] != rh[0]:
            new_s = ''
        else:
            new_s += rh[0]
            lh = lh[1:]
        rh = rh[1:]
    return new_s if new_s and new_s[0] == my_string[0] else ''

def maxBlock(my_string):
    max_len = 0
    count = 1
    for idx in range(1, len(my_string)):
        if my_string[idx] == my_string[idx - 1]:
            count += 1
        else:
            count = 1
        max_len = max(count, max_len)
    return max_len

def sumNumbers(my_string):
    nums = []
    substr = ''
    for elem in my_string:
        if elem.isdigit():
            substr += elem
        else:
            nums.append(int(substr)) if substr else 0
            substr = ''
    return sum(nums + ([int(substr)] if substr else [0]))

assert countYZ("fez day") == 2
assert countYZ("day fez") == 2
assert countYZ("day fyyyz") == 2
assert countYZ("day yak") == 1
assert countYZ("day:yak") == 1
assert countYZ("!!day--yaz!!") == 2
assert countYZ("yak zak") == 0
assert countYZ("DAY abc XYZ") == 2
assert countYZ("aaz yyz my") == 3
assert countYZ("y2bz") == 2
assert countYZ("zxyx") == 0

assert withoutString("Hello there", "llo") == "He there"
assert withoutString("Hello there", "e") == "Hllo thr"
assert withoutString("Hello there", "x") == "Hello there"
assert withoutString("This is a FISH", "IS") == "Th a FH"
assert withoutString("THIS is a FISH", "is") == "TH a FH"
assert withoutString("THIS is a FISH", "iS") == "TH a FH"
assert withoutString("abxxxxab", "xx") == "abab"
assert withoutString("abxxxab", "xx") == "abxab"
assert withoutString("abxxxab", "x") == "abab"
assert withoutString("xxx", "x") == ""
assert withoutString("xxx", "xx") == "x"
assert withoutString("xyzzy", "Y") == "xzz"
assert withoutString("", "x") == ""
assert withoutString("abcabc", "b") == "acac"
assert withoutString("AA22bb", "2") == "AAbb"
assert withoutString("1111", "1") == ""
assert withoutString("1111", "11") == ""
assert withoutString("MkjtMkx", "Mk") == "jtx"
assert withoutString("Hi HoHo", "Ho") == "Hi "
assert withoutString("Hi there Bill!", " ") == "HithereBill!"
assert withoutString(" Hi there Bill!", " ") == "HithereBill!"
assert withoutString(" Hi there Bill!", " ") == "HithereBill!"
assert withoutString("Hi there Bill! ", " ") == "HithereBill!"

assert notReplace("is test") == "is not test"
assert notReplace("is-is") == "is not-is not"
assert notReplace("This is right") == "This is not right"
assert notReplace("This is isabell") == "This is not isabell"
assert notReplace("") == ""
assert notReplace("is") == "is not"
assert notReplace("isis") == "isis"
assert notReplace("Dis is bliss is") == "Dis is not bliss is not"
assert notReplace("is his") == "is not his"
assert notReplace("xis yis") == "xis yis"
assert notReplace("AAAis is") == "AAAis is not"

assert equalIsNot("This is not") == False
assert equalIsNot("This is notnot") == True
assert equalIsNot("noisxxnotyynotxisi") == True
assert equalIsNot("noisxxnotyynotxsi") == False
assert equalIsNot("xxxyyyzzzintint") == True
assert equalIsNot("") == True
assert equalIsNot("isisnotnot") == True
assert equalIsNot("isisnotno7Not") == False
assert equalIsNot("isnotis") == False
assert equalIsNot("mis3notpotbotis") == False

assert mirrorEnds("abXYZba") == "ab"
assert mirrorEnds("abca") == "a"
assert mirrorEnds("aba") == "aba"
assert mirrorEnds("abab") == ""
assert mirrorEnds("xxx") == "xxx"
assert mirrorEnds("xxYxx") == "xxYxx"
assert mirrorEnds("Hi and iH") == "Hi "
assert mirrorEnds("x") == "x"
assert mirrorEnds("") == ""
assert mirrorEnds("123and then 321") == "123"
assert mirrorEnds("band andab") == "ba"

assert countTriple("abcXXXabc") == 1
assert countTriple("xxxabyyyycd") == 3
assert countTriple("a") == 0
assert countTriple("") == 0
assert countTriple("XXXabc") == 1
assert countTriple("XXXXabc") == 2
assert countTriple("XXXXXabc") == 3
assert countTriple("222abyyycdXXX") == 3
assert countTriple("abYYYabXXXXXab") == 4
assert countTriple("abYYXabXXYXXab") == 0
assert countTriple("abYYXabXXYXXab") == 0
assert countTriple("122abhhh2") == 1

assert gHappy("xxggxx") == True
assert gHappy("xxgxx") == False
assert gHappy("xxggyygxx") == False
assert gHappy("g") == False
assert gHappy("gg") == True
assert gHappy("") == True
assert gHappy("xxgggxyz") == True
assert gHappy("xxgggxyg") == False
assert gHappy("xxgggxygg") == True
assert gHappy("mgm") == False
assert gHappy("mggm") == True
assert gHappy("yyygggxyy") == True

assert sumDigits("aa1bc2d3") == 6
assert sumDigits("aa11b33") == 8
assert sumDigits("Chocolate") == 0
assert sumDigits("5hoco1a1e") == 7
assert sumDigits("123abc123") == 12
assert sumDigits("") == 0
assert sumDigits("Hello") == 0
assert sumDigits("X1z9b2") == 12
assert sumDigits("5432a") == 14

assert sameEnds("abXYab") == "ab"
assert sameEnds("xx") == "x"
assert sameEnds("xxx") == "x"
assert sameEnds("xxxx") == "xx"
assert sameEnds("javaXYZjava") == "java"
assert sameEnds("javajava") == "java"
assert sameEnds("xavaXYZjava") == ""
assert sameEnds("Hello! and Hello!") == "Hello!"
assert sameEnds("x") == ""
assert sameEnds("") == ""
assert sameEnds("abcb") == ""
assert sameEnds("mymmy") == "my"

assert maxBlock("hoopla") == 2
assert maxBlock("abbCCCddBBBxx") == 3
assert maxBlock("") == 0
assert maxBlock("xyz") == 1
assert maxBlock("xxyz") == 2
assert maxBlock("xyzz") == 2
assert maxBlock("abbbcbbbxbbbx") == 3
assert maxBlock("XXBBBbbxx") == 3
assert maxBlock("XXBBBBbbxx") == 4
assert maxBlock("XXBBBbbxxXXXX") == 4
assert maxBlock("XX2222BBBbbXX2222") == 4

assert sumNumbers("abc123xyz") == 123
assert sumNumbers("aa11b33") == 44
assert sumNumbers("7 11") == 18
assert sumNumbers("Chocolate") == 0
assert sumNumbers("5hoco1a1e") == 7
assert sumNumbers("5$$1;;1!!") == 7
assert sumNumbers("a1234bb11") == 1245
assert sumNumbers("") == 0
assert sumNumbers("a22bbb3") == 25
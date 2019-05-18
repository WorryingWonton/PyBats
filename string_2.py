def double_char(str):
    return ''.join([2*x for x in str])

def count_hi(str):
    return len(str.split('hi')) - 1

def cat_dog(str):
    return len(str.split('cat')) == len(str.split('dog'))

def count_code(str):
    return len([x for idx, x in enumerate(str) if (idx < len(str) - 3 and (x == 'c' and str[idx + 1] == 'o' and str[idx + 3] == 'e'))])

def end_other(a, b):
    return a[len(a) - len(b):].lower() == b.lower() or b[len(b) - len(a):].lower() == a.lower()

def xyz_there(str):
    return 'xyz' in ''.join(str.split('.xyz'))


assert double_char('The') == 'TThhee'
assert double_char('AAbb') == 'AAAAbbbb'
assert double_char('Hi-There') == 'HHii--TThheerree'
assert double_char('Word!') == 'WWoorrdd!!'
assert double_char('') == ''
assert double_char('a') == 'aa'
assert double_char('.') == '..'
assert double_char('aa') == 'aaaa'

assert count_hi('abc hi ho') == 1
assert count_hi('ABChi hi') == 2
assert count_hi('hihi') == 2
assert count_hi('hiHIhi') == 2
assert count_hi('') == 0
assert count_hi('h') == 0
assert count_hi('hi') == 1
assert count_hi('Hi is no HI on ahI') == 0
assert count_hi('hiho not HOHIhi') == 2

assert cat_dog('catdog') == True
assert cat_dog('catcat') == False
assert cat_dog('1cat1cadodog') == True
assert cat_dog('catxxdogxxxdog') == False
assert cat_dog('catxdogxdogxcat') == True
assert cat_dog('catxdogxdogxca') == False
assert cat_dog('dogdogcat') == False
assert cat_dog('dogogcat') == True
assert cat_dog('dog') == False
assert cat_dog('cat') == False
assert cat_dog('ca') == True
assert cat_dog('c') == True
assert cat_dog('') == True

assert count_code('aaacodebbb') == 1
assert count_code('codexxcode') == 2
assert count_code('cozexxcope') == 2
assert count_code('cozfxxcope') == 1
assert count_code('xxcozeyycop') == 1
assert count_code('cozcop') == 0
assert count_code('abcxyz') == 0
assert count_code('code') == 1
assert count_code('ode') == 0
assert count_code('c') == 0
assert count_code('') == 0
assert count_code('AAcodeBBcoleCCccoreDD') == 3
assert count_code('AAcodeBBcoleCCccorfDD') == 2
assert count_code('coAcodeBcoleccoreDD') == 3

assert end_other('Hiabc', 'abc') == True
assert end_other('AbC', 'HiaBc') == True
assert end_other('abc', 'abXabc') == True
assert end_other('Hiabc', 'abcd') == False
assert end_other('Hiabc', 'bc') == True
assert end_other('Hiabcx', 'bc') == False
assert end_other('abc', 'abc') == True
assert end_other('xyz', '12xyz') == True
assert end_other('yz', '12xz') == False
assert end_other('Z', '12xz') == True
assert end_other('12', '12') == True
assert end_other('abcXYZ', 'abcDEF') == False
assert end_other('ab', 'ab12') == False
assert end_other('ab', '12ab') == True

assert xyz_there('abcxyz') == True
assert xyz_there('abc.xyz') == False
assert xyz_there('xyz.abc') == True
assert xyz_there('abcxy') == False
assert xyz_there('xyz') == True
assert xyz_there('xy') == False
assert xyz_there('x') == False
assert xyz_there('') == False
assert xyz_there('abc.xyzxyz') == True
assert xyz_there('abc.xxyz') == True
assert xyz_there('.xyz') == False
assert xyz_there('12.xyz') == False
assert xyz_there('12xyz') == True
assert xyz_there('1.xyz.xyz2.xyz') == False
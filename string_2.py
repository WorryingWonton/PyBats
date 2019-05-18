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
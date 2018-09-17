#!/usr/bin/python
import re
import string

code = 'int x3y= 5; b = 3;if(x > 0)'
counter = 33
while code:
    code = str.lstrip(code)
    # print(code)
    if re.match('for(.*)', code):
        print('(1,for)')
        code = code[3:]
        continue
    if re.match('if(.*)', code):
        print('(2,if)')
        code = code[2:]
        continue
    if re.match('then(.*)', code):
        print('(3,then)')
        code = code[4:]
        continue
    if re.match('else(.*)', code):
        print('(4,else)')
        code = code[4:]
        continue
    if re.match('while(.*)', code):
        print('(5,while)')
        code = code[5:]
        continue
    if re.match('do(.*)', code):
        print('(6,do)')
        code = code[2:]
        continue
    if re.match('until(.*)', code):
        print('(29,until)')
        code = code[5:]
        continue
    if re.match('int(.*)', code):
        print('(30,int)')
        code = code[3:]
        # print(code)
        continue


    if code[0] == '+':
        print('(13,+)')
        code = code[1:]
        continue
    if code[0] == '-':
        print('(14,-)')
        code = code[1:]
        continue
    if code[0] == '*':
        print('(15,*)')
        code = code[1:]
        continue
    if code[0] == '/':
        print('(16,/)')
        code = code[1:]
        continue
    if code[0:1] == ':=':
        print('(18,:=)')
        code = code[1:]
        continue
    if code[0] == ':':
        print('(17,:)')
        code = code[1:]
        continue
    if code[0:1] == '<=':
        print('(22,<=)')
        code = code[1:]
        continue
    if code[0:1] == '>=':
        print('(24,>=)')
        code = code[1:]
        continue

    if code[0] == '>':
        print('(23,>)')
        code = code[1:]
        continue
    if code[0] == '<':
        print('(20,<)')
        code = code[1:]
        continue
    if code[0] == '=':
        print('(25,=)')
        code = code[1:]
        continue
    if code[0] == ';':
        print('(26,;)')
        code = code[1:]
        continue
    if code[0] == '(':
        print('(27,()')
        code = code[1:]
        continue
    if code[0] == ')':
        print('(25,))')
        code = code[1:]
        continue

    if code[0] == '#':
        print('(0,#)')
        code = code[1:]
        break

    search = re.match('(^[_a-zA-Z]\w*)(.*)', code)

    if search:
        print('(%d,\'%s\')' % (10, search.group(1)))
        counter = counter + 1
        # print
        code = code[len(search.group(1)):]
        continue

    search1 = re.match('(^[0-9]*)(.*)', code)
    if search1:
        print('(%d,\'%s\')' % (11, search1.group(1)))
        # print(search1.group(1))
        counter = counter + 1
        code = code[len(search1.group(1)):]
        continue
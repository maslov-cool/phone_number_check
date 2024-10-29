mts = [i for i in range(910, 920)] + [i for i in range(980, 990)]
megafon = [i for i in range(920, 940)]
beeline = [i for i in range(902, 907)] + [i for i in range(960, 970)]

try:
    s = input().strip().replace('\t', '')

    if s[0] not in '+8':
        raise TypeError

    for i in range(len(s)):
        if s[i] == '-':
            if s[i - 1] == '-':
                raise TypeError
        elif s[i] == '(':
            if s[i - 1] == '(':
                raise TypeError
        elif s[i] == ')':
            if s[i - 1] == ')':
                raise TypeError
        else:
            if s[i] not in '1234567890- ()+':
                raise TypeError

    if s.find('(') <= s.find(')') and s.count('(') == s.count(')'):
        if s[0] == '8' or s[:2] == '+7':
            s1 = '+7'
        elif s[:2] == '+1':
            s1 = '+1'
        elif s[:4] == '+359':
            s1 = '+359'
        elif s[:3] == '+55':
            s1 = '+55'
        else:
            raise IndentationError

        if s[0] == '8':
            s = s[1:]
            cnt = 1
        elif s[:2] == '+7' or s[:2] == '+1':
            s = s[2:]
            cnt = 1
        elif s[:3] == '+55':
            s = s[3:]
            cnt = 2
        else:
            s = s[4:]
            cnt = 3

        for i in range(len(s)):
            if s[i].isdigit():
                s1 += s[i]
                cnt += 1

        if not (s1[:2] == '+7' or s1[:2] == '+1' or s1[:4] == '+359' or s1[:3] == '+55'):
            raise IndentationError

        if cnt != 11:
            raise ValueError

        if s1[:2] == '+7':
            if int(s1[2:5]) not in mts + megafon + beeline:
                raise SystemError

        print(s1)
    else:
        raise TypeError
except ValueError:
    print('неверное количество цифр')
except SystemError:
    print('не определяется оператор сотовой связи')
except TypeError:
    print('неверный формат')
except IndentationError:
    print('не определяется код страны')

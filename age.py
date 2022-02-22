driving = input('請問你有沒有開過車(Y/N): ')
if driving != 'Y' and driving != 'N':
    print("不要胡亂輸入哦")
    raise SystemExit

age = input('請問你的年齡:')
age = int(age)
if age <= 0:
    print("不要胡亂輸入哦")
    raise SystemExit

if driving == 'Y':
    if age >= 18:
        print('你已經有駕照')
    else:
        print('你冇牌駕駛')
elif driving == 'N':
    if age >= 18:
        print('你可以考車牌')
    else:
        print('等你18歲後就可以考啦')
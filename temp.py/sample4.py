import unicodedata

print(unicodedata.digit('５'))
print(unicodedata.numeric('参'))
print(unicodedata.numeric('Ⅷ'))

msg = '     こんに  ちは  '

print('[' + msg.replace(' ', '') + ']')

msg2 = '''\
こんにちは
こんばんわ
さようなら
'''
print(msg2.splitlines())
print(msg2.splitlines(True))
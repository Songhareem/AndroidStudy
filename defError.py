
# 내 예외 만들기 ( Exception 클래스를 상속받아서 만들다 )

class myError(Exception):
    ''' 연습용 에러 '''


def callError():
    print('call my Error')
    raise myError

try:
    callError()

except myError:
    print('Error call success')


# -*- encoding=UTF-8 -*-
def log(level,*args,**kvargs):
    def inner(func):
        '''
        *无名字的参数
        **有名字的参数
        :param func:
        :return:
        '''
        def wrapper(*args,**kvargs):
            print level,'befor calling',func.__name__
            func(*args,**kvargs)
            print level,'after calling',func.__name__
        return  wrapper
    return inner

@log(level='INFO')
def hello(name,age):
    print 'hello world',name,age
if __name__=='__main__':
    #hello=log(hello)
    #hello()
    hello('zpwust','12 ')
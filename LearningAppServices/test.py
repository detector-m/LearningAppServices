# *-* coding: utf-8 *-

import functools

# def log(func):
#     print('123')
#     # @functools.wraps(func)
#     def ttpper(*args, **kwargs):
#         print('456')
#         return func(*args, **kwargs)

#     return ttpper

# # @log
# def test(p):
#     print(test.__name__ + ' param:' + p)


# test('aa')
# log(test)('aaaa')

# def log_with_param(text):
#     print('1')
#     def decorator(func):
#         print('2')
#         # @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print(3)
#             # print('call %s():' % func.__name__)
#             # print('args = {}'.format(*args))
#             # print('log_param = {}'.format(text))
#             return func(*args, **kwargs)

#         return wrapper

#     return decorator

# tr = 'abc'
# log_with_param(tr)(test)('123456')

# @log_with_param('abc')
# def test():
#     print(test.__name__)
#     print('4')

# test()
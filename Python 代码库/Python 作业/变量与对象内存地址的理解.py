Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list((1,2,3,4,5,6))
[1, 2, 3, 4, 5, 6]
>>> a=[1,2,3,4,5,6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> id(a)
3050090564424
>>> b=list((1,2,3,4,5,6))
>>> id(b)
3050089964360
>>> a==b
True
>>> id(a)==id(b)
False
>>> c='23'
>>> d='23'
>>> id(c)==id(d)
True
>>> d='24'
>>> id(d)==id(c)
False
>>> e=[2,1,3]
>>> f=[2,1,3]
>>> id(e)==id(f)
False
>>> id(e[2])==id(f[2])
True
>>> h=123
>>> i=123
>>> id(h)==id(i)
True
>>> e==f
True
>>> e===f
SyntaxError: invalid syntax
>>> e[0]=1
>>> f
[2, 1, 3]
>>> e
[1, 1, 3]
>>> 

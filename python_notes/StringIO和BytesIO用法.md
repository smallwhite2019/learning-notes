# StringIO:在内存中读写str

```py
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world!')
6
>>> print(f.getvalue())  # getvalue()方法用于获得写入后的str
hello world!

若读取，用str初始化StringIO,再正常读文件。
```


# BytesIO:在内存中读写二进制

```py
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())  #注意，写入的不是str，而是经过UTF-8编码的bytes。
b'\xe4\xb8\xad\xe6\x96\x87'



和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87

```
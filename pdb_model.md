# python 模块
## 1.python 调试器pdb
：单步执行代码,通过命令 python -m pdb xxx.py 启动脚本，进入单步执行模式

：pdb单步执行太麻烦了，所以第二种方法是import pdb 之后，直接在代码里需要调试的地方放一个pdb.set_trace()，就可以设置一个断点， 程序会在pdb.set_trace()暂停并进入pdb调试环境，可以用pdb 变量名查看变量，或者c继续运行

```
import pdb
s = '0'
n = int(s)
pdb.set_trace()  #程序运行到这里会自动暂停
print(10/n)
```
```
                        运行 l(list) 查看代码：
(Pdb) l
  1     import pdb
  2     s = '2'
  3     n = int(s)
  4     pdb.set_trace()  #程序运行到这里会自动暂停
  5  -> print(10/n)
[EOF]
(Pdb) 

                        运行 n 单步执行代码：
(Pdb) n
5.0
--Return--
> e:\github\learning-notes\test.py(5)<module>()->None
-> print(10/n)
(Pdb) 

                        运行 p 变量名 查看变量（必须是运行过的）：
(Pdb) p s
'2'
(Pdb)

                        运行 q 结束调试，退出程序
(Pdb) q
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(10/n)
  File "D:\Program Data\Anaconda3\lib\bdb.py", line 52, in trace_dispatch
    return self.dispatch_return(frame, arg)
  File "D:\Program Data\Anaconda3\lib\bdb.py", line 96, in dispatch_return
    if self.quitting: raise BdbQuit
bdb.BdbQuit
```
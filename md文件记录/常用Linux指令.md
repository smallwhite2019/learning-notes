# Linux常用指令

## --查看磁盘空间大小

```shell
df -h
```

Df命令是Linux系统以磁盘分区为单位查看文件系统，可以加上参数查看磁盘剩余空间信息，命令格式：

```shell
df -hl		# 查看磁盘剩余空间
df -h		# 查看每个根路径的分区大小
du -sh [目录名]	# 返回该目录的大小
du -sm [文件夹]	# 返回该文件夹总M数
du -h [目录名]		# 查看指定文件夹下的所有文件大小（包含子文件夹）
```

## --查找文件命令

常用查找命令主要有`find`和`grep`，两者区别：

- `find`命令是根据<font size=4 >**文件的属性**</font>进行查找，如文件名、文件大小、所有者、是否为空、访问时间等。
- `grep`命令是根据<font size=4>**文件的内容**</font>进行查找，会对文件的每一行按照给定的模式(patter)进行匹配查找。

**find命令:**

<font color=red>基本格式：</font> `find path expression`
1.按照文件名查找

```shell
find / -name httpd.conf			# 在根目录下查找文件httpd.conf，表示在整个硬盘中查找
find /etc -name httpd.conf		# 在/etc目录下文件httpd.conf
find /etc -name '*srm*'			# 使用通配符*(0或者任意多个)。表示在/etc目录下查找文件名中含有字符串'srm'的文件
find . -name 'srm*'				# 表示当前目录下查找文件名开头是字符串'srm'的文件
```

**grep命令:**

<font color=red>基本格式：</font> `find expression`

```shell
grep 'test' d*		# 显示所有以d开头的文件中包含test的行
grep magic /usr/src			# 显示/usr/src目录下的文件（不含子目录）包含的magic的行
grep -r magic /usr/src		# 显示/usr/src目录下的文件（包含子目录）包含magic的行
grep -w pattern files		# 只匹配整个单词，而不是字符串的一部分（如匹配'magic',而不是'magical'）
```

## --查看Linux下隐藏文件命令

`ls -a`	# 查看该文件夹下的所有文件，包含隐藏文件都可查到

## --将一个文件夹或文件夹下所有的内容复制到另一个文件夹

**1.将一个文件夹下的所有内容复制到另一个文件夹下：**

```shell
cp -r /home/packageA/* /home/packageB/
或
cp -r /home/packageA/. /home/packageB/		# 在当前文件夹下用此种方式效果最好
这两种方法效果是一样的。
```

**2.将一个文件夹复制到另一个文件夹下：**

```shell
cp -r /home/packageA /home/packageB
运行命令后`packageB`文件夹下就有`packageA`文件夹啦。
```

**3.删除一个文件夹及其下面的所有文件：**

```shell
rm -rf /home/packageA
# -r 表示向下递归，不管有多少级目录，一并删除
# -f 表示直接强行删除，不作任何提示的意思
```

**4.移动一个文件夹到另一个文件夹下面：**

```shell
mv /home/packageA /home/packageB/
或
mv /home/packageA /home/packageB
这两种方法效果是一样的。
```

**5.移动一个文件夹下的所有内容到另一个文件夹下面：**

```shell
mv /home/packageA/* /home/packageB/
```

## --查看Linux文件夹下文件数量

**查看当前目录下有多少个文件及文件夹需在终端输入：**

`ls | wc -w`

**查看当前目录下有多少个文件需在终端输入：**

`ls | wc -c`

**查看当前文件夹下有多少个文件，多少个子目录需在终端输入：**

`ls -l |wc -l`

**查看当前文件夹中文件的数量，则输入：**

`/bin/ls -l |grep ^-|wc -l`

## --查看Linux当前目录下一个文本文件有多少行

`wc -l test.txt`		# wc>word count缩写

## --删除文件夹下不想要的文件或者目录

```shell
shopt -s extglob
rm -f !(*color12.jpg)		# 删掉除了后缀为color12.jpg的图片文件
rm -f !(*color12.jpg|color11*|color10*)		# 删掉除了后缀为color12.jpg或前缀为color11或前缀为color10的文件，即保留多个不同形式的文件
```

## --Linux查看文件夹下所有的文件并写入txt文档中

```shell
find $paths -name '*.jpg' > $train_file
# 例：
find . -name '*.jpg' > /home/jovyan/jpg_list.txt		# 注意'*.jpg'必须携带单引号，要不然会报下面错误
```

<font color=blue>问题：</font>

```shell
find: paths must precede expression: webfd
Usage: find [-H] [-L] [-P] [-Olevel] [-D help|tree|search|stat|rates|opt|exec] [path...] [expression]
```

```shell
出现这个提示是因为型号代表为当前目录下所有的文件，然后被当作shell展开，这就是网上说的多文件的查找的时候需要增加单引号
```

## --Linux下查看某一文件夹的大小（磁盘使用情况）

**linux查看某一文件夹的大小：**

`du -s 文件夹`

**linux查看某一文件夹以及其各个子目录的大小：**

`du -[-k/m] 文件夹`	# []里面是可选的，-k是以kb形式， -m是以Mb形式

**linux查看当前目录下所有目录及其各个子目录的大小：**

`du -h .`

**Linux系统查看文件夹的大小：**

`ls -lht`	# 查询整个文件夹大小；知道大文件夹和下面小文件夹大小

`du -sh ./file1`	# 能查询单个文件夹大小

## --Linux下的tar压缩解压命令详解

### tar常用指令

```shell
-c:建立压缩档案
-x:解压
-t:查看内容
-r:向压缩归档文件末尾追加文件
-u:更新原压缩包中的文件
# 上述五个是独立的命令，压缩解压都要用到其中一个，可以和别的命令连用但只能用其中一个。下面参数是根据需要在压缩或解压文档时可选的。

-z:有gzip属性的
-j:有bz2属性的
-Z:有compress属性的
-v:显示所有过程
-O:将文件解开到标准输出

# 下面参数-f是必须的
-f:使用档案名字，切记，这个参数是最后一个参数，后面只能接档案名

# 组合指令
tar -cf all.tar *.jpg		# 这条指令是将所有jpg的文件打包成一个名为all.tar的包。-c是产生新的包，-f指定包的文件名。
tar -rf all.tar *.gif		# 将所有的gif文件增加到all.tar包里面去。-r表示增加文件
tar -uf all.tar logo.gif	# 更新原来tar包中logo.gif文件，-u表示更新文件
tar -tf all.tar				# 列出all.tar包中所有文件，-t表示列出文件
tar -xf all.tar				# 解出all.tar包中所有文件，-x表示解压
```

### 压缩

```shell
tar -cvf jpg.tar *.jpg		# 将目录里所有jpg文件打包成jpg.tar
tar -czf jpg.tar.gz *.jpg	# 将目录里所有jpg文件打包成jpg.tar后，并将其用gzip压缩，生成一个gzip压缩过的包，命名为jpg.tar.gz
tar -cjf jpg.tar.bz2 *.jpg	# 将目录里所有jpg文件打包成jpg.tar后，并将其用bzip2压缩，生成一个bzip压缩过的包，命名为jpg.tar.bz2
tar -cZf jpg.tar.Z *.jpg	# 将目录里所有jpg文件打包成jpg.tar后，并将其用compress压缩，生成一个umcomprocess压缩过的包，命名为jpg.tar.Z
rar a jpg.rar *.jpg			# rar格式的压缩，需要先下载rar for linux
zip jpg.zip *.jpg			# zip格式的压缩，需先下载
```

### 解压

```shell
tar -xvf file.tar		# 解压tar包
tar -xzvf file.tar.gz	# 解压tar.gz
tar -xjvf file.tar.bz2	# 解压tar.bz2
tar -xZvf file.tar.Z	# 解压tar.Z
unrar e file.rar		# 解压rar
unzip file.zip			# 解压zip
```

### 总结

```shell
*.tar用`tar -xvf`解压
*.gz用`gzip -d` 或者 `gunzip`解压
*.tar.gz和*.tgz用`tar -xzvf`解压
*.bz2用`bzip2 -d` 或者用`bunzip2`解压
*.tar.bz2用`tar -xjvf`解压
*.Z用`uncomprocess`解压
*.tar.Z用`tar -xZvf`解压
*.rar用`unrar e` 解压
*.zip用`unzip`解压
```

## --linux下常用性能分析工具

### top 工具：对进程时间监控

```shell
数字`1`:监控每个逻辑cpu的状况
`q`退出进程
```

### ps aux | grep XXX:

> - grep(global search regular expression(RE) and print out the line, 全面搜索正则表达式并把行打印出来)：是一种文本搜索工具，它能使用正则表达式搜索文本，并把匹配行打印出来。
> - ps aux:显示所有进程和其状态
> - ps -aux | grep python :查到python的进程
> - kill -9 pid:杀死进程

## --Linux下多个txt文件合并到 一个txt文件

`cat 1.txt 2.txt > 3.txt`		# 合并两个txt文件到3.txt




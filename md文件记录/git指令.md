# git代码简单指令

1.下载代码指令

```shell
git clone http:
```

2.添加、修改、提交代码指令

```shell
git add .
git commit -m "上传代码"
git push origin master
```

3.拉取代码指令

```shell 
git pull
```

4.查看本地分支

```shell
git branch 
其中带星号*的为当前分支
```

5.删除本地分支

```shell
git branch -d [branchname]
```

6.查看所有分支

```shell
git branch -a
```

7.删除远程分支

```shell
git push origin --delete [branchname]
```

8.清理本地无效分支（远程已删除本地没删除的分支）

```shell
git fetch -p
```

9.查看所有提交记录

`git log`

10.查看状态

`git status`
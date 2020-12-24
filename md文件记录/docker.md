# 1.Docker基本概念

## 1.1Docker镜像

Docekr镜像（Image），就相当于一个`root`文件系统。

分层存储

镜像构建时，会一层层构建，前一层是后一层的基础。因此，在构建镜像时，要小心，每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。利用之前构建好的镜像作为基础层，然后进一步添加新的层，以定制自己所需的内容，构建新的镜像。

## 1.2Docker容器

`镜像`和`容器`与面向对象程序设计中的`类`和`实例`一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。

## 1.3Docker Registry仓库

一个Docker Registry中可以包含多个仓库（`Repository`）；每个仓库可以包含多个标签（`Tag`）；每个标签对应一个镜像。

一个仓库会包含同一个软件不同版本的镜像，而标签就常用于对应该软件的 各个版本。我们可以通过`<仓库名>:<标签> (reposity:tag)`的格式来指定具体是这个软件哪个版 本的镜像。若未给出标签，将以`latest`

作为默认标签。

`仓库名`经常以两段式路径形式出现，比如`jwilder/nginx-proxy`，前者往往意味着Docker Registry用户环境下的用户名，后者则往往是对应的软件名。但并非绝对。

# 2.使用镜像

## 2.1获取镜像

从Docker镜像仓库（Docker Hub）获取镜像的命令是`docker pull`。其命令格式为：

```shell
docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]

例如：
docker pull ubuntu:16.04
```

具体选项可通过`docker pull --help`命令看到，这里说下镜像名称格式：

> - Docker镜像仓库地址：格式一般为`<域名/IP>[:端口号]`
> - 仓库名：两段式名称，即`<用户名>/<软件名>`。若不给出用户名，则默认为`library`，也就是官方镜像。

### 2.1.1运行

在有镜像之后，以这个镜像为基础启动并运行一个容器。以上面的`ubuntu:16.04`为例，启动里面的`bash`并且进行交互式操作的话，可以执行下面命令。

```shell
docker run -it --rm \
	ubuntu:16.04 \ 
	bash
```

`docker run`就是运行容器的命令。后面再详解，下面简单看下参数：

> - `-it`：这是两个参数，一个是`-i`：交互式操作，一个是`-t`终端。我们这里打算进入`bash`执行一些命令并查看返回结果，因此我们需要交互式终端。
> - `--rm`：该参数是说容器退出后随之将其删除。手动删除用`docker rm`，此处使用`--rm`可以避免浪费空间。
> - `ubuntu:16.04`：以该镜像为基础来启动容器。
> - `bash`：放在镜像名后的是命令。

在shell下操作，执行了`cat /etc/os-release`，这是Linux常用的查看当前系统版本的命令。最后通过`exit`退出了这个容器。

## 2.2列出镜像

列出已下载的镜像，可使用`docker image ls`命令。

```shell
docker image ls
```

> - 镜像ID（`IMAGE ID`）是镜像的唯一标识，一个镜像可以对应多个标签。

```shell
docker system df
```

### 2.2.1虚悬镜像

特殊镜像，既没有仓库名，也没有标签，均为`<none>`。

```shell
<none>			<none>			00285df0df87			5 days ago 		342M
B
```

原因：新旧镜像同名，旧镜像名称被取消，从而出现仓库名、标签均为`<none>`的镜像。

虚悬镜像可以用下面指令专门显示这类镜像：

```shell
docker image ls -f dangling=true
```

一般来说，虚悬镜像已失去了存在的价值，是可以随意删除的，可以用下面命令删除。

```shell
docker image prune
```

### 2.2.2中间层镜像

为了加速镜像构建、重复利用资源，Docker会利用中间层镜像。默认的`docker image ls`列表中只会显示顶层镜像，若显示包括中间层镜像在内的所有镜像的话，需要加`-a`参数。

```shell
docker image ls -a
```

## 2.3删除本地镜像

删除格式为：

```shell
docker image rm [选项] <镜像1> [<镜像2> ...]
```

### 2.3.1用docker image ls命令来配合

使用`docker image ls -q`来配合使用`docker image rm`，可以成批的删除希望删除的镜像。

比如，删除所有仓库名为`redis`的镜像：

```shell
这种指令不知对与错？
docker image rm (docker image ls -q redis)
```

## 2.4使用Dockerfile定制镜像

Dockerfile是一个文本文件，其内包含了一条条的指令，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。

以之前定制`nginx`镜像为例，使用Dockerfile来定制。在一个空白目录中，建立一个文本文件，并命名为`Dockerfile`：

```shell
创建文件夹：mkdir mynginx
进入文件夹：cd mynginx
创建文件：touch Dockerfile
```

Dockerfile文件内容：

```shell
FROM nginx
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
```

这个Dockerfile很简单，一共就两行，涉及两条指令，`FROM`和`RUN`。

### 2.4.1`FROM`指定基础镜像

所谓定制镜像，就是以一个镜像为基础，在其上进行定制。而`FROM`就是指定基础镜像，因此一个`Dockerfile`中`FROM`是必备指令，并且必须是第一条指令。

### 2.4.2`RUN`指定基础镜像

`RUN`指令是用来执行命令行命令的。`RUN`指令在定制镜像时是最常用的指令之一。其格式有两种：

> - shell格式：`RUN <命令>`，就像直接在命令行中输入的命令一样。例如上例：
>
>   ```shell
>   RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
>   ```

> - exec格式：`RUN ["可执行文件", "参数1", "参数2"]`，更像是函数调用中的格式。

<font color=red size=4>修正错误区，避免釆坑</font>

由于Dockerfile中每一个指令都会建立一层镜像，每一个`RUN`的行为，跟前面建立镜像过程一样：新建立一层，在其上执行这些命令，执行结束后，`commit`这一层的修改，构成新的镜像。

<font color=yellow-red size=3>错误示范指令：</font>

```shell
FROM debian:jessie

RUN apt-get update
RUN apt-get install -y gcc libc6-dev make
RUN wget -0 redis.tar.gz "http://download.redis.io/release/redis-3.2.5.tar.gz"
RUN mkdir -p /usr/src/redis
RUN tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1
RUN make -C /usr/src/redis
RUN make -C /usr/src/redis insatll
```

上面写法创建了4层镜像。这毫无意义，而且很多东西运行时不需要的东西被装进了镜像里，比如编译环境、更新的软件包等。这样导致镜像显得臃肿，而且增加了构建部署的时间也很容易出错。这是很多初学Docker的人长常犯的一个错误。

Unios FS是有最大层数限制的，比如AUFS，曾经是最大不得超过42层，现在是不得超过127层。

<font color=gree size=3>正确示范指令：</font>

```shell
FROM debian:jessie

RUN buildDeps='gcc libc6-dev make' \
	&& apt-get update \
	&& apt-get insatll -y $buildDeps \
	&& wget -0 redis.tar.gz "http://download.redis.io/release/redis-3.2.5.tar.gz" \
	&& mkdir -p /usr/src/redis
	&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
	&& make -C /usr/src/redis \
	&& make -C /usr/src/redis install \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm redis.tar.gz \
	&& rm -r /usr/src/redis \
	&& apt-get purge -y --auto-remove $buildDeps

```

首先，之前所有的命令只有一个目的，就是编译、安装redis可执行文件。因此没必要建立很多层，这只是一层的事情。因此，此处使用`&&`将各个所需指令串联起来。在撰写Dockerfile的时候，要经常提醒自己，这并不是在写Shell脚本，而是<font color=gree-red>定义每一层该如何构建</font>。

并且，这里为了格式化进行了换行。`\`换行方式，`#`行首进行注释。

此外，命令最后添加了清理工作的命令，删除了前期所需的软件，清理了所有下载、展开的文件，还清理了`apt`缓存文件。因此镜像构建时，确保每一层添加有用的东西，任何
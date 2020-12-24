# Linux环境下安装anaconda3

1、下载anaconda2020-02版本，对应python为3.7.6
官网（下载速度慢）：wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
清华源（推荐）： wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2020.02-Linux-x86_64.sh

2、安装(默认根目录下): bash Anaconda3-2020.02-Linux-x86_64.sh
一路yes、Enter，若要修改路径，参照网址：https://www.cnblogs.com/NoTrace/p/12509599.html
自定义安装路径：
    bash Anaconda3-2020.02-Linux-x86_64.sh -p path -u
    例：bash Anaconda3-2020.02-Linux-x86_64.sh -p /opt/anaconda/ -u

3、关闭重启
输入conda是否安装好

3、创建虚拟环境envs，可直接参照步骤2网址

4、下载对应的环境，利用conda安装，方便管理，conda list；
conda安装格式：conda install tensorflow-gpu=1.14.0


 安装tensorflow版本时，要对应cuda版本，其他一样一一对应。

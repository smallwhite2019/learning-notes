# 1、进入虚拟环境
E:\work\project\test-test\GY191208>conda activate yolo

(yolo) E:\work\project\test-test\GY191208>conda env list
# conda environments:
#
base                     D:\Program Data\Anaconda3

inception                D:\Program Data\Anaconda3\envs\inception

opencv                   D:\Program Data\Anaconda3\envs\opencv

yolo                  *  D:\Program Data\Anaconda3\envs\yolo

# 2、安装ipykernel

conda install ipykernel

若上述安装不成功，可选择清华源安装：
conda install --channel 清华源

# 3、再配置jupyter notebook环境

(yolo) E:\work\project\test-test\GY191208>python -m ipykernel install --user --name yolo --display-name "Python [conda env:yolo]"

usage: ipython-kernel-install [-h] [--user] [--name NAME]
                              [--display-name DISPLAY_NAME]
                              [--profile PROFILE] [--prefix PREFIX]
                              [--sys-prefix]

<font color = red > NAME、 DISPLAY_NAME</font>都是你要编辑的名字
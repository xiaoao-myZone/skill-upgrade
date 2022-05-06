## docker

### 安装
see https://docs.docker.com/engine/install/ubuntu/
### docker核心概念
1. Image与Container的关系
2. [Docker 核心技术与实现原理](http://dockone.io/article/2941)
3. docker软件是C/S构型，docker命令是C端

### docker Image

2. 给镜像取别名
`$ docker tag Image_A Image_B`
>> 给Image_A取一个别名,Image_B的IMAGE ID与前者是一样的

4. 创建镜像
`$ docker build .` #在当前目录下找到Dockerfile,并生成image
`$ docker build https://github.com/docker/rootfs.git#container:docker`
`$ docker pull https:localhost:port/aa/bb:version`  这里的version会作为TagName
>> 其中container是分支名,docker是目录名
`$ docker build -t xiaoao/test:mysql .` #将生成镜像命名为xiaoao/test:mysql
5. 推送到远端
`$ docker push https://github.com/docker/rootfs.git#container:docker`
6. 删除镜像(前提不存在引用该镜像的容器)
`$ docker rmi IMAGE_ID/IMAGE_NAME`
7. 启动镜像
`$ docker run tag_name shell_cmd`

#### 查看信息
1. 查看镜像
`$ docker images` 或者 `sudo docker image ls`
2. 查看容器
`docker ps -a`
3. 查看镜像详细信息
`$ docker inspect image_name`

#### 操作
1. 启动镜像（生成一个容器）
2. 关闭一个容器
3. 删除一个容器
4. 进入一个容器




### docker CONTAINER
1. 查看运行中的容器
`docker ps -a`
2. 停止容器
`docker stop container_id/container_name`
3. 删除容器
`docker rm container_id/container_name`
4. 强制停止
`docker kill container_id/container_name`
5. 启动容器
`docker start container_id/container_name`
6. 创建容器
`docker run image`

#### 深入
1. docker run 做了什么?
[Docker run 命令](https://www.runoob.com/docker/docker-run-command.html)
  
  
  -e 设置环境变量， 表达方式为Name=Value
  -v 将宿主机的文件/文件夹共享给容器
  -p 将宿主机的端口共享给容器
  
* 检查本地是否存在指定的镜像，不存在则从公有仓库下载
* 使用镜像创建并启动容器
* 分配一个文件系统，并在只读的镜像层外面挂载一层可读可写层
* 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
* 从地址池分配一个ip地址给容器
* 执行用户指定的应用程序
* 执行完毕之后容器被终止
2. docker run的选项
* -i	以交互模式运行容器，通常与 -t 同时使用
* -t	为容器重新分配一个伪输入终端，通常与 -i 同时使用
* -d	后台运行容器，并返回容器ID
* -v  前者为宿主机目录，后者为容器目录，不存在会被创建（如果已存在呢？）
* -p  端口映射
* --name 为容器起一个名字
* --link  共享被link的容器的环境变量与端口映射
* --env(-e): `docker run -e var1=value1`
* --entrypoint: `docker run -it --rm --entrypoint /bin/bash {image}`可以调试启动失败的容器


## Dockerfile
### ADD
1. 如果是源文件夹，那么表示把这个文件夹里面的东西掏出来放到后面的文件夹中， 如果前者与后者的路径最后加上/，这种操作不会成功
2. `ADD ./code /root/` 这种情况极有可能会覆盖/root，所以ADD的参数条件是source_path expect_path，有别于shell的cp [ADD注意事项](https://blog.csdn.net/thedarkclouds/article/details/81990093)

### WORKDIR
1. 如果之后执行`RUN`命令，会以该目录默认目录

### Notice
1. 如果在Dockerfile中`COPY`, `ADD`等使用宿主机的相对路径，那么这个相对路径是相对于谁？是使用docker build时所在的路径，还是Dockerfile文件所在的目录的路径 docker build path -f dockerfile_path -t name 这种，就是前者，path可以放在build后面也可以放在最后面
2. Dockerfile中想要指定容器内的路径，其默认初始路径是/

## Question
1. docker 每run一次就会产生一个container? （是）





[参考1](https://www.cnblogs.com/lcword/p/13711443.html)
[参考2官方](https://docs.docker.com/engine/reference/commandline/build)

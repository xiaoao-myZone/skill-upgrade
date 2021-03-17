## docker

### docker核心概念
1. Image与Container的关系

### docker Image
1. 查看镜像
`$ docker images` 或者 `sudo docker image ls`
2. 给镜像取别名
`$ docker tag Image_A Image_B`
>> 给Image_A取一个别名,Image_B的IMAGE ID与前者是一样的
3. 查看镜像详细信息
`$ docker inspect image_name`
4. 创建镜像
`$ docker build .` #在当前目录下找到Dockerfile,并生成image
`$ docker build https://github.com/docker/rootfs.git#container:docker`
>> 其中container是分支名,docker是目录名
`$ docker build -t xiaoao/test:mysql .` #将生成镜像命名为xiaoao/test:mysql
5. 推送到远端
`$ docker push https://github.com/docker/rootfs.git#container:docker`
6. 删除镜像(前提不存在引用该镜像的容器)
`$ docker rmi IMAGE_ID/IMAGE_NAME`
7. 启动镜像
`$ docker run tag_name cmd`


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



[参考1](https://www.cnblogs.com/lcword/p/13711443.html)
[参考2官方](https://docs.docker.com/engine/reference/commandline/build)
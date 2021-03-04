## docker


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





[参考1](https://www.cnblogs.com/lcword/p/13711443.html)
[参考2官方](https://docs.docker.com/engine/reference/commandline/build)
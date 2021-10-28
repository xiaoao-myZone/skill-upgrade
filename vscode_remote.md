# VSCODE Remote Connect

## From Windows10 to ubuntu20.04
1. 在windows10上下载安装vscode
2. 下载安装git-bash
3. 在ubuntu上下载安装vscode
4. 在win10上安装扩展Remote Development
5. 在win10上点击左侧的Remote Development的图标
6. 点击“+”， 后面的自然就会了
7. 使用git-bash`ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.235.22`


## 常见问题
1. vscode反复尝试无法连接到目标服务器
重启vscode,或者重启电脑
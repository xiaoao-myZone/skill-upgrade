1. 下载合适的golang编译器版本 [链接](https://golang.google.cn/dl/)
2. 安装, 以linux系统为例, sudo tar -xvzf go1.××.××.linux-amd64.tar.gz -C /usr/local
3. 配置环境, 以ubuntu为例, `export GOROOT=/usr/local/go` 与 `export GOPATH=/home/usrname/projects/golang` 与 `export PATH=$PATH:/usr/local/go/bin:/home/usrname/projects/golang`, 之所以将GOPATH放在用户目录下, 是因为方便用vscode下载GO的各种工具
4. vscode配置, 安装go插件, 认准Go Team at Google
5. 进入vscode设置, 搜索go.go, 在用户区设置Gopath与Goroot, 与步骤3中的保持一致
6. ctrl + shift + P, 搜索Go: Install/Update Tools, 安装所有插件
7. 用一下脚本测试是否安装正确
hello_world.go
```
package main
import "fmt"
func main(){
	fmt.Println("hello, wolrd")
}
```
`go run hello_world.go`

8. 快捷键(自动联想)配置参见[链接](https://www.cnblogs.com/nickchen121/p/11517473.html)

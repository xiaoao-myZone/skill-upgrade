[逐行读取指令并执行](https://www.cnblogs.com/lemon-le/p/14037619.html)
`while read -r line ; do echo -e "\033[41m$line\033[0m" && eval $line && echo -e "\n\033[42msuccess\033[0m"; done < shell`



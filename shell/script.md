
## 一般性规则：
1. 要么回车断句， 要么用分号
2. =号前后不能有空格
3. shell是从左向右解析， 因此后面的执行部分不能影响前面  [参考](https://www.cnblogs.com/manqing/p/6675467.html)

## 变量
1. 名字规则基本与C一致
2. 引用$Var或者${Var}，一般用后者比较规范
3. 只读命令 readonly Var
4. 删除变量unset Var
5. 作用域
6. 字符串长度${#string}
7. 字符串切片${string:1:4}注意从0开始计数， 第4个是可以取到的
7. 所以检索变成${string:2:2}
8. 如果后一个省略默认为最大长度${string:1},前一个省略默认为从第一个开始${string::4}
9. 超出范围不会报错

## 如何进行循环
1. while 
while condition1
do
    cmd1
done
2. for
for loop in 1 2 3 4
do
    echo "The value is: $loop"
done

for((i=1;i<=5;i++));do
    echo "这是第 $i 次调用";
done;

>> 没有break吗？（有的）还有continue

3. until
until condition
do
    command
done
## 如何处理字符串，比如拼接， 组个搜索

## 如何处理输入输出
### 输入参数
1. 引用输入参数 $1, $2, $3 ...
2. 应用输入参数个数 $#
3. 对shell命令输入参数 
cat << EOF
hello
world
EOF
但是对于git pull/push 以及mysql -u root -p没有用, 因为它们不像cat一样立即起作用
### 输出 
1. $?可知最近一个指令的退出状态
2. 输入到文件cat 'hello, world' > file_name (>是覆盖写入， >>是在底部追加)
## 如何进行判断
if condition1
then
    command1
    command2
elif condition2 
then 
    command2
else
    commandN
fi
1. condition有什么要求， 或者是shell中的bool值是怎样的
    -eq     //equal  等于

    -ne     //no equal 不等于

    -gt      //great than 大于

    -lt       // low than  小于

    ge      // great and equal 大于等于，注意没有"-"

    le      //low and equal 小于等于，注意没有“-”



[菜鸟shell教程](https://www.runoob.com/linux/linux-shell-passing-arguments.html)
[字符串的比较](https://www.jb51.net/article/56559.htm)
[逐行读取指令并执行](https://www.cnblogs.com/lemon-le/p/14037619.html)
`while read -r line ; do echo -e "\033[41m$line\033[0m" && eval $line && echo -e "\n\033[42msuccess\033[0m"; done < shell`
[shell read -r](https://www.runoob.com/linux/linux-comm-read.html)
[逐行读取文件](https://blog.csdn.net/wdz306ling/article/details/80029829)
[检查当前shell脚本被运行的权限](https://blog.csdn.net/rikeyone/article/details/88723418)



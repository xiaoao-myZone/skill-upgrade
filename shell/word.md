# Word

## 单引号与双引号
1. 在echo中单引号类似于window系统中python的在字符串前的r前缀, 其中的特殊符号不会被转移
2. 双引号会转义很多特殊符号, 比如$Var表示引用变量

## 文档的操作

### 1. 写入
1. `>` 与 `>>`
`>`将字符数据覆盖将写入的文件
`>>`会在文档中继续写入, 新写入的字符不会换行

### 2. 读出
1. cat
2. sed


### 3. sed
1. 就地修改 -i 
2. (行操作)删除 `sed '2d' file_name` 删除第二行
3. (行操作)替换 `sed '1c hello' file_name` 
`sed '1,3c hello' file_name` 将1-3行用hello替换
4. (行操作)插入 `sed '3a new-line' file_name` 在第三行下插入新行`new-line`
`sed '$a yes' file_name`  尾行插入

### 4. sed如何清空一行
貌似无法将一行替换成
`sed "1c \ \n"` 就是\n的前面必须要有一个字符并且不是是空格, 还需要是\空格

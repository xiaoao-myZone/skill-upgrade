# git


## clone
1. `git clone xxxx.git -b branch_name` clone貌似没办法只下载一个分支
2. `git config --global http.postBuffer 524288000` 
    当仓库比较大的时候,可能会出现'fatal: The remote end hung up unexpectedly'
    执行这一行再clone

## 添加与删除
[图解Git工作原理](https://mp.weixin.qq.com/s/hLjMxQQsRI2N9nzhQ5LfRQ)
### 工作区 --> 暂存区
1. `git add filename`
2. `git add .`  添加所有 

### 暂存区 --> 工作区
1. `git reset HEAD filename`
2. `git reset HEAD` 清除所有 

### 工作区 --> system
1. `git checkout -- filename`
2. `git clean -d -f`   清除工作区所有未跟踪项目
3. `git checkout -- .` 取消工作区所有修改

### 暂存区 --> 历史记录
1. `git commit -m "messgae"`

### 历史记录 --> 暂存区
1. `git rm --cache filename` 会在工作区保留

### 强制修改
1. `git reset --hard commitId filename`
2. `git reset --hard HEAD` 清除所有修改


### 选择特定文件
将所有修改的py文件加入暂存区
`git status | grep -o "\S\+\.py$" | xargs git add`
`git add "*.py"`
## 管理commit
1. 修改当前commit的信息 `git commit --amend`
2. [用rebase合并多个commit](https://www.cnblogs.com/yxhblogs/p/10527271.html)

## 管理分支
`git branch -D branchname`
`git push origin --delete branchname` push后面像是在发送一段指令

## 暂存
1. 将工作区改动暂存，并将工作区恢复最近版本 
`git stash`
2. 弹出最近的一次暂存
`git stash pop`
3. 恢复最近的一次暂存，但是不删除这个暂存
`git stash apply`
4. 查看所有暂存
`git stash list`
5. 恢复某一次次暂存，但是不删除这个暂存
`git stash apply stash@{0}`

## 标签
1. 创建当前分支的最新commit id 的tag
`git tag tagName`
2. 为某一commit id 创建一个tag
`git tag -a tagName commitId`
3. 查看某一个tag
`git show tagName`
4. 推送
`git push origin tagName`
5. 推送所有
`git push origin --tags`
6. 删除tag
`git tag -d tagName`
7. 删除远程tag
`git push origin: tagName`
8. the more [链接](https://blog.csdn.net/jdsjlzx/article/details/98654951)

## 查看基本信息
1. `git status`
2. `git rev-parse HEAD` # 查看当前的commit id


## 设置
1. 查看git的所有设置
`git config --global --list` --system --local
2. 查看某个值的设置
`git config --global --get user.email`
3. 删除某个值的设置
`git config --global --unset user.mail`
4. 换源
`git remote remove origin && git remote add origin https://github....`
5. 设置global变量
`git config --global --add user.email name@example.com`
6. ultimate set
`git config --global -e`
7. 更换默认编辑器
`git config --global core.editor vim`
8. 缓存密码
`git config --global credential.helper store`
输入一次密码后就会缓存
9. 清除缓存
`git credential-manager uninstall`

## 源
1. 换源
`git remote set-url origin git@github.com:xiaoming/my-repo.git`
2. 查看源
`git remote get-url origin` # tab 竟然无法显示
3. ultimate set
`vim .git/config`
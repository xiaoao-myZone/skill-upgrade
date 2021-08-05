# git


## clone
1. `git clone xxxx.git -b branch_name` clone貌似没办法只下载一个分支
2. `git config --global http.postBuffer 524288000` 
    当仓库比较大的时候,可能会出现'fatal: The remote end hung up unexpectedly'
    执行这一行再clone
## 删除
1. 取消工作区所有修改
`git reset --hard HEAD` # 后面可以跟文件
`git checkout -- .`
&#160;
2. 删除工作区中的未跟踪文件
`git clean -d -f`
&#160;
3. 取消工作区某个文件改动
`git checkout -- filename`
&#160;
4. 删除暂存区某个文件 # 不会改动工作区， 但是会在暂存区删掉， commit后就会真的删掉
`git reset HEAD filename`
&#160;
5. 删除暂存区所有文件
`git reset HEAD`

6. 删除分支
`git branch -D branchname`
`git push origin --delete branchname` push后面像是在发送一段指令

7. 删除已经commit的文件，但是在工作区保留
`git rm --cache fileName`
## 添加
1. 将所有修改的py文件加入暂存区
`git status | grep -o "\S\+\.py$" | xargs git add`
`git add "*.py"`


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
如果不喜欢默认的编辑器，可以通过`git config --global core.editor vim`修改
7. 缓存密码
`git config --global credential.helper store`
输入一次密码后就会缓存
8. 清除缓存
`git credential-manager uninstall`

## 源
1. 换源
`git remote set-url origin git@github.com:xiaoming/my-repo.git`
2. 查看源
`git remote get-url origin` # tab 既然无法显示
3. ultimate set
`vim .git/config`
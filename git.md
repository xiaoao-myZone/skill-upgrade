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
4. 删除暂存区某个文件
`git reset HEAD filename`
&#160;
5. 删除暂存区所有文件
`git reset HEAD`

6. 删除分支
`git branch -D branchname`
`git push origin --delete branchname` push后面像是在发送一段指令

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

## 查看状态
1. `git status`


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

## 源
1. 换源
`git remote set-url origin git@github.com:xiaoming/my-repo.git`
2. 查看源
`git remote get-url origin`
3. ultimate set
`vim .git/config`
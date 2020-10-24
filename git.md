# git

## 删除
1. 取消工作区所有修改
`git reset --hard HEAD`
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
`git push origin --delete branchname`

## 添加
1. 将所有修改的py文件加入暂存区
`git status | grep -o "\S\+\.py$" | xargs git add`
`git add "*.py"`
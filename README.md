# Python Flask と React を試した

### 作業場所
```
/home/nisigaki/python01
```

### workspace05
workspace04 の成果物を Heroku へデプロイ

### フォルダ内に submodule が含まれる場合のこと
- git add でこのメッセージ
```
warning: adding embedded git repository: workspace05
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint:   git submodule add <url> workspace05
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint:   git rm --cached workspace05
hint:
hint: See "git help submodule" for more information.
nisigaki@AMD-win11-64:~/python01$
```

- なぜなら、workspace05 は git 管理下にあるから
```
nisigaki@AMD-win11-64:~/python01/workspace05$ git remote -v
heroku  https://git.heroku.com/morning-peak-09108.git (fetch)
heroku  https://git.heroku.com/morning-peak-09108.git (push)
```

- そこで
```
git submodule add https://git.heroku.com/morning-peak-09108.git workspace05
```




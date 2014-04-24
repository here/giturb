

# http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
import requests

# http://amoffat.github.io/sh/
from sh import git, curl

# Python Git Libraries
# Gittle -- soft fail requires --allow-external mimer
# https://github.com/FriendCode/gittle
# Pygit2 -- fail could not install with py3
# https://github.com/libgit2/pygit2
# GitPython -- fail incompatible with py3?
# https://github.com/gitpython-developers/GitPython
# from git import *

d = '/home/known/a/code/py/pyreqgit/weburbanist.com/'
f = 'index.html'
repopath = d

g = git.bake(_cwd=repopath)
c = git.bake(curl)

req = requests.get('http://weburbanist.com')

out = open(d+f,'w',encoding='utf-8')
out.write(req.text)
# out.flush()
out.close()

g.commit('-a','-m','auto')

# GitPython
# repo = Repo(d);
# if ( repo.is_dirty(1,1,1) ) {
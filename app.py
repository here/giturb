
# Fix relative import fails for imported libraries

# http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# fails when run from cron due to py2.7 on sys and this py3.3 in venv
import requests

# http://amoffat.github.io/sh/
from sh import git, curl

# dir, file, repopath
d = '/home/known/a/code/py/pyreqgit/weburbanist.com/'
f = 'index.html'
repopath = d

# git, curl
g = git
g = g.bake(_cwd=repopath)
c = curl

# req
req = requests.get('http://weburbanist.com')
# using sh.curl
# encoding is different
# req = c.call('http://weburbanist.com')

# write to git

## write to git


## write to file
out = open(d+f,'w',encoding='utf-8')
out.write(req.text)
# out.flush()
out.close()

## commit
	# todo: check repo status
  # todo: functional to receive api hit

# g.commit('-a','-m','auto')

## loop by cron or trigger

##### end 


# https://docs.python.org/2/install/index.html#modifying-python-s-search-path
# fix import module path error for pyvenv-3.3 from cron 
# site.py in standard lib
# import sys
# sys.path.append('/www/python/')


# Other Python Git Libraries
# Gittle -- soft fail requires --allow-external mimer
# https://github.com/FriendCode/gittle
# Pygit2 -- fail could not install with py3
# https://github.com/libgit2/pygit2
# GitPython -- fail incompatible with py3?
# https://github.com/gitpython-developers/GitPython
# from git import *

# GitPython
# repo = Repo(d);
# if ( repo.is_dirty(1,1,1) ) {
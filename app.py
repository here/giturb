#!/home/known/a/code/py/pyreqgit/env3.3/bin/python

import sys
sys.path.insert(0,'/home/known/a/code/py/pyreqgit/env3.3/lib/python3.3/site-packages');

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

# targets

# http://en.wikipedia.org/w/api.php
# action=query
# prop=revisions
# format=json
# rvprop=timestamp|content
# Parameters:
#   rvprop              - Which properties to get for each revision:
#                          ids            - The ID of the revision
#                          flags          - Revision flags (minor)
#                          timestamp      - The timestamp of the revision
#                          user           - User that made the revision
#                          userid         - User id of revision creator
#                          size           - Length (bytes) of the revision
#                          sha1           - SHA-1 (base 16) of the revision
#                          contentmodel   - Content model id
#                          comment        - Comment by the user for revision
#                          parsedcomment  - Parsed comment by the user for the revision
#                          content        - Text of the revision
#                          tags           - Tags for the revision
# rvlimit=10
# titles=Pull


# write to git

## write to git


## write to file
out = open(d+f,'w',encoding='utf-8')
out.write(req.text+'b')
# out.flush()
out.close()

## commit
	# todo: check repo status for new files etc
  # todo: functional to receive api hit
  # todo: test '--allow-empty'

g.commit('-a','--allow-empty','-m','auto')

## loop by cron or trigger

##### end active code

## Notes

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

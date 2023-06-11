#!/usr/bin/env python3
# coding: utf-8


import os
import subprocess


def make_files(project):
    os.mkdir(project)
    os.chdir(project)

    with open('README.md', 'w'):
        pass

    with open('.gitignore', 'w') as f:
        f.write('__pycache__/')

    os.mkdir(project)

    src_init = os.path.join(project, '__init__.py')
    src_main = os.path.join(project, '__main__.py')

    with open(src_init, 'w'):
        pass

    with open(src_main, 'w') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# coding: utf-8')

def git_setting(project, username):
    repository = 'github:' + username + '/' + project + '.git'

    cmd = 'git init'
    subprocess.run(cmd.split())

    cmd = 'git remote add origin ' + repository
    subprocess.run(cmd.split())

def main():
    project = input('Project name: ')
    git_username = input('Git username: ')

    make_files(project)
    git_setting(project, git_username)


if __name__ == '__main__':
    main()

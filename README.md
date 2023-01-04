<p align="center">
  <img src="https://user-images.githubusercontent.com/61448492/210484107-83ddd68c-3b44-4751-9b97-62139f21ad27.png">
</p>

# Project launcher for Python

Project launcher for Python launches a simple project: makes direcroties, files, and sets git. When a project is launched by this launcher, the git setting is done too, so you can `push` your reopsitory of the project without `git remote add ...` setting.

As executing this launcher, directories and files are made as below:

<img src="https://user-images.githubusercontent.com/61448492/210484115-38afe665-2295-41e2-86e0-dc47d787b3b0.png" height="40%" width="40%">

# Usage

Set `PYTHONPATH` and command alias to `~/.bashrc`.

``` bash
export PYTHONPATH=$PYTHONPATH:/path/to/project-launcher-for-python/
alias project-launcher='python3 -m project-launcher-for-python'
```

Read `~/.bashrc` or reboot.

``` bash
$ source ~/.bashrc
```

Execute `project-launcher` command on the directory you like.

``` bash
$ project-launcher
```

# Example

<img src="https://user-images.githubusercontent.com/61448492/210485776-80073555-cd89-42c4-a659-8a4b1a2595f1.png">



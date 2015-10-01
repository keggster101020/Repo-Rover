# Repo-Rover
______

## Do you use git?
______
Does the thought of un-clean [git](http://git-scm.com/docs/gittutorial) repositories keep you up at night? If
you have a lot of git repositories on your computer, chances are,
lurking on your harddrive is a un-committed file, waiting to cause a
merge conflict, slowing down the
development process and putting your team behind.
Do not fear, *Repo-Rover* is here!

## Repo-Rover Overview
______
**Repo-Rover** is a command-line tool used to track the statuses of your
local git repositories! You may be thinking, "Don't we have a
`git-status` to do that exact thing?" The answer is, your are exactly
right! **Repo-Rover** is a `git-status` for your entire collection of
git repositories on your machine! Give **Repo-Rover** a path and it will
return to you the status of every single git repository under that path
to a clean, material design, web-page! Awesome tool, right? [Give it a try](https://github.com/keggster101020/Repo-Rover/archive/master.zip)!

## Requirements
______
+ Python v2.0 < v3.0
+ Git v1.9.X (at least)

## Preparation Overview
______
_The following bulleted points will be covered in more detail below._
+ Launch Terminal
+ Check that you have `Python` installed
+ Install **Repo-Rover**
+ Usage

### Launching Terminal
______
Our system, in its current state, requires you to use the
Terminal Application (OSX, Linux).
Launching the Terminal will put you in your home directory.
To make installing and using our system as simple for you as possible,
we will assume that it is okay that you install your system in your home
directory. We will not provide you with the shell commands necessary
to navigate Terminal as this is not necessary in the usage of our system.
After launching either Terminal,
you may proceed with the rest of this tutorial on using `reporover`.

### Check that you have Python installed
______
To check whether or not you have [Python](https://www.python.org/)
installed type the following command in your Terminal.
Our system has been tested on a machine with Python version 2.7.9. We
will continue to work on making it Python 3 compatible.

```
# Python Verion
python --version

# Your version may differ
# => Python 2.7.9
```

### Installation
______
The easiest way to get our system is to clone
the repository to your local machine. If you are familiar with git and
cloning repositories use the following command. Otherwise, if you are
interested in learning git, please refer to this
[link](https://try.github.io/levels/1/challenges/1) for a wonderful
git tutorial that explains the basics of using git as a tool for version
control.

```
# clone Repo-Rover to your local machine using git
git clone https://github.com/keggster101020/Repo-Rover.git
```
_Note: Upon special request, we can provide our system via Universal
Serial Bus (USB), Compact disc (CD), and even [Floppy
Disk](https://www.youtube.com/watch?v=ba14uJFvqMs)._

#### Installing *with* `sudo` Privileges
After cloning the repository, you can install `reporover` with the
following command (assuming that you have `sudo` privileges).

```
# OSX/Linux Installation
sudo ./setup.py install
```

#### Installing *without* `sudo` Privileges
```
# OSX/Linux Installation
python setup.py install --user

# set your path so that you can run `reporover`
PATH=$PATH:~/.local/bin
```

### Usage
______
Print the help menu displaying all of the excepted command-line
arguments
```
# display accepted command-line args
reporover -h
```

Find git repositories in the directory that you are currently in
```
# find git repos in the current directory and output to html
reporover

# find git repos in the current directory and output to terminal
reporover -n
```

Find git repositories in a given directory
```
# find git repos in a given dir and output to terminal
reporover -n path/to/dir

# find git repos in a given dir and output to html in the given dir
reporover path/to/dir -o path/to/html/dir
```

## Trouble Installing or Running on [Windows](https://www.youtube.com/watch?v=-NsXHPq71Bs)?
______
Since Python is cross-platform, our system should work on Windows.
However, you will have to figure out how to install as well as set your
`Path` variable to point where `reporover` installed to.

# Requirements
______
_For the full list of requirements see_
[requirements](https://github.com/keggster101020/Repo-Rover/blob/master/docs/RequirementsAnalysis.md).

# Feedback
______
If you like it, hate it, or have some ideas for new features, submit a
issue request
[here](https://github.com/keggster101020/Repo-Rover/issues) and we will
respond as soon as possible! Again, we do not currently support
[Windows](https://www.youtube.com/watch?v=Kwma71yl8mU).

# Contributors
______

+ Keegan Shudy ([keggster101020](https://github.com/keggster101020))
+ Cody Kinneer ([kinneerc](https://github.com/kinneerc))
+ Colton McCurdy ([mccurdyc](https://github.com/mccurdyc))
+ Michael Camara ([camaram88](https://github.com/camaram88))
+ Hanzhong Zheng ([victorzhz](https://github.com/victorzhz))
+ Jacob Hanko ([hankoj](https://github.com/hankoj))

# License
______

The MIT license (MIT)

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

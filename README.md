# Repo-Rover
______

## Do you use git?
Do you use [git](https://git-scm.com/) as a way to manage versions of
your software or documents? If so, I imagine you have a number of git
repositories on your local computer. Some of these repositories may not
be as clean as you may have thought! Now, you can use **Repo-Rover** to
detect these un-committed, un-tracked, or un-pushed files!

## Repo-Rover Overview
**Repo-Rover** is a command-line tool used to track the statuses of your
local git repositories! You may be thinking, "Don't we have a
`git-status` to do that exact thing?" The answer is your are exactly
correct! **Repo-Rover** is a `git-status` for your entire collection of
git repositories on your machine! Give **Repo-Rover** a path and it will
return to you the status of every single git repository under that path
to a clean, material design webpage! Awesome tool, right? Give it a try!

## Requirements
Python v2.7.X (at least)

## Preparation Overview
_The following bulleted points will be covered in more detail below._
+ Launch Terminal/Command Prompt
+ Check that you have `Python` installed
+ Install **Repo-Rover**
+ Usage

### Launching Terminal/Command Prompt
Our system, in its current state, requires you to use the
Terminal Application (OSX, Linux) or Command Prompt (Windows).
Launching the Terminal or Command Prompt will put you in your home directory.
To make installing and using our system as simple for you as possible,
we will assume that it is okay that you install your system in your home
directory. We will not provide you with the shell commands necessary
to navigate Terminal as this is not necessary in the usage of our system.
After launching either Terminal or the Command Prompt,
you may proceed with the rest of this tutorial on using **Repo-Rover**.

### Check that you have Python installed
To check whether or not you have [Python](https://www.python.org/)
installed type the following command in your Terminal/Command Prompt.
Our system has been tested on Python version 2.7.9 and Python 3.4.3.

```
# Python Verion
python --version

# Your version may differ
# => Python 2.7.9
```

### Installation
The easiest way to get our system is to clone
the repository to your local machine. If you are familiar with git and
cloning repositories use the following command. Otherwise, if you are
interested in learning git, please refer to this link for a wonderful
git tutorial that explains the basics of using git as a tool for version
control.

```
# clone Repo-Rover to your local machine using git
git clone git@github.com:keggster101020/Repo-Rover.git
```
_Note: Upon special request, we can provide our system via Universal
Serial Bus (USB), Compact disc (CD), and even Floppy Disk._

After cloning the repository, you can install **Repo-Rover** with the
following command:

```
# installing reporover executable
sudo ./setup.py install
```

### Usage
Find git repositories in the directory that you are currently in
```
# find git repos in the current directory
reporover
```
Find git repositories in a given directory
```
# find git repos in a given dir
reporover "path/to/dir"
```

# Requirements
_For the full list of requirements see_
[requirements](https://github.com/keggster101020/Repo-Rover/blob/master/docs/RequirementsAnalysis.md).

# License
______

We have released **Repo-Rover** under the MIT license. Which basically means
you can use it however you want.
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

# Feedback
______
If you like it, hate it, or have some ideas for new features, submit a
issue request
[here](https://github.com/keggster101020/Repo-Rover/issues) and we will
respond as soon as possible!

# Contributors
______

+ Keegan Shudy (keggster101020)
+ Cody Kinneer (kinneerc)
+ Colton McCurdy (mccurdyc)
+ Michael Camara (camaram88)
+ Hanzhong Zheng (victorzhz)
+ Jacob Hanko (hankoj)



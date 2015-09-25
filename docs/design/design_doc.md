# System Design

## Overview

The system will take the full path of the directory that the user wants to scan as an input of the system. Then it will automatically go to the directory and scan the directory to count the number of git repositories in that directory and prints out in the terminal window. The system implements the feature that has the same function as "git status" command. It allows user to see the issues that files with changes are not staged for commit and the commit has not been pushed. The system is able to print these issues out in the terminal window. In addition, the system also prints out the relative path of the files that have these issues in the report. In order to bring convenience for user, the system is able to generate a web report named "Git Repository Report" that contains the information of the directory that user's enter to our system. 

## Input
The path of directory, which is a String datatype, will be the input for the system. We implement our system by Python programming language. In order to make sure that our system can accurately locate the directory that user wants to scan, the format of the input must be written in a certain format. For example, If the user wants to scan for git repository in directory "cs280-lab4Team1" under the directory "cs280" and home directory, the input should be the path of the directory and written in the format of "/home/z/zhengh/cs280/cs280-lab4Team1" as a parameter for running the program and it will print that "I found + (the number of repositories) + git repository" in the terminal. If the system can not locate the directory or the user doesn't enter the path of the directory in a correct format, the system can print out "I found 0 git repositories." in the terminal. If the user runs the program without given any parameters, the system will automatically scan the current directory and count the number of repositories in the current directory. 


## Output
The system can generate two reports of the summary of the directory that the system scans. For terminal report, the report firstly prints the number of repositories that exit in the directory. Then, it prints out the type of the issue and the files that have the issue. For example, if the user makes some change in the file and he forgets to push the file, the issue after running the our system is "changes not staged for commit" in a red color and then it prints out the relative paths of these files to help user to find these files . However, if there is no issue found in that directory, it will print "no issue found" in a GREEN color. For html report, it has a block in the center of the page that contains all the issues in the directory. It prints out the path of the directory that user enters and the information of the issues, which are the same of terminal report. 

## Directory Scanning and Status Detection
The main logical of our system is to go to the directory that is user's input and scan all files in that directory. In our system, it has a function that can iterate through all names of folders or files. If there is a folder named ".git ", our system counts this folder is a git repository and add the path of the file in the list that contains all paths of git repository. Then, our system has a function that returns the list and size of the list is the number of git repositories in that directory. To determine the status of files in the repository, our system has the function to ckeck the the file's stauts to see if there are some issues int the repository that user has not noticed. Hence, user can run our system to check the status of their repositories instead of run "git status" command at each directory. 

\newpage

![System Structure](diagrams/design_dia.pdf)

## States Explanation
+ find_git_repos(Directory): it will get all of the git repos listed under the given directory.
+ git_issues(Directory): it runs the command "git status" to attain the status of the given directory.
+ has_issues(): check the git status message to see if there are changes that haven't been added or committed or pushed.
+ write_report(): Write all the output to a nice little html file. 

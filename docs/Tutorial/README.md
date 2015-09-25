# A Quick Tutorial For NAME
______

## Brief Summary of NAME
NAME is a currently a command line cline that can provide a brief summary report for user given directory. NAME can automatcally locates the user given directory in the range of hundreds and thousands directories and enter that directory. It also has the ability to scan through all files in that directory to count the number of repositories in that given directory. Then, NAME can determine the current status of the given directory by providing the information of files with changes that are not been commited or staged files that are not pushed. After the NAME's automatical diagnois of the given directory, it is able to generate the a HTML web report to users so that they can clearly see the issues that exist in the given directory and help the users to fix these issues. As a software developer, merge conflictions is a very common issue for using repository to share files with software development team members. The purpose of our product is to help developers to avoid this issue and improve the efficiency of software developing process.


## Requirements
* Python

## Development Notes

The NAME is developed for users who use Linux operating system and Git repository software. 


## Installation
The currently only way to install NAME is to clone the repository to your local machine, If you are familiar with Git and clonning repositories, please use the following command "git clone git@bitbucket.org:victorzhz/cs280-lab4team1.git". After finishing cloning the git repository, Make sure you can go to the "/src" directory and find the Python file named fidGitDir.py. 



## Tutorial of How to Run NAME

+ Step1: Open a terminal window and go to the directory where fitGitDir.py locates. 
+ Step2: Run the command "Python fidGitDir.py + the path of directory you want to scan" or user can only use the command "Python fidGitDir.py" to scan for the directory where you current at. 
+ Step3: After running the program, it will prints a short report about your current repository status at the terminal window. In the report, it includes the information that the number of Git repositories found in the given directory and the issues found in given directory. In order to attract user's attention, the issue context in the report is marked with different color. If there is a issue found in the directory, it will tell the user what the issue is and prints out the path of file that causes this issue. The path of the file is marked in red color to alarm user. However, if there is no issue found in the directory, it will tell the user that your given directory is safe and it is marked in green color. NAME is also can generate a HTML web report that stores in "/webReport" directory. The user can see the detailed report of given repository by openning clean.html file. 




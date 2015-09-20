import os
import subprocess
import re

"""
This method will get all of the git repos listed under the given 
directory

param: directory path
retuns: list
"""
def find_git_repos(dir):
    repos = []
    for (path, dirs, files) in os.walk(dir):
        for directory in dirs:
            if directory == ".git":
                repos.append(path)
    return repos

"""
This will run git status for all the git repos
and compile a list of repo dirs that have
any staged commits

param: list
return: list or boolean
"""
def git_status(repos):
	report_stats = []
	for repo in repos:
		os.chdir(repo)
		status = subprocess.check_output(['git', 'status'])
		if has_issues(status):
			print [False, repo, status] #debug output
			#run_report(repo,[status])
		print [True, repo] #also debug
"""
check the git status message to see if there are changes 
that haven't been added or committed or pushed
"""
def has_issues(message):
	issues = []
	changes_staged = "changes not staged for commit"
	changes_committed = "changes to be committed"
	changes_pushed = "your branch is ahead of"
	
	changes_not_committed = changes_committed in message.lower()
	committed_not_pushed = changes_pushed in message.lower()
	changes_not_added = changes_staged in message.lower()
	#if changes_not_added:
		#get_file(message)
	
	return changes_not_committed or committed_not_pushed or changes_not_added #this will be removed 

#def get_file(message):
	
				
def main():
	print "Enter the full directory you want to scan: "
	initial_directory = raw_input()
	repos = find_git_repos(initial_directory)
	print repos
	print git_status(repos)
	

	
if  __name__ =='__main__':main()
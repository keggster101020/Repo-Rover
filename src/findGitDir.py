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
		issues = has_issues(status)
		if issues[0]:
			print issues #debug output
		else:
			print [True, repo] #also debug
"""
check the git status message to see if there are changes 
that haven't been added or committed or pushed
"""
def has_issues(message):
	issues = []
	bool_issues = False
	changes_staged = "changes not staged for commit"
	changes_committed = "changes to be committed"
	changes_pushed = "your branch is ahead of"
	
	changes_not_committed = changes_committed in message.lower()
	committed_not_pushed = changes_pushed in message.lower()
	changes_not_added = changes_staged in message.lower()
	if changes_not_added:
		bool_issues = True
		file_name = get_file(message)
		issues.append("changes not staged for commit : %s" % file_name)
	if committed_not_pushed:
		bool_issues = True
		file_name = get_file(message)
		issues.append("You have a commit that you have not pushed : %s" % file_name)
	if changes_not_committed:
		bool_issues = True
		file_name = get_file(message)
		issues.append("Changes to be committed %s" % file_name)
	
	return [bool_issues, issues]
	
	#return changes_not_committed or committed_not_pushed or changes_not_added #this will be removed 
"""
Gets the file that is being staged in git
"""
def get_file(message):
	file_index = []
	split = message.split()
	count_mod = split.count('modified:')
	
	for i in range(0, count_mod):
		file_index.append(split[split.index('modified:',split.index('modified:')) + 1])
	return file_index
	
				
def main():
	print "Enter the full directory you want to scan: "
	initial_directory = raw_input()
	repos = find_git_repos(initial_directory)
	print repos
	print git_status(repos)
	

	
if  __name__ =='__main__':main()
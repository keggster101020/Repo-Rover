#!/usr/bin/env python

"""
Author: Keegan Shudy, Cody Kinneer
"""

import os
import subprocess
import re
import shutil
import sys
import webbrowser
import pkgutil
import tempfile

# ANSI color codes
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

totalRepos=0; #setup the counter for the total number of repositories
cleanRepos=0; # setup the counter for the total number of clean repositories
dirRepos=0; # setup the counter for the total number of repositories that have problems

temp_dir = tempfile.mkdtemp()


owd = os.getcwd()
"""
This method will ge all of the git repos listed under the given
directory

param: directory path
retuns: list
"""
def find_git_repos(dir):
    global totalRepos;
    repos = []
    for (path, dirs, files) in os.walk(dir):
        for directory in dirs:
            if directory == ".git":
                repos.append(path)
		totalRepos=totalRepos+1;
    return repos

"""
run git status for a single git repo
param: repo
return: bool , list of issues
"""
def git_issues(repo):

    os.chdir(repo)
    status = subprocess.check_output(['git', 'status'])
    issues = has_issues(status)
    if issues[0]:
        #print [repo, issues] #debug output
        write_report([repo, issues])
        return issues
    else:
        return issues[1]

"""
This will run git status for all the git repos
and compile a list of repo dirs that have
any staged commits

param: list
return: list or boolean
"""
def write_reports(repos):
	report_stats = []
	for repo in repos:
            print ("%s: " % repo),
            issues = git_issues(repo)
            if (issues):
                if (len(issues[0])==1):
                    print (FAIL+"One issue:"+ENDC)
                else:
                    print (FAIL+"%d issues:" % len(issues[0])+ENDC)

                for issue in issues[0]:
                    print (WARNING+issue+ENDC)
            else:
                print (OKGREEN+"No issues."+ENDC)





"""
check the git status message to see if there are changes
that haven't been added or committed or pushed
"""
def has_issues(message):
	global dirRepos;
	dirRepos=dirRepos+1;
	#try:
	issues = []
	bool_issues = False
	changes_staged = "changes not staged for commit"
	changes_committed = "changes to be committed"
	changes_pushed = "your branch is ahead of"
	branch_behind = "your branch is behind"

	changes_not_committed = changes_committed in message.lower()
	committed_not_pushed = changes_pushed in message.lower()
	changes_not_added = changes_staged in message.lower()
	behind_commits = branch_behind in message.lower()
	if changes_not_added:
		bool_issues = True
		#file_name = get_file(message, 'Changes',message.count('Changes'))
		file_name = get_file_new('staged')
		issues.append("Changes not staged for commit: %s" % file_name)
	if committed_not_pushed:
		bool_issues = True
		unpushed = get_unpushed(message)
		issues.append("You have %s unpushed commits." % unpushed)
	if changes_not_committed:
		bool_issues = True
		#file_name = get_file(message, 'Changes',1 if (message.count('Changes') > 1 ) else 0)
		file_name = get_file_new('committed')
		issues.append("Changes to be committed: %s" % file_name)
	#if behind_commits:
	#	bool_issues = True
	#	issues.append("Your current branch is behind by %d commits", get_commits_behind(message))

	return [bool_issues, issues]
	#except:
	#	print '\nWe encounted an error on our end trying to read a clean repo\n'


	#return changes_not_committed or committed_not_pushed or changes_not_added #this will be removed
"""
Gets the file that is being staged in git
"""
def get_file(message, section, section_number):
	file_index = []
	splits = message.split(section)
	split = splits[section_number]
	count_mod = split.count('modified:')
	index = 0
	split = split.split()
	for i in range(0, count_mod):
		index = split.index('modified:', index+1)
		file_index.append(split[split.index('modified:',index) + 1])
	return file_index
	
def get_file_new(stage):
	files = []
	if stage == 'staged':
		output = subprocess.check_output(['git', 'diff', '--name-only'])
		output = output.split()
		for f in output:
			files.append(f)
	
	if stage == 'committed':
		output = subprocess.check_output(['git', 'diff', '--cached', '--name-only'])
		output = output.split()
		for f in output:
			files.append(f)	
	return files

"""
Gets the number of unpushed commits
"""
def get_unpushed(message):
    p = re.compile('\' by (\\d+)')
    r = p.search(message)
    num_unpushed = r.group(1)
    return num_unpushed
	
"""
Gets the number of commits that the branch is behind
"""
def get_commits_behind(message):
	split_message = message.lower().split()
	return (split_message.index('commits') -1)

"""
Write all the output to a nice little html file

param: list
"""
def write_report(report_info):

                # wow, we have to make a temporary directory because we cant get the 
                # package data directory

                os.chdir(temp_dir)


                matmin = open(temp_dir+"/material.min.css","w")

                matminlib = pkgutil.get_data('repo_rover', 'webReport/material.min.css')

                matmin.write(matminlib)

                matmin.close()

                styles = open(temp_dir+"/styles.css","w")

                styleslib = pkgutil.get_data('repo_rover', 'webReport/styles.css')

                styles.write(styleslib)

                styles.close()

		report_info[1].remove(True) #remove this because it is for conditional purposes and no longer needed
		#print '\n\n %s' % os.getcwd()
		create_card = """<section class=\"section--center mdl-grid mdl-grid--no-spacing mdl-shadow--3dp\">
				<div class=\"mdl-card mdl-cell mdl-cell--12-col\">
				<div class=\"mdl-card__supporting-text\">\n"""
		end_card = """
				</div>
				</div>
			</section>
		"""
		with open(temp_dir+'/index.html') as fin, open(temp_dir+'/output.html','w') as fout:
			#fout.writelines(create_card)
			#fout.write("The number of repositories: ", totalRepos)
			#fout.write("The number of clean repositories", cleanRepos)
			#fout.write("The number of issued repositories: ", dirRepos)
			#fout.writelines(end_card)
			for line in fin:
				fout.write(line)
				if '<div class="mdl-layout__tab-panel is-active" id="overview">' in line:
					next(fin)
					#print "inside"
					fout.write('\n\n')
					fout.writelines(create_card)
					fout.writelines('<h4> %s </h4>' % report_info[0])
					for info in report_info[1]:
						#fout.writelines(''.join(str(info)))
						#fout.writelines('<br />'.join(map(str,info)))
						fout.writelines('<br />'.join(info))
						fout.write('<br />')
						fout.write('\n')
					#fout.writelines(create_card)
					#fout.writelines(end_card)
					fout.writelines(end_card)



			
			fout.close()
			fin.close()
			os.rename(temp_dir+'/output.html',temp_dir+'/index.html')	



	# with open('src/webReport/index.html') as fin, open('src/webReport/output.html','w') as fout:
    # 	for line in fin:
    #     	fout.write(line)
    #     	if line == '<div class="mdl-layout__tab-panel is-active" id="overview">':
    #        		next_line = next(fin)
    #        		fout.writelines(create_card)
    #        		fout.writelines('<h2> %s </h2' % report_info[0])
	# 	report_file.close()

def main(argv):
	global totalRepos, dirRepos, cleanRepos
        
        if len(argv) > 0:
            initial_directory = argv[0]
			
	    if not os.path.isdir(initial_directory):
			print 'The directory provided is not valid please run again and provide a valid directory'				
			sys.exit(1)
				
        else:
            initial_directory = os.getcwd()

        repos = find_git_repos(initial_directory)

        if (totalRepos == 0):
            print "No repositories found."
            sys.exit()

        cleanRepos=(totalRepos-dirRepos)/totalRepos*100

        print ("I found %d git repositories, %0.2f%% clean." % (len(repos), cleanRepos))
	index = open(temp_dir+"/index.html","w")

		##create init_setup method
      	clean = pkgutil.get_data('repo_rover', 'webReport/clean.html')
	index.write(clean)
	index.close()
        write_reports(repos)

    	if os.path.exists(temp_dir + '/index.html'):
		index_url = ('file://' + temp_dir + '/index.html')
        	webbrowser.open(index_url, new=2)

	# print "The number of clean repositories that I found is: ", (totalRepos-dirRepos)
	# print "The number of issuses repositories that I found is : ", dirRepos
	# dirRepos=dirRepos/totalRepos*100
	# print ("The percentage of problematic repositories is: %0.2f%%." % dirRepos)

if  __name__ =='__main__':main(sys.argv[1:])

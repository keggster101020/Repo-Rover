import os
import subprocess
import re
import shutil


owd = os.getcwd()
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
            print "%s:" % repo,
	    issues = git_issues(repo)
            if (issues):
                if (len(issues[0])==1):
                    print "One issue:"
                else:
                    print "%d issues:" % len(issues[0])

                for issue in issues[0]:
                    print issue
            else:
                print "No issues."


            

		
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
	index = 0
	
	for i in range(0, count_mod):
		index = split.index('modified:', index+1)
		file_index.append(split[split.index('modified:',index) + 1])
	return file_index
	

"""
Write all the output to a nice little html file

param: list
"""
def write_report(report_info):
	report_info[1].remove(True) #remove this because it is for conditional purposes and no longer needed
	os.chdir(owd)
	#print '\n\n %s' % os.getcwd()
	create_card = """<section class=\"section--center mdl-grid mdl-grid--no-spacing mdl-shadow--2dp\">
            <div class=\"mdl-card mdl-cell mdl-cell--12-col\">
              <div class=\"mdl-card__supporting-text\">\n"""
	end_card = """
			 </div>
            </div>
          </section>
	"""
	with open('webReport/index.html') as fin, open('webReport/output.html','w') as fout:
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
					fout.writelines('<br />'.join(map(str,info)))
					fout.write('<br />')
					fout.write('\n')
				
				fout.writelines(end_card)
		fout.close()
		fin.close()
		os.rename('webReport/output.html','webReport/index.html')
			
			
	# with open('src/webReport/index.html') as fin, open('src/webReport/output.html','w') as fout:
    # 	for line in fin:
    #     	fout.write(line)
    #     	if line == '<div class="mdl-layout__tab-panel is-active" id="overview">':
    #        		next_line = next(fin)
    #        		fout.writelines(create_card)
    #        		fout.writelines('<h2> %s </h2' % report_info[0])
	# 	report_file.close()
				
def main():
	shutil.copyfile('webReport/clean.html', 'webReport/index.html')
	print "Enter the full directory you want to scan: "
	initial_directory = raw_input()
	repos = find_git_repos(initial_directory)
	print "I found %d git repositories." % len(repos)
	write_reports(repos)

	
if  __name__ =='__main__':main()

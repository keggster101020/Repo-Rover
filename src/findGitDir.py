import os

def find_git_repos(dir):
    repos = []
    for (path, dirs, files) in os.walk(dir):
        for directory in dirs:
            if directory == ".git":
                repos.append(path)
    return repos
				
def main():
	print "Enter the full directory you want to scan: "
	initial_directory = raw_input()
	print find_git_repos(initial_directory)
	
	
	
if  __name__ =='__main__':main()
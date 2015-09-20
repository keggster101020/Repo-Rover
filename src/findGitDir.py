import os

def find_git_repos(dir):
    repos = []
    for (path, dirs, files) in os.walk(dir):
        for directory in dirs:
            if directory == ".git":
                repos.append(path)
    return repos
				
def main():
	print "running"
	print find_git_repos("/home/s/shudyk/shudyk/cs280/")
	
	
	
if  __name__ =='__main__':main()
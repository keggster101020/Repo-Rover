import unittest
import reporover

class reporoverTestCase(unittest.TestCase):

  def testOne(self):
	expectedRepos=1;
	pwd="/home/z/zhengh/cs280/cs280-lab4team1/Repo-Rover"
	repos=[]
	repos=reporover.find_git_repos(pwd)
	actualRepos=len(repos)
	print "The expected number of repos is: ", expectedRepos
	print "The actual number of repos is: ", actualRepos
      	self.assertEqual(expectedRepos, actualRepos)

  def testTwo(self):
      	expectedRepos=2;
	pwd="/home/z/zhengh/cs280/cs280-lab4team1"
	repos=[]
	repos=reporover.find_git_repos(pwd)
	actualRepos=len(repos)
	print "The expected number of repos is: ", expectedRepos
	print "The actual number of repos is: ", actualRepos
	self.assertEqual(expectedRepos, actualRepos)

  def testThree(self):
   	expectedRepos=9;
	pwd="/home/z/zhengh/cs280"
	repos=[]
	repos=reporover.find_git_repos(pwd)
	actualRepos=len(repos)
	print "The expected number of repos is: ", expectedRepos
	print "The actual number of repos is: ", actualRepos
	self.assertEqual(expectedRepos, actualRepos)

  def testFour(self):
	expectedRepos=2
	pwd="/home/z/zhengh/cs220"
	repos=[]
	repos=reporover.find_git_repos(pwd)
	actualRepos=len(repos)
	print "The expected number of repos is: ", expectedRepos
	print "The actual number of repos is: ", actualRepos
	self.assertEqual(expectedRepos, actualRepos)

  def testFive(self):
	expectedRepos=90
	pwd="/home/z/zhengh"
	repos=[]
	repos=reporover.find_git_repos(pwd)
	actualRepos=len(repos)
	print "The expected number of repos is: ", expectedRepos
	print "The actual number of repos is: ", actualRepos
	self.assertEqual(expectedRepos, actualRepos)




if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(reporoverTestCase)
	unittest.TextTestRunner(verbosity=4).run(suite)


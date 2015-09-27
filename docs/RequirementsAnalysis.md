# Requirements Analysis

## Repo-Rover Summary
The customer requests a diagnostic tool to analyze all `Git` repositories located in a user's filesystem.  The purpose of this tool is to indicate warning signs that might need to be addressed by the user, such as untracked file modifications or files that have been committed, but never pushed to the remote repository.  The target audience for this tool will be other computer scientists who need such a tool to help manage and maintain their large number of repositories.  Both the input and output should be console-based and largely automated.  The program should accept a root directory from the user's filesystem, and then traverse the system to identify every `Git` repository contained therein.  It should then analyze and output all warning signs found within each individual repository, in addition to displaying a collection of summary statistics for all repositories examined.  The customer expects a functional programming systems product by Friday, 10/2/15.  Given the short time limit for this request, the customer suggests an incremental software development approach, preferring a few finished features over many partially completed ones.

---

## Background
Currently, there does not exist an efficient solution for analyzing large volumes of `Git` repositories in a user's local filesystem.  Comparable analysis is usually performed by using the `git status` or `git log` commands.  While these commands are helpful, they must be manually entered in each desired repository.  For computer scientists with hundreds or thousands of repositories, this becomes infeasible and likely will not be performed regularly.  As such, an automated process is needed for computer scientists to easily monitor their repositories and avoid potentially costly oversights.

---

## Process Constraints

1. __Incremental Development__

	The customer requests that we use an incremental build model while developing the system.  He has emphasized his preference for having a few fully functional features over having many partially functioning ones when the system is initially released.
	
2. __Documentation__

	Sufficient documentation should be included with the system's release, including: a thorough description of the system's requirements, an outline of the system's design that encompasses all of the system's intended features, a technical diagram of the design, and a comprehensive tutorial that clearly explains how the user can operate the system.
	
3. __Public Access__

	Once the system has been finished, it should be made publicly available in a `GitHub` version control repository.  

---
	
## Design Constraints

1. __Audience__

	The intended audience for this system is computer scientists.  As such, certain assumptions can be made regarding the knowledge of the user.  For instance, the user is assumed to be familiar with `Git` and understand related syntax, such as the meaning behind uncommitted files or untracked modifications in a `Git` repository.  The user is further assumed to be familiar with navigating a filesystem through a terminal window and to be comfortable executing programs from the command line.
	 
2. __Programming Language__
	
	No specific constraints have been given for the selection of programming language when implementing the system.  However, the choice of language should not pose a significant inconvenience or obstacle for users to operate the system on their own devices.  The documentation provided with the system should clearly outline how the user can obtain and install any necessary files needed to run the system using the selected language.
	
3. __Operating System__

	The customer ultimately wants this system to work across all operating systems, such that any computer scientist will be able to use it regardless of the device they choose.

4. __Input and Output Format__

	The customer requests the default implementation of the system to exclusively use the console for input and output, although the addition of a graphical user interface (GUI) would be permitted if resources allow (see *Non-Functional Requirements* for more details).
	
	*Input*: The user should specify a root address as a command line argument before program execution.  This address will determine the "starting point" for the system as it traverses all subdirectories therein.  Command line arguments/flags may also be used to control the use of certain features, at our discretion.
	
	*Output*: The output should include the diagnostic summaries for each repository individually, followed by the overall summary for the collection of repositories analyzed.  Specifically, the overall summary should be the first item the user views after the program finishes executing.
	
	>*TBD: Currently the __per__ repo summaries are only included in the external HTML report.  I will clarify with the customer if this is OK, or it such summaries should also be included in the console.*

---

## Functional Requirements

### Essential

1. __Filesystem Traversal__
	
    From a given root address, obtained via the user's input, the system should traverse the user's filesystem and identify all `Git` repositories present in all subdirectories.

2. __Diagnostic Summary (*Per* Repository)__
	
    Upon finding a repository, the system should identify all pertinent warning signs for that particular repository and output a summary of these findings.  If no warning signs are found, then the summary should indicate that the repository is *clean*.
			
    At a minimum, this summary should include:
      
       1. The names of files with untracked modifications.
       2. The names of files that have been added to the staging area, but not committed.
       3. The names of files that have been committed, but not pushed to the remote repository.
		
3. __Diagnostic Summary (*All* Repositories)__
  
    After analyzing all repositories individually, the system should output some statistics about the collection of repositories.  By default, this summary should be immediately viewable after program execution.
    
    At a minimum, this summary should include:
      
       1. The total number of repositories found in the filesystem (given a root address).
       2. The total number and percentage of *clean* repositories, i.e. repositories that have no indicated problems. 

### Desirable

1. __Additional *Per* Repository Statistics__
    
    In addition to displaying the names of files with warning signs, the summaries produced *per* repository should include:
       
       1. The number and/or percentage of files with untracked modifications.
       2. The number and/or percentage of files that have been added to the staging area, but not committed.
       3. The number and/or percentage of files that have been committed, but not pushed to the remote repository.

2. __Additional *Overall* Repository Statistics__

    In addition to displaying the number of repositories found and the number of clean repositories, the *overall* repository summary should include:
    
       1. The total number of files with untracked modifications.
       2. The total number of files that have been added to the staging area, but not committed.
       3. The total number of files that have been committed, but not pushed to the remote repository.

### Optional

1. __Garbage File Recognition__
    
    While analyzing each repository, the system should detect specific files that the user designates as "garbage."  These file types could be included in command line arguments during program execution, or by any other means at our discretion.  For example, if the user indicates `.class` or `.pdf` files, then all files of these types should be specifically designated in each individual repository summary, regardless of its *clean* status.

---

## Non-Functional Requirements

### Essential

1. __Scalability__

    The system should be able to traverse tens of thousands of directories in a user's filesystem, in addition to analyzing hundreds or thousands of `Git` repositories.
    
2. __Speed__

	The system should be able to locate all `Git` repositories and output the desired summaries within a "*reasonable amount of time*."
    
    >*TBD: Need to clarify with customer if this __"reasonable amount of time"__ can be translated into a quantifiable amount*
    
3. __Ease of Use__

    The user should be able to operate the system with minimum difficulty.  The input syntax should be easy to understand, and the output should be formatted clearly.
    
4. __Reliability__

	>*TBD: The customer did not specifically indicate this during requirements elicitation, but I will clarify if he has certain expectations for handling faults in the system_*

### Desirable

1. __Color Coordination__

	The output produced by the system should exhibit some form of color coordination to enhance the user's interpretation of the results.  For example, each of the *per* repository statistics might be highlighted in a different color, or the *overall* repository statistics might change color depending on the number/percentage of files identified.  However, the specifics of this color coordination are left to our discretion.

### Optional

1. __Graphical Report__

	After the system has finished execution, an external graphical report should be produced.  The format of this report is left to our discretion, but it should include all of the pertinent repository diagnostics described previously.
	
	>*TBD: The current HTML reports that our system produces appear to overwrite each other during each run.  I will clarify if this is acceptable to the customer, or if he wants each report to be saved separately*
	
2. __Graphical User Interface (GUI)__

	The default implementation requested by the customer involves exclusive use of the console for input and output.  However, if time and resources permit, then a GUI could be added to improve the system's ease of use and the clarity of results.  No formating or other stylistic constraints have been determined by the customer for such an interface, if we decide to implement it. 
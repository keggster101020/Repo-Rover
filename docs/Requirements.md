Requirements
============

High Level
----------

A tool for developers who use a lot of git repositories.
The tool should search through the file system for git repos
and report on their status.  The tool should provide a high
level summary, as well as draw the users attention to potential
issues with their git repos.

Features
--------

# Summary

Let the user know how many git repos were found and their
location on the file system.

# Issue Detection

Notify the user if git repositories have any of 
the following issues:
+ Issue: Files changed but not staged
+ Issue: Files staged but not commited
+ Issue: Changes commited but not pushed

Non-functional
--------------

# Scalability

Handle thousands of directories and hundreds of repositories.

# UI

Color-coordinated output.
Scan in the current working directory.

# Platform

No specific preference, but the more the better.

Stretch Goals
-------------

+ GUI
+ Detect garbage files
+ Branch level reporting
+ HTML report
+ Complete cross-compatibility

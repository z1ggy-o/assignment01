# A Short Introduction to Git

## What is git?

Git may be the most popular distributed version control system in the world.
It is created by Linus Torvalds for development of the Linux kernel. Git is
primarilly used for source code management in software development, but it can
be used to for any set of files.

Next, let's briefly talk about the Version Control System and the features of git briefly.

### Version Control System

How do you manage your files? Do you do things like this when you try to modify
your files?
[files capture]

With version control, you do not need to make duplicate files to avoid screw your
files up anymore. Version control system is a system that records changes to
files over time so that you can go back to the previous states. Also it provides more features, such as comparing the differences between two versions and collaborating with others.

### Git

In general there are two types of version control systems, *Centralized Version
Control Systems* and *Distributed Version Control Systems*. Centralized system has
a client-server structure. All files are stored in a central server and users just
can access specific files which adminitrators allow them to.

Like we said before, git is a *distributed version control system*. Instead of
certain files, it fully mirror the repository from the server, including history.
This approach gives disctributed system some advantages that centralized system
does not have. Such as users can work offline; if one server dies, any client
can restore it easily. Furthermore, we can have several remote repositores working
simultaneously within the same project.

## How git works?
the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they’re working on. If the hard disk the central database is on becomes corrupted, and proper backups haven’t been kept, you lose absolutely everything

they fully mirror the repository, including its full history. Thus, if any server dies, and these systems were collaborating via that server, any of the client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data.

### repository structure
### branch

## How I use git

###  
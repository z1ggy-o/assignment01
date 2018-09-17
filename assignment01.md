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

## How to Use Git

At this part, let's talk about how to use git. I will just list some basic operations to let you get into git's world. If you want to know more, Pro Git[link] is a good book to read. You can get it free online.

### The Basic Construct of Git

The files in git has three main states: committed, modified and staged:
- Modifed means that you have changed something but have not put them into your database yet.
- Staged means that you tell git which modifed files you want to commit.
- Committed files are files that stroed in our local database

[picture git states]

At the root directory of each git repositoy, you can find a hidden directory called .git.
This directory stores all the datas for your project. When you clone a repository from another computer, this is what you get. Delete .git, you will lose everything.

Another thing I want to talk about is *Branch*. One of the features of git is that it supports non-linear developments well. Branching means you diverge from the main line of development and to do some other works without messing with main line. Git's branching operation's overhead is small. It does not copy the files but use pointers to link your project snapshots together. This approach makes creating braches fast and lightweight. That's why git encourages people to do branch and merge often.
We will talk how to use branch later.

### First Time with Git

#### Set User Name and Email Address

After the installation, the first thing to do is to set your name and email address. This is important because Git uses this information to identify users.

Use command `git config`
```
git config --global user.name "Your Name"
git config --global user.email "Your Email address"
```

Git's configuration files be stored in three different places and have different scope. Use options below to `git config` to choose the scope you want. Each level overrides the previous level.
```
--system # apply to every user on the system
--global # apply to you, the user's repository
--local # apply to that single repository (default option)
```

There are many other variables we can modify. Check them once you got time.

#### First Repository

Let's do our first commit together. Go to your project's directory, type 
```
git init
```
This command will generate the `.git` subdirectory under the current directory.

At this point, nothing in the project is tracked yet. You have to tell git which files it should working on.

We can check the status of files through command `git status`:
```
$ git status

On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

To track new files, use command `git add <file>`. This command will put files into the *staging area*, both new files or modified files. Only files in the staging area will be commited into the database. Now, let's add some files.

```
$ git add README.md assignment01.tex
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   README.md
	new file:   assignment01.tex
```

We can find the two files are staged and will to into our next commit.

Now let's finish our first commit, just type `git commit`. Git will ask you to input the commit message:

```
# Please enter the commit message for your changes. Lines starting
  3 # with '#' will be ignored, and an empty message aborts the commit.
  4 #
  5 # On branch master
  6 #
  7 # Initial commit
  8 #
  9 # Changes to be committed:
 10 #   new file:   README.md
 11 #   new file:   assignment01.tex
 12 #
 ```

Writing meaningful commit message is very important, because the message is the best way to learn about a change. Google "How to write a good git commit", you can find lots of articles talking about it. There is no standard way to write commit message, but well formed message helps a lot.

Use `git log` we can check the existing commit history:
```
commit 7af35596163c980d0661faeef9a3eef1e67732be (HEAD -> master)
Author: Guangyu Zhu <guangyuzhu1129@gmail.com>
Date:   Mon Sep 17 22:04:38 2018 +0900

    Third commit

commit 38697bada55cf777d069613760f90a24dd09b792
Author: Guangyu Zhu <guangyuzhu1129@gmail.com>
Date:   Mon Sep 17 22:03:49 2018 +0900

    Second commit

commit b2e78948dde81c0ca5858e4f78d52a4b0676c368
Author: Guangyu Zhu <guangyuzhu1129@gmail.com>
Date:   Mon Sep 17 21:35:30 2018 +0900

    Initial the project.
```

There are hash values for each commit. Git use the hash values to identify commits. By the way, this is a bad example of commit message. You can get nothing meaningful from above commit messages.

With these hash values we can go back to previous commit through command `git checkout <hash>`:
```
$ git checkout b2e78948
Note: checking out 'b2e78948'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at b2e7894... Initial the project.
```

To go back to the newest commit, type `git checkout master`.

#### Delete and Ignore Files

Sometimes you tracked the wrong files or you want to remove some tracked files. Delete them from the directory may not working well, because you need to tell git to stop tracking them. Use `git rm <file>` will remove the file from git and working directory.

To avoid tracking some files that we do not need, `.gitignore` comes out. List patterns to match file names in `.gitignore`. Git will ignore all the files that are listed in `.gitignore` file.
Git use *glob patterns` that shells use. If you do not know which files need to be ignored. Do not worry,https://www.gitignore.io/ can generate these rules for you. The only thing you need to do is input the working environment.

### Branch

## Collaborate Through Github

### Github work flow
https://guides.github.com/introduction/flow/
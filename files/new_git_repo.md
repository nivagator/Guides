# GitHub Things

### New Git Repo  
[Guide](http://kbroman.org/github_tutorial/pages/init.html)  

1. Clone existing repo  
2. Create new local from scratch, push to GitHub  
3. New repo from existing project  
[Github Help](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)  

Create new repo on Github but do not initialize with README  
Open Git Bash in the project directory  
`git init`  
`git add .`  
`git commit -m "first commit"`  
`git remote add origin [remote repository URL]`  
`git remove -v`  
`git push origin master`  


### Basic Workflow
Git Bash order of events:
1. `git clone <github url>`

As needed, `git status` will describe the changes made since the last commit.
Repeat steps 2 through 4 for each commit to GitHub

2. `git add .` or `git add <filename>`
3. `git commit -m "commit message"` use -m to add a comment to each commit
4. `git push <remote name> <name of branch to push>` i.e., `git push origin master`

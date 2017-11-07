# Deploy from GitHub

1. [Manual Steps](#manual)  
2. [Automated using git hooks](#automated)  


### <a name="manual"></a>1. Manual steps

Clone the repo to a temp destination    
`mkdir gittemp && cd gittemp`  
`git clone [repo http url]`    

Build an exclude-list for git files and any other exclusions you don't want in production  
`cd /path/to/html/`  
`touch exclusion-list.txt`  
`nano exclusion-list.txt`     
```
.git
.git/
.gitignore
*.gitignore
README.md
```

Use rsync to merge the html destination  
`rsync -avz --exclude-from '/path/to/html/exclude-list.txt' /path/to/gittemp/[repo name]/ /path/to/html`

rsync will recursively merge-copy files to the html folder while excluding the non-production files and directories in the exclude-list.txt file.



### <a name="automated"></a>2. Automated using git hooks

[Deploy your site with git](https://gist.github.com/oodavid/1809044)  

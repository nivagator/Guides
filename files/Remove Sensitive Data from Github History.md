[Stack Overflow](https://stackoverflow.com/a/872700)

`git filter-branch --index-filter 'git update-index --remove filename' <introduction-revision-sha1>..HEAD`
`git push --force --verbose --dry-run`
`git push --force`

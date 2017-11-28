# rsync

[6 rsync Examples to Exclude](http://www.thegeekstuff.com/2011/01/rsync-exclude-files-and-folders/?utm_source=feedburner)  
[10 Practical Examples of Rsync](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)  
[Linode Backup Guide](https://www.linode.com/docs/security/backups/backing-up-your-data#rsync-1)  
[rsync Incremental](http://webgnuru.com/linux/rsync_incremental.php)  


### Excerpts from Linode Backup Guide
Basic rsync command
```
rsync user@production_server:~/public ~/backups/mybackup

|---| |-----------------------------| |----------------|
  ^                 ^                          ^
  |                 |                          |
rsync           copyfrom                    copyto
```

Option usage
```
rsync --options copyfrom copyto
```

copyfrom using ssh:
```
user@production_server:~/public
|--------------------| |------|
          ^                ^
          |                |
     SSH login           path
```

creating dated backup folders
```
~/backups/public_$(date -I)
                 |--------| <- date variable
|-------------------------|
             ^
             |
           path
```

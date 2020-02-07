#### Install scripts to the crontab
Moving files to the crontab (or cron.[timeframe])  
`cp -v website_bak.sh /etc/cron.daily/`


#### Testing the crontab
I think files with extensions are ignored.  

run:  
`run-parts --test /etc/cron.daily`  
If you don't see your scripts listed, remove the .sh extensions and try again.

#### Links
[nixCraft - Cron](https://www.cyberciti.biz/faq/howto-check-cronjob-is-running-not/)

### Location of crotab files
 - The location of cron files for individual users is `/var/spool/cron/crontabs/`

### different crontabs
- `crontab -e` vs `sudo crontab -e`

### mount nas on boot
`sudo crontab -e`
```
@reboot mount 192.168.1.216:/volume1/backups /mnt/backups
@reboot mount 192.168.1.216:/volume1/sinefiles /mnt/sineserver
@reboot mount 192.168.1.216:/volume1/files /mnt/files
```

### run remote server backup scripts
`crontab -e`
```
0 6 * * * /home/gavin/bkupscripts/dev01_backup.sh
10 6 * * *  /home/gavin/bkupscripts/linode02_backup.sh
```

#### Install scripts to the crontab
Moving files to the crontab (or cron.[timeframe])  
`cp -v website_bak.sh /etc/cron.daily/`


#### Testing the crontab
I think files with extensions are ignored.  

run:  
`run-parts --test /etc/cron.daily`  
If you don't see your scripts listed, remove the .sh extensions and try again.

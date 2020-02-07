## Update MOTD on demand
- http://manpages.ubuntu.com/manpages/xenial/man5/update-motd.5.html
- `sudo apt install update-motd`

Used to dynamically refresh the motd seen at server startup on demand.

From the linked manpage:
> MOTD  fragments  must  be scripts in /etc/update-motd.d, must be executable, and must emit information on standard out.
Scripts should be named named NN-xxxxxx where NN is a two digit number indicating their position in the MOTD, and xxxxxx is an appropriate name for the script.

use:
`sudo update-motd`
example output:
```bash
gavin@docker:~$ sudo update-motd
Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-32-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Aug 23 02:40:34 UTC 2018

  System load:  0.01               Processes:              276
  Usage of /:   26.3% of 48.96GB   Users logged in:        1
  Memory usage: 77%                IP address for ens160:  192.168.1.166
  Swap usage:   0%                 IP address for docker0: 172.17.0.1

 * Read about Ubuntu updates for L1 Terminal Fault Vulnerabilities
   (L1TF).

   - https://ubu.one/L1TF

 * Check out 6 great IDEs now available on Ubuntu. There may even be
   something worthwhile there for those crazy EMACS fans ;)

   - https://bit.ly/6-cool-IDEs

 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

2 packages can be updated.
1 update is a security update.
```

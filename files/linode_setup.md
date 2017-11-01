# Linode Setup

# Adapted from [Feross][5]


### Overview
1. OS Setup
2. Updates
3. Install essential software
4. Lockdown -> Security
5. System stability and features
6. Backups and automation
7. Install custom software
---
### Assumptions
- OS: Ubuntu 16.04 LTS
---
### 1. OS Setup
- [Set hostname](#sethostname)
- FQDN
- Set the time
- Set non-root user
- SSH Keys [Digital Ocean][4]
- disable root login
- change SSH port

### 2. Updates
- apt-get update
- apt-get upgrade

### 3. Install essential software
- virtualenv
- virtualenvwrapper(?)
- ufw [ufw][]

### 4. Lockdown -> Security
- disable repeated logins with Fail2Ban
- setup firewall [ufw][]
- enable email notification for each user use of sudo

### 5. System stability and features
- Limit Apache(2.2) max clients
- Reboot on out-of-memory condition
- Reverse DNS
- Private IP

### 6. Backups and automation
- rsync [Digital Ocean][1] | [Linode][2]
- Synology NAS
- Linode Backups [Linode][3]
### 7. Install custom software
- Compiler
- MySQL
- Python
- Nginx
- Apache
- PHP
- Node.js
- MongoDB
- PostgreSQL
- Django

---

#### <a name="sethostname"></a> Set hostname
As the root user, use `hostname` to check the current hostname value.

The hostname is stored in `/etc/hostname`. Either edit this file using `nano` or
execute `echo "hostname" > /etc/hostname`. In order to force the new hostname to the system, execute
`hostname -F /etc/hostname`.


[ufw]: ufw.md
[1]: https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps
[2]: https://www.linode.com/docs/security/backups/backing-up-your-data
[3]: https://www.linode.com/docs/security/backups/backing-up-your-data#making-a-manual-backup
[4]: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
[5]: https://feross.org/how-to-setup-your-linode/

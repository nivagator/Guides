# Linode Setup

Adapted from [Feross](https://feross.org/how-to-setup-your-linode/)
----------------------------
### Overview
1. OS Setup
2. Updates
3. Install essential software
4. Lockdown -> Security
5. System stability and features
6. Backups and automation
7. Install custom software
--------------------------------
### Assumptions
- OS: Ubuntu 16.04 LTS
--------------------------------
### 1. OS Setup
-Set hostname
-FQDN
-Set the time
-Set non-root user
-SSH Keys
-disable root login
-change SSH port

### 2. Updates
-apt-get update
-apt-get upgrade

### 3. Install essential software
-virtualenv
-virtualenvwrapper(?)
-ufw

### 4. Lockdown -> Security
-disable repeated logins with Fail2Ban
-setup firewall (ufw)
-enable email notification for each user use of sudo

### 5. System stability and features
-Limit Apache(2.2) max clients
-reboot on out-of-memory condition
-Reverse DNS
-Private IP

### 6. Backups and automation
-rsync
--Synology NAS
-Linode Backups

### 7. Install custom software
-Compiler
-MySQL
-Python
-Nginx
-Apache
-PHP
-Node.js
-MongoDB
-PostgreSQL
-Django

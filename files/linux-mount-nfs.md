## Mounting NFS Share to Linux server

[Mount Synology NAS via NFS][1]  

Client - Linux machine requiring access to files on the NAS  
Host - Machine that shares its files (in my case, a Synology NAS)  

There are specific steps you must follow within the Synology control panel. See [this link][1] for step by step instructions to setup the Synology NAS to serve its folders to a client via NFS.  

#### Set up Host
this is simple in my case, mainly because its done through a GUI interface using a step by step detailed guide. [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-16-04) has a guide for serving files from one Linux server to another.

#### Set up Client
This command will mount the NFS drive to the specified mount point.
`sudo mount [host ip]:/path/to/share /local/mount/point`  

Running the disk free command,`df`, will show all file systems. If the mount was successful, it will be listed here.  

To unmount the NFS run the following:  
`sudo umount -f -l /local/mount/point`



[1]: https://www.synology.com/en-us/knowledgebase/DSM/tutorial/File_Sharing/How_to_access_files_on_Synology_NAS_within_the_local_network_NFS

# Guide to install SSL certs

## System

- nginx
- ubuntu 18.04
- letsencrypt

Best, most comprehensive walkthrough for nginx/ubuntu/letsencrypt and explains optional config for A grade on ssllabs.com

**<https://www.linuxbabe.com/ubuntu/nginx-lets-encrypt-ubuntu-16-04-17-10#>**

## SSLLabs.com A+ Grade changes

As of January 31st, 2020, [ssllabs.com has depricated tls v1.1 and 1.2](https://blog.qualys.com/ssllabs/2018/11/19/grade-change-for-tls-1-0-and-tls-1-1-protocols) and caps grades to B where they exists
Per linuxbabe comments:

- To disable TLSv1 and TLSv1.1, edit the Let’s Encrypt SSL options configuration file.
  - `sudo vi /etc/letsencrypt/options-ssl-nginx.conf`
- Find the following line.
  - `ssl_protocols TLSv1 TLSv1.1 TLSv1.2;`
- Remove the phased-out TLS version. Replace with this text
  - `ssl_protocols TLSv1.2`
- Save and close the file and test nginx configuration
  - `sudo nginx -t`
- Then restart Nginx.
  - `sudo systemctl restart nginx`

## HSTS - HTTP Strict Transport Security

<https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>

Sites can opt into the Chrome preload list as HTTPS only.

## DNS Certification Authority Authorization - CAA Records

<https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization>

You can define a specific certification authority for domains.

## Other Links

### Redirect www to non-www and/or Force HTTPS

- <https://easyengine.io/tutorials/nginx/www-non-www-redirection/>  
- <https://www.hostinger.com/tutorials/nginx-redirect/>  

# 0x10. HTTPS SSL

# 0. World wide web


    Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

<ul>

     dig www.holberton.online | grep -A1 'ANSWER SECTION:'
     ./0-world_wide_web holberton.online    

</ul>

# 1. HAproxy SSL termination

    “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

    Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

<ul>

     curl -sI https://www.holberton.online
     curl https://www.holberton.online
</ul>

# 2. No loophole in your website traffic

    A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.


<ul>
    curl -sIL http://www.holberton.online
    
</ul>
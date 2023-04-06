# 0x10. HTTPS SSL

# 0. World wide web


    Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

<ul>

     dig www.holberton.online | grep -A1 'ANSWER SECTION:'
     ./0-world_wide_web holberton.online    

</ul>
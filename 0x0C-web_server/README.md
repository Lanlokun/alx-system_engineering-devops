# 0x0C. Web server

# 0. Transfer a file to your server


<ul>

    ./0-transfer_file
    ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
</ul>

# 1. Install nginx web server


<ul>
    ./1-install_nginx_web_server > /dev/null 2>&1
    curl localhost
</ul>


# 2. Setup a domain name


<ul>
    dig kwye.tech

</ul>

# 3. Redirection

    Configure your Nginx server so that /redirect_me is redirecting to another page.



<ul>
    curl -sI 34.198.248.145/redirect_me/

</ul>


# 4. Not found page 404


    Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

<ul>

    curl -sI 34.198.248.145/xyz

</ul>

# 5. Install Nginx web server (w/ Puppet)


    Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.


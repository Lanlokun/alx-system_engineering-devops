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


<ul>
    curl -sI 34.198.248.145/redirect_me/

</ul>

# 0x08. Networking basics #1

# 0. Change your home IP


Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

localhost resolves to 127.0.0.2
facebook.com resolves to 8.8.8.8.

<ul>
     ping localhost
</ul>


# 1. Show attached IPs


Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

<ul>
    ./1-show_attached_IPs | cat -e
</ul>

# 2. Port listening on localhost

Write a Bash script that listens on port 98 on localhost.


<ul>

    sudo ./100-port_listening_on_localhost

    (open_new_terminal)

    telnet localhost 98

    (on_previous_terminal)

    sudo ./100-port_listening_on_localhost

</ul>



# 0x0B. SSH


# 0. Use a private key

<ul>
    ./0-use_a_private_key
</ul>

# 1. Create an SSH key pair


<ul>
    ./1-create_ssh_key_pair
</ul>

# 2. Client configuration file


<ul>
    ssh -v ubuntu@0.0.0.0

<span>replace ip with yours</span>
</ul>

# 4. Client configuration file (w/ Puppet)


<ul>
    sudo puppet apply 100-puppet_ssh_config.pp

</ul>
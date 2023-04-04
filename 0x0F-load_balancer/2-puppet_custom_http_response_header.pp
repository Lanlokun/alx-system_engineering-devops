# creating a custom HTTP header response, but with Puppet

exec { 'command':
  command => 'apt-get -y update',
  apt-get -y install nginx
  sudo sed -i "/listen 80;/a-add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
  sudo service nginx restart
  provider => 'shell',
}
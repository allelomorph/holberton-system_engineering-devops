# installs nginx with a 301 and 404 page

# general update before install
exec { 'general update':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'apt-get -y update',
  user    => 'root',
}

# install nginx
exec { 'install nginx':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'apt-get -y install nginx',
  user    => 'root',
  require => exec['general update'],
}

# create new default index page and 404 page
exec { 'new index and 404 pages':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'echo "Holberton School" > /var/www/html/index.html; echo "Ceci n\'est pas une page" > /var/www/html/404.html',
  user    => 'root',
  require => exec['install nginx'],
}

# update nginx sites-available with 301
exec { 'update sites-available with 301':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'sed -i "/listen \[::]:80 default_server;/a\	rewrite ^/redirect_me/?.*$ https://www.youtube.com/watch?v=mTEros927Ow permanent;" /etc/nginx/sites-available/default',
  user    => 'root',
  require => exec['new index and 404 pages'],
}

# update nginx sites-available with 404
exec { 'update sites-available with 404':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'sed -i "/listen \[::]:80 default_server;/a\	error_page 404 /404.html;" /etc/nginx/sites-available/default',
  user    => 'root',
  require => exec['update sites-available with 301'],
}

# start nginx
exec { 'start nginx':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'service nginx start',
  user    => 'root',
  require => exec['update sites-available with 404'],
}

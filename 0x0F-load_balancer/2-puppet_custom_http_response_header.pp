# 0x0F. Load balancer - 2. Add a custom HTTP header with Puppet
# HTTP response header for nginx web server

exec { 'general update':
    command => '/usr/bin/env apt-get -y update',
}

package { 'nginx':
    ensure  => installed,
    require => Exec['general update']
}

file { 'minimum HTML content' :
    ensure  => file,
    path    => '/var/www/html/index.html',
    content => 'Holberton School',
}

file_line { 'HTTP response header' :
    ensure  => present,
    path    => '/etc/nginx/nginx.conf',
    line    => "
        add_header X-Served-By ${hostname};",
    after   => 'http {',
    require => Package['nginx']
}

service { 'nginx' :
    ensure  => running,
    require => File_line['HTTP response header']
}
# 0. Sky is the limit...: raise simultaneous open file descriptor cap on nginx

file { '/etc/default/nginx' :
  ensure  => file,
}
-> exec { 'comment out arbitrary FD limit':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i "s/^ULIMIT=/# ULIMIT=/" /etc/default/nginx',
}
~> service { 'nginx' :
  ensure  => running;
}

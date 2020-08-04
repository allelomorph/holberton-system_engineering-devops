# task 0. Create a file

file { 'holberton':
  path    => '/tmp/holberton',
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

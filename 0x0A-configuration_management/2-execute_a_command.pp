# task 2. Execute a command

exec { 'killmenow':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'pkill killmenow',
  user    => 'root',
  onlyif  => 'pgrep killmenow',
}

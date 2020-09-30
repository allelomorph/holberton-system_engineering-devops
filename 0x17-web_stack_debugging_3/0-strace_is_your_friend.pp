# task 0. Strace is your friend: repair LAMP stack server running wordpress

file { '/var/www/html/wp-settings.php' :
  ensure  => file,
}
-> exec { 'replace reference to /class-wp-locale.phpp':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'sed -i "s|/class-wp-locale.phpp|/class-wp-locale.php|" /var/www/html/wp-settings.php',
}

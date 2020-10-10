# remove `holberton` user open file limits

exec { 'hard file limit':
  command => "sed -i 's/^holberton hard nofile /#holberton\thard\tnofile\t/' /etc/security/limits.conf",
  path    => '/bin:/usr/bin:/usr/local/bin'
}

exec { 'soft file limit':
  command => "sed -i 's/^holberton soft nofile /#holberton\tsoft\tnofile\t/' /etc/security/limits.conf",
  path    => '/bin:/usr/bin:/usr/local/bin'
}

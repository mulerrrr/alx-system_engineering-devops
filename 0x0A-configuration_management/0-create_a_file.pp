# This manifest creates holberton file in the /tmp directory
file { '/tmp/holberton':
    ensure  => file,
    content => 'I love Puppet',
    group   => 'www-data',
    owner   => 'www-data',
    mode    => '0744',
}

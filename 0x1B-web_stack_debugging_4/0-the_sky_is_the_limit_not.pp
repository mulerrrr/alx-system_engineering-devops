# fix the limit nginx.
exec { 'myfix':
command => 'sed -i s/15/2000/ /etc/default/nginx',
path    => '/bin',
}
service { 'nginx':
ensure    => running,
subscribe => Exec['myfix'],
}

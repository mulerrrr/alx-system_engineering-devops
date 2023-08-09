# ensure class-wp-locale.phpp exists with the content of class-wp-locale.php
# solution for 500 status error code
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
ensure => present,
source => '/var/www/html/wp-includes/class-wp-locale.php',
}

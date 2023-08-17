# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec { 'change-os-configuration-for-holberton-user':
command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 4096/g' /etc/security/limits.conf;
sed -i 's/holberton soft nofile 4/holberton soft nofile 1024/g' /etc/security/limits.conf",
provider => shell,
}

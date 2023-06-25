# Append a line for passwd auth or identity file if it doesn't exist in the path file

file_line {'Turn off passwd auth':
    path  => '/etc/ssh/ssh_config',
    line  => 'PasswordAuthentication no',
}

file_line {'Declare identity file':
    path  => '/etc/ssh/ssh_config',
    line  => 'IdentityFile ~/.ssh/holberton',
}

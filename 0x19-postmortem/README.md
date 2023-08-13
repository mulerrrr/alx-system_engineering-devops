Postmortem
 An outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server led to `500 Internal Server Error`'s, when the expected response was an HTML file site.
Debugging Process
Debugger man started debugging:-
1. Checked running processes using `ps aux`. Two `apache2` processes - `root` and `www-data` - were properly running.
2. Looked in the `sites-available` folder of the `/etc/apache2/` directory. Determined that the web server was serving content located in `/var/www/html/`.
3. In one terminal, ran `strace` on the PID of the `root` Apache process. In another, curled the server. Expected great things... only to be disappointed. `strace` gave no useful information.
4. Repeated step 3, except on the PID of the `www-data` process. Kept expectations lower this time... but was rewarded! `strace` revelead an `-1 ENOENT (No such file or directory)` error occurring upon an attempt to access the file `/var/www/html/wp-includes/class-wp-locale.phpp`.
5. Looked through files in the `/var/www/html/` directory one-by-one, using Vim pattern matching to try and locate the erroneous `.phpp` file extension. Located it in the `wp-settings.php` file. (Line 137, `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).
6. Removed the trailing `p` from the line.
7. Tested another `curl` on the server. 200 A-ok!
8. Wrote a Puppet manifest to automate fixing of the error.
Summation
Simply said, a typo. Have to adore 'em. In its entirety, the WordPress software was trying to load the file "class-wp-locale.phpp" when it encountered a fatal error in "wp-settings.php." 'class-wp-locale.php' was the right file name, and it was located in the application's folder within the 'wp-content' directory.
Patch only required eliminating the trailing "p" to correct the error.
Prevention
This outage was caused by an application fault, not a web server error. Please keep the following in mind going ahead to avoid any more outages of this nature.
 
* Test! Try, try, try. Before deploying, test the application. If the program had been tested, this problem would have occurred and could have been fixed sooner.
 
* Monitoring of status. Allow an uptime monitoring service, such as [UptimeRobot](./https://uptimerobot.com/), to send out an immediate notice in the event that the website goes down.
 
As a result of this error, I created the Puppet manifest [0-strace_is_your_friend.pp] (https://github.com/bdbaraban/holberton- system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp) to automate the correction of any future occurrences of the same errors. Any instances of the 'phpp' extension in the file '/var/www/html/wp-settings.php' are changed to 'php' by the manifest. 


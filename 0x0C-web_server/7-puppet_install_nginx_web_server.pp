# install nginx, 301, 404
exec {'/usr/bin/env apt-get -y update': }
exec {'/usr/bin/env apt-get -y install nginx': }
exec {'/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html': }
exec {'/usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html': }
exec {'/usr/bin/env sed -i "/listen [::]:80 default_server;/ a\\\trewrite ^/redirect_me http://www.holbertonschool.com permanent;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env sed -i "/listen [::]:80 default_server;/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env service nginx restart': }

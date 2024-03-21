
#!/bin/bash

# Installation du serveur SSH
apt-get update
apt-get install -y openssh-server

# Configurer le serveur SSH (ajoutez d'autres configurations si nécessaire)
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# Démarrer le serveur SSH
service ssh start

# Installer WP-CLI
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
chmod +x wp-cli.phar
mv wp-cli.phar /usr/local/bin/wp

# Installer WordPress
wp core install --url=http://192.168.99.11 --title=wordpress --admin_user=Aurelie --admin_password=1234 --admin_email=nkblondelle@gmail.com --allow-root

# Exécuter la commande CMD ou ENTRYPOINT d'origine
exec "$@"

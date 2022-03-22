echo "You must run with root!"
sudo apt install gnome-terminal
sudo apt install python3
git clone https://github.com/GeerxOS/msf-shell
cd msf-shell
mkdir /usr/share/msf-shell
mv * /usr/share/msf-shell
mv .gitignore /usr/share/msf-shell
mv .git /usr/share/msf-shell
cd /usr/bin
echo '#!/bin/bash' >> msf-shell
echo ' ' >> msf-shell
echo 'exec python3 /usr/share/msf-shell/msf-shell.py' >> msf-shell
echo 'Installed!'
echo "Open terminal"
echo "Use msf-shell"
chmod 777 msf-shell


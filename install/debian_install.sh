#!/usr/bin/env bash

use_superuser=""
if [ $UID -ne 0 ]; then
    echo "Superuser privileges are required to run this script."
    use_superuser="sudo"
fi

echo "Updating software source..."

${use_superuser} apt-get update

echo "Installing Dependency..."

${use_superuser} apt-get install -y nginx uwsgi uwsgi-plugin-python3 python3-pip python3-wheel git


if [ ! -f "install.sh" ]; then
    git clone https://github.com/SilverBlogTeam/SilverBlog.git --depth=1 silverblog
    cd silverblog/install
fi

${use_superuser} pip3 install -r python_dependency.txt

if [ ! -f "../pm2.json" ]; then
    cp -i ../example/pm2.example.json ../pm2.json
fi

read -p "Is qrcode support component installed? (Y/N): " yn

if [ "$yn" == "Y" ] || [ "$yn" == "y" ]; then
    ${use_superuser} pip3 install qrcode-terminal
fi

./install.sh

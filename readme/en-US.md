# SilverBlog

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/SilverBlogTeam/SilverBlog/blob/master/LICENSE)

SilverBlog is a lightweight blog project based on Python3.

## Why SilverBlog

* Simple, compact blog system.
* Easy to install and deploy.
* Complete Rss support.
* Modular design, easy to add, delete.
* No database design.
* With a static page generation module comparable to Hexo, you can run on Github Page with only one line of commands.
* Native support for Linux can be deployed on any platform through Docker.
* Have an Android client.
* Have a web client.
* Developing an IOS client

## how to install

You can install SilverBlog directly using the installation script:

Docker:

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/SilverBlogTeam/SilverBlog/master/install/docker_install.sh)"
```

On Container:

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/SilverBlogTeam/SilverBlog/master/install/container_install.sh)"
```

Debian:

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/SilverBlogTeam/SilverBlog/master/install/debian_install.sh)"
```

Arch Linux:

```
bash -c "$(https://raw.githubusercontent.com/SilverBlogTeam/SilverBlog/master/install/archlinux_install.sh)"
```


You can select a theme in [SilverBlogTheme](https://github.com/SilverBlogTheme), then use `./manage.py` to install the configuration and configure it correctly in the configuration file below.

This installation script uses the nginx + uwsgi execution mode by default. You can put the auto-generated `nginx_config` file into your nginx package's website configuration directory. If you need to use a third-party web client, don't forget to modify the CORS configuration in `nginx_config`.

## Configure Your SilverBlog

You need to use `./manage.py setting` to initialize your system information.

You need to edit `menu.json` and `menu.json` as the configuration file for the navigation bar:

```
[
  {
    "title": "Homepage", (Name of display)
    "name": "hello-world", (Optional, article name. Cannot exist with absolute.)
    "absolute": "https://demo.silverblog.org" (Optional, absolute path address, cannot exist with name.)
  }
]
```

## start operation

You can run SilverBlog using tools such as Tmux or Screen. You just need to execute `python3 watch.py` to open your blog.

You can use the `--control` parameter to run the management server.

If you need to run blogs and manage servers simultaneously in a container, use the `python3 watch.py ​​--control --docker` command. We do not recommend this method of operation if conditions permit.

## Keep running and monitoring your blog

Containers started with docker-compose are automatically restarted. You just need to ensure that the Docker service starts automatically when it starts up.

You can configure your server using the `systemd_startup_install.sh` file in the install directory, which requires root privileges. It is consistent with the recommended method below.

SilverBlog recommends using a NodeJS-based monitor: pm2

For the installation of pm2 see [GitHub - tj/n: Node version management](https://github.com/tj/n) and [pm2 - Quick Start](http://pm2.keymetrics.io/docs/Usage/quick-start/)

Then, you just have to run:

```
pm2 start pm2.json
```

It is possible to automatically restart SilverBlog after updating files or program errors.

You can also use:

```
pm2 startup
pm2 save
```

Enables your SilverBlog to start automatically when the system is powered on.

## How to use administrative scripts

You can use `./manage.py -h` at any time to get the help information for the SilverBlog management module.

Directly typing `./manage.py` will enter the whiptail build's graphical environment.

## Using the github page feature

You can use `git clone https://${personal_access_tokens}@github.com/${your_repo} static_page` to initialize your Github Page repository.

Don't forget to initialize your submit user information using the following command:

```
cd static_page
git config user.email "youremail@google.com"
git config user.name "your name"
```

Next, you just need to execute the Build static page command. The system will automatically generate a static page and submit it to the github page.

You can try using the `/example/.travis.yml` script for automated submission. (experimental feature, not guaranteed)


## Use client management server

Warning! If you need to use the SilverBlog client, make sure you use the https security protocol. Using http is like telling a password to a hacker! This may compromise your server security!

You can download the latest android client at https://github.com/SilverBlogTeam/SilverBlog_Android/releases.

You can compile and deploy the https://github.com/SilverBlogTeam/silverblog_ios IOS client yourself.

You can use Silver Create (https://c.silverblog.org) to manage your blog.

You can use pip to install the [qrcode_terminal](https://github.com/alishtory/qrcode-terminal) dependency, and then execute `./manage.py qrcode` to generate the automated configuration QR code.

## Switch to developer preview

SilverBlog is now available as a developer preview version. You can switch from `git checkout nightly` to the developer preview in the repository root directory. This version may have undiscovered bugs. Please use it with caution.

## Participate in development

We welcome you to report issue or pull request on GitHub of the SilverBlog project.

If you are not yet familiar with GitHub's Fork and Pull development model, you can read the [GitHub Documentation](https://help.github.com/articles/using-pull-requests) for more information.

We recommend that you use the Chinese language to raise an issue, and attach an English translation below to make it easier for non-Chinese native language developers to read and understand.

## Thanks

Thanks to [@Liqueur Librazy](https://github.com/Librazy) for providing the demo program server for this project.

Thanks [Jetbrains](https://www.jetbrains.com/) for providing a free All product IDE for this project
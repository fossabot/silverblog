#!/usr/bin/env bash
command -v docker >/dev/null 2>&1 || { echo >&2 "This installation method relies on Docker, but does not find Docker. Please install Docker and try again."; exit 1; }
docker pull qwe7002/silverblog

if [ ! -f "install.sh" ]; then
    git clone https://github.com/SilverBlogTeam/SilverBlog.git --depth=1
    cd SilverBlog/install
fi

./install.sh

cd ..

sed -i '''s/127.0.0.1/0.0.0.0/g' uwsgi.json

cat << EOF >start.sh
#!/usr/bin/env bash
docker run -dit -v $(pwd):/home/SilverBlog --restart="always" --name="silverblog" -p 5000:5000 qwe7002/silverblog
docker run -dit -v $(pwd):/home/SilverBlog --restart="always" --name="silverblog_control" -p 5001:5001 qwe7002/silverblog uwsgi --json uwsgi.json:control
EOF
cat << EOF >attach-docker.sh
#!/usr/bin/env bash
docker run -it -v $(pwd):/home/SilverBlog qwe7002/silverblog bash

EOF

chmod +x manage.sh
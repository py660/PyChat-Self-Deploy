if [ ! -d "/tmp/nginx" ]; then
    mkdir /tmp/nginx
fi
export REPL_SLUG="py/pychat";
nginx -c ../nginx.conf -p ~/$REPL_SLUG/debug;
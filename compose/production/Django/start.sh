#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

# python manage.py compilemessages
# gunicorn config.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/app
gunicorn WxBlog.wsgi -w 4 -k gthread -b 0.0.0.0:8000
#`-w 2 表示启动 2 个 worker 用于处理请求（一个 worker 可以理解为一个进程），通常将 worker 数目设置为 CPU 核心数的 2-4 倍。
#
#-k gthread 指定每个 worker 处理请求的方式，根据大家的实践，指定为 gthread 的异步模式能获取比较高的性能，因此我们采用这种模式。
#
#-b 0.0.0.0:8000，将服务绑定到 8000 端口，运行通过公网 ip 和 8000 端口访问应用。
#
#访问 ip:8000（ip 为你服务器的公网 ip），应用成功访问了，但是我们看到样式完全乱了。别急，这不是 bug！此前我们使用 django 自带的开发服务器，它会自动帮我们处理静态样式文件，但是 Gunicorn 并不会帮我们这么做。因为处理静态文件并不是 Gunicorn 所擅长的事，应该将它交给更加专业的服务应用来做，比如 Nginx。
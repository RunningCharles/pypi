#### 1. 安装 Python
``` shell
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev curl -y
wget https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tgz
tar -xzf Python-3.12.1.tgz
./configure --prefix=/usr/local/python3.12 --enable-optimizations --with-ssl
make
sudo make install
sudo ln -s /usr/local/python3.12/bin/python3 /usr/bin/python3
sudo ln -s /usr/local/python3.12/bin/pip3 /usr/bin/pip3

pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
pip config set global.trusted-host mirrors.aliyun.com
vim /etc/pip.config
```

#### 2. Python 虚拟环境
``` shell
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
deactivate
pip freeze > requirements.txt
pip install -r requirements.txt
```

#### 3. 安装蓝牙库
```
LDFLAGS="-lm" pip install dbus-python
pip install bluezero
```

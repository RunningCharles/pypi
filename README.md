#### 1. 安装 Python
``` shell
./configure --prefix=/usr/local/python3.12 --enable-optimizations --with-ssl
make
sudo make install
ln -s /usr/local/python3.12/bin/python3 /usr/bin/python3
ln -s /usr/local/python3.12/bin/pip3 /usr/bin/pip3
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

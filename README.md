#### 1. 安装虚拟环境依赖包
``` shell
$ pip3 install virtualenv
```

#### 2. 创建项目虚拟环境
``` shell
$ virtualenv venv
```

#### 3. 启动虚拟环境
``` shell
$ source venv/bin/activate
```

#### 4. 退出虚拟环境
``` shell
$ deactivate
```

#### 5. 存储依赖环境
``` shell
pip freeze > requirements.txt
```

#### 5. 安装依赖环境
``` shell
pip install -r requirements.txt
```
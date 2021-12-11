# sekiro

sekiro框架部署，升级https

```shell
# 关闭uwsgi
killall -9 uwsgi
# 切换项目所在目录
cd /srv
# 删除项目文件夹
rm -rf sekiro/
# 重新拉取最新代码
git clone https://github.com/guoxianru/sekiro.git
# 切换项目根目录
cd sekiro/
# 切换虚拟环境
workon spider_py38
# 加载uwsgi配置
uwsgi --ini flaskuwsgi.ini
# 重启nginx服务
systemctl restart nginx
```

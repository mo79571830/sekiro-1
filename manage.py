# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2021-09-15
# @UpdateTime: 2021-09-15

import logging
import os

from flask import Flask, render_template
from flask_script import Manager, Server

logging.basicConfig(level=logging.INFO)
app = Flask(__name__, template_folder="templates")
manager = Manager(app)
manager.add_command("runserver", Server("0.0.0.0", port=5588))


def start_sekiro():
    os.popen("cd /srv/sekiro && sh /srv/sekiro/sekiro_run.sh")


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    return render_template("index.html")


@app.route("/start", methods=["GET"], strict_slashes=False)
def start():
    try:
        start_sekiro()
        return {"code": "1", "msg": "sekiro服务启动成功"}
    except:
        return {"code": "0", "msg": "sekiro服务启动失败"}


if __name__ == "__main__":
    manager.run()

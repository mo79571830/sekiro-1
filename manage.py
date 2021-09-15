# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2021-09-15
# @UpdateTime: 2021-09-15

import logging

from flask import Flask, render_template
from flask_script import Manager, Server

logging.basicConfig(level=logging.INFO)
app = Flask(__name__, template_folder="templates")
manager = Manager(app)
manager.add_command("runserver", Server("0.0.0.0", port=5000))


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    return render_template("index.html")


if __name__ == "__main__":
    manager.run()

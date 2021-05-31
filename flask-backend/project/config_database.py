import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# print()当你想取指定文件或目录的绝对路径（完整路径），想起OS模块不是有个取文件绝对路径的方法os.path.abspath()，马上拿来用！

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite://")  # hui bei ti dai
    SQLALCHEMY_TRACK_MODIFICATIONS = False

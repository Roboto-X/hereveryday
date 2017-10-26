# coding:utf-8
import logging
import datetime

logger = logging.getLogger("django")  # 为loggers中定义的名称


def convert_readable_img(imgsrc):
    return imgsrc.replace("blog", "")


def current_timestamp():
    return datetime.datetime.now()


def current_date():
    return current_timestamp().strftime("%Y-%m-%d")

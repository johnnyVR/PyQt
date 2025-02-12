#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年9月24日
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: QWebView.BlockAds
@description: 拦截请求
"""
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtWebKitWidgets import QWebView


__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019'
__Version__ = 'Version 1.0'


class RequestInterceptor(QNetworkAccessManager):

    def createRequest(self, op, originalReq, outgoingData):
        """创建请求
        :param op:           操作类型见http://doc.qt.io/qt-5/qnetworkaccessmanager.html#Operation-enum
        :param originalReq:  原始请求
        :param outgoingData: 输出数据
        """
        url = originalReq.url().toString()
        if url.find('pos.baidu.com') > -1 and url.find('ltu=') > -1:
            # 拦截百度联盟的广告
            print('block:', url)
            originalReq.setUrl(QUrl())

        return super(RequestInterceptor, self).createRequest(op, originalReq, outgoingData)


class Window(QWebView):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.page().setNetworkAccessManager(RequestInterceptor(self))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    w.load(QUrl('https://so.csdn.net/so/search/s.do?q=Qt&t=blog'))
    sys.exit(app.exec_())

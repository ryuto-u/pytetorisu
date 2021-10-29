#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyicloud import PyiCloudService

#以下は接続するicloudのアカウントとパスワードを記載します。
api = PyiCloudService('ryuto310@icloud.com', 'Ryuto1013')

def get_oauth():
    auth = api.devices
    return auth

if __name__ == '__main__':
    auth=get_oauth()
    print('\n')
    print(auth)
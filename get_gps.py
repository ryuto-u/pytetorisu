#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyicloud import PyiCloudService

#以下は接続するicloudのアカウントとパスワードを記載します。
api = PyiCloudService('ryuto310@icloud.com', 'Ryuto1013')

def get_oauth():
    # デバイスナンバーは、icloudに登録しているデバイスに応じて数が異なる。
    auth = api.devices[0].location()
    return auth

if __name__ == '__main__':
    auth = str(get_oauth())
    s=auth.find('longitude')
    e=auth.find(u'positionType')
    s1=auth.find(u'latitude')
    e1=auth.find(u'isOld')
    lng1 =float(auth[s+12:e-4])
    lat1 =float(auth[s1+11:e1-4])
    print('%3.14f,%3.14f'%(lng1,lat1))

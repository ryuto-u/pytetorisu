#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyicloud import PyiCloudService

#以下は接続するicloudのアカウントとパスワードを記載します。
api = PyiCloudService('XXXXXX@YYYYYYYYYY', 'password')

#ここから2段認証を実施する。
if api.requires_2fa:
    import click
    print "Two-factor authentication required. Your trusted devices are:"

    devices = api.trusted_devices
    for i, device in enumerate(devices):
        print "  %s: %s" % (i, device.get('deviceName',
            "SMS to %s" % device.get('phoneNumber')))

    device = click.prompt('Which device would you like to use?', default=0)
    device = devices[device]
    if not api.send_verification_code(device):
        print "Failed to send verification code"
        sys.exit(1)

    code = click.prompt('Please enter validation code')
    if not api.validate_verification_code(device, code):
        print "Failed to verify verification code"
        sys.exit(1)

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

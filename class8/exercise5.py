#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    devices = NetworkDevice.objects.all()

    start_time = datetime.now()

    for device in devices:

        creds = device.credentials
        remote_conn = ConnectHandler(
                device_type = device.device_type,
                port = device.port,
                secret = '',
                ip = device.ip_address,
                username = creds.username,
                password = creds.password
                )

        print "_" * 60
        print device
        print remote_conn.send_command("show version")

    print "=" * 60
    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)


if __name__ == "__main__":
    main()

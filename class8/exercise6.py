#!/usr/bin/env python
"""
Use threads and Netmiko to execute 'show version' on each device in the database.
Calculate the amount of time required to do this. What is the difference in time
between executing 'show version' sequentially versus using threads?
"""

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

import threading
import time

def show_version(device):
    creds = device.credentials
    remote_conn = ConnectHandler(
        device_type = device.device_type,
        port = device.port,
        secret = '',
        ip = device.ip_address,
        username = creds.username,
        password = creds.password
            )

    # print "_" * 60
    # print device
    # print remote_conn.send_command("show version")
    print "-" * 60 + "\n" + "\n" + remote_conn.send_command("show version")



def main():
    django.setup()

    devices = NetworkDevice.objects.all()

    start_time = datetime.now()

    for device in devices:
        #Notice a tuple is used rather than an argument in the below
        my_thread = threading.Thread(target=show_version, args=(device,))
        my_thread.start()

    main_thread = threading.currentThread()
    # The below is to block the threading process until all threads have completed
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()

    print "=" * 60
    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)


if __name__ == "__main__":
    main()

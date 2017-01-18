from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    new_device1 = NetworkDevice(
        device_name='new_device1',
        device_type='juniper_mx',
        ip_address='192.168.100.1',
        port=22,
    )
    new_device1.save()

    new_device2 = NetworkDevice.objects.get_or_create(
        device_name='new_device2',
        device_type='juniper_mx',
        ip_address='192.168.100.2',
        port=22,
    )
    print new_device2

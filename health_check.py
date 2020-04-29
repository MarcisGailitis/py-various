#!/usr/bin/python3

# checks load for drive/CPU
import os
import psutil
import socket


# check reboot
def check_reboot():
    return os.path.exists("/run/reboot-required")


# disk usage
def check_disk_usage():
    return psutil.disk_usage('/')


# cpu usage
def check_cpu_usage():
    return psutil.cpu_percent(interval=2)


# ram usage
def check_ram_usage():
    return psutil.virtual_memory()


# check for network
def check_network():
    try:
        socket.gethostbyname('www.google.com')
        return True
    except:
        return False


def main():
    print(f'Reboot: {check_reboot()}')
    ssd = check_disk_usage()
    print(
        f'SSD free: {100-((ssd[1]/ssd[0])*100):.2f}%, '
        f'Tot/Used/Avail (in GB): {ssd[0]/(1_000_000_000):.2f} /'
        f'{ssd[1]/(1_000_000_000):.2f} / {ssd[2]/(1_000_000_000):.2f}'
    )
    ram = check_ram_usage()
    # print(ram)
    print(
        f'RAM free: {(1-(ram[3]/ram[0]))*100:.2f}%; '
        f'Tot/Used/Avail (in GB): {ram[0]/1_000_000_000:.2f} /'
        f'{ram[3]/1_000_000_000:.2f} / {ram[1]/1_000_000_000:.2f}')
    print(f'CPU free: {100 - check_cpu_usage()} %')
    print(f'Network: {check_network()}')


main()

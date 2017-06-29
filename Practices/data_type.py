# coding=utf-8
cp_mac = "4C-CC-6A-6E-37-09"
prefix_mac = cp_mac[:-3]
last_mac = cp_mac[-2:]
tmp_last_mac = int(last_mac, 16) + 1
new_last_mac = hex(tmp_last_mac)[2:]
if len(new_last_mac) < 2:
    new_pc_mac = prefix_mac + "-" + "0" + new_last_mac.upper()
else:
    new_pc_mac = prefix_mac + "-" + new_last_mac.upper()
print (new_pc_mac)

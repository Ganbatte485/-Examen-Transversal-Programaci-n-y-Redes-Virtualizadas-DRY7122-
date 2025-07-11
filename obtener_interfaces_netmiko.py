from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.104",
    "username": "cisco",
    "password": "cisco123!",
}

net_connect = ConnectHandler(**router)

output_ipv4 = net_connect.send_command("show ip interface brief")
output_ipv6 = net_connect.send_command("show ipv6 interface brief")

with open("evidencia_interfaces_netmiko.txt", "w") as file:
    file.write("===== IPv4 Interfaces =====\n")
    file.write(output_ipv4)
    file.write("\n\n===== IPv6 Interfaces =====\n")
    file.write(output_ipv6)

print("✅ Información de interfaces obtenida y guardada.")

net_connect.disconnect()

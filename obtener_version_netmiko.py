from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.104",
    "username": "cisco",
    "password": "cisco123!",
}

net_connect = ConnectHandler(**router)

output_version = net_connect.send_command("show version")

with open("evidencia_show_version_netmiko.txt", "w") as file:
    file.write("===== show version =====\n")
    file.write(output_version)

print("✅ Información de versión obtenida y guardada.")

net_connect.disconnect()

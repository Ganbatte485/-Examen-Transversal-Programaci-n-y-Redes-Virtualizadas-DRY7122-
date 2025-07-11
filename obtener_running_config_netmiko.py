from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.104",
    "username": "cisco",
    "password": "cisco123!",
}

net_connect = ConnectHandler(**router)

running_config = net_connect.send_command("show running-config")

with open("evidencia_running_config_netmiko.txt", "w") as file:
    file.write("==== Running Configuration ====\n")
    file.write(running_config)

print("✅ Running-config obtenido y guardado.")

net_connect.disconnect()

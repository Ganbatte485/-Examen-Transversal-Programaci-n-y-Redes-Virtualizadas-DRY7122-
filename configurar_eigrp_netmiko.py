from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.104",
    "username": "cisco",
    "password": "cisco123!",
}

net_connect = ConnectHandler(**router)

config_commands = [
    "ipv6 unicast-routing",
    "router eigrp MY-EIGRP",
    "address-family ipv4 unicast autonomous-system 10",
    "af-interface GigabitEthernet1",
    "no passive-interface",
    "exit-af-interface",
    "network 192.168.56.0 0.0.0.255",
    "exit-address-family",
    "address-family ipv6 unicast autonomous-system 10",
    "af-interface GigabitEthernet1",
    "no passive-interface",
    "exit-af-interface",
    "exit"
]

output = net_connect.send_config_set(config_commands)

eigrp_section = net_connect.send_command("show running-config | section eigrp")

with open("evidencia_eigrp_netmiko.txt", "w") as file:
    file.write(output)
    file.write("\n\n")
    file.write("==== SALIDA show running-config | section eigrp ====\n")
    file.write(eigrp_section)

print("✅ Configuración completada y evidencia guardada.")

net_connect.disconnect()

from ncclient import manager

with manager.connect(
    host="192.168.56.104",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:
    print("Conexión NETCONF establecida. Capacidades del servidor:")
    for capability in m.server_capabilities:
        print(capability)

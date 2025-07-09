from ncclient import manager

hostname_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Rodriguez-Aguilera-Ponce-Contreras</hostname>
  </native>
</config>
"""

with manager.connect(
    host="192.168.56.104",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:
    response = m.edit_config(target="running", config=hostname_config)
    print(response)

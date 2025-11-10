

from pyats.topology import loader

# 1. Load the testbed file
testbed = loader.load("testbed.yaml")

# 2. Pick one device (R1)
device = testbed.devices["R1"]

# 3. Connect to the device
print(f"Connecting to {device.name}...")
device.connect(log_stdout=True)

# 4. Run a simple command
output = device.execute("show ip interface brief")
print("\n===== show ip interface brief =====")
print(output)

# 5. Disconnect
device.disconnect()
print("\nDisconnected.")

#pip install bleak

import asyncio
from bleak import BleakScanner


async def scan_for_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Nombre: {device.name}, Dirección: {device.address}")

# Ejecutar el escaneo
asyncio.run(scan_for_devices())
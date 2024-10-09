#pip install bleak

import asyncio
from bleak import BleakScanner


async def run():
    print("Buscando dispositivos BLE...")
    dispositivos = await BleakScanner.discover()
    for dispositivo in dispositivos:
        print(f"Dispositivo: {dispositivo.name}, Dirección: {dispositivo.address}")

# Ejecutar la función asíncrona
asyncio.run(run())
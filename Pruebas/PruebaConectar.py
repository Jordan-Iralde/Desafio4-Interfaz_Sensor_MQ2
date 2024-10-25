import asyncio
from bleak import BleakClient

address = "30:38:F7:39:80:3C"  # Reemplaza con la dirección MAC de tu dispositivo
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"  # UUID de la característica que quieras leer

async def run(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))

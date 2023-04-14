from telethon import TelegramClient, events
import asyncio


async def main(api_id, api_hash, user_receive_id, user_id, time_sleep):
    client = TelegramClient('BanditFarm', api_id, api_hash)
    print('Starting...')

    await client.start()
    print('Connected to Telegram API.')

    while True:
        await client.send_message(user_receive_id, 'я')
        await asyncio.sleep(2)
        await client.send_message(user_receive_id, 'бизнес')
        await asyncio.sleep(2)
        await client.send_message(user_receive_id, 'снять деньги')
        await asyncio.sleep(2)
        await client.send_message(user_receive_id, 'сырье все')
        await asyncio.sleep(2)
        await client.send_message(user_receive_id, 'кинуть ' + user_id + ' все')

        print('Done! Waiting ' + str(time_sleep) + ' seconds!')

        await asyncio.sleep(time_sleep)

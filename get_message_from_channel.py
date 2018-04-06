from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon import TelegramClient, events
channel_id=''
channel_name=''
date_message=''
message=''
charset='utf8'
# channel_lists=[1148331688,1270880234]
channel_lists=[1152922969]
api_id = '231412'
api_hash = '0e22e808b7d79184d38b7e6124822df0'
phone = '+84997718737'
client = TelegramClient('session_name', api_id, api_hash,update_workers=1, spawn_read_thread=False)
client.start()
@client.on(events.NewMessage)
def my_event_handler(update):
    if (update.message.message):
        # channel id
        channel_id = update.message.to_id.channel_id
        # channel name
        channel_name = client.get_entity(PeerChannel(update.message.to_id.channel_id)).username
        # channel message Date
        date_message = update.message.date
        # channel message
        message = update.message.message
        # print(channel_name,"-----",channel_id,"------",date_message,"-----",message)
        if (channel_id in channel_lists):
            client.send_message(PeerChannel(1194529271), message)
client.idle()
from init import *

ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
heart = ws.recv()
auth = {
    "op": 2,
    "d": {
        "token": token,
        "properties": {
            "os": "windows",
            "browser": "chrome",
            "device": "pc"
        },
    }
}
ws.send(json.dumps(auth))
res = json.loads(ws.recv())

def triggerSlashCommand(command_name, command_id, channel_id, guild_id):

    payload = {
        "type": 2,
        "guild_id": guild_id,
        "channel_id": channel_id,
        "application_id":"270904126974590976",
        "session_id":  res["d"]["session_id"],
        "data": {
            "version":"1011560371645063234",
            
            "id": command_id,
            "name": command_name,
            
            "type":1,
            "options":[],
            "application_command": {
                "id": command_id,
                "application_id":"270904126974590976",
                "version":"1011560371645063234",
                "default_permission":"true",
                "default_member_permissions":"null",
                "type":1,

                "name": command_name,
                "dm_permission":"true"
            }
        }
    }
    req = requests.post('https://discord.com/api/v9/interactions', headers={"authorization": token}, json=payload)
    print(req.text)
    ws.close()

    show(command_name.upper() + "ED")

def Deposit(channel_id, guild_id):

    payload = {
        "type":2,
        "application_id":"270904126974590976",
        "guild_id": guild_id,
        "channel_id": channel_id,
        "session_id":  res["d"]["session_id"],
        
        "data": {
            "version":"1011560371351470199",
            "id": dankCommands["deposit"],
            
            "name":"deposit",
            "type":1,
            "options": [
                {
                    "type":3,
                    "name":"amount",
                    "value":"max"
                }
            ],
            
            "application_command": {
                "id": dankCommands["deposit"],
                "application_id":"270904126974590976",
                "version":"1011560371351470199",
                "default_permission": "true",
                "default_member_permissions": "null",
                "type":1,
                
                "name":"deposit",
                "description":"Deposit money into your bank.",
                "dm_permission": "true",
                
                "options":[
                    {
                        "type":3,
                        "name":"amount",
                        "description":"A constant number like \"123\", a shorthand (\"2k\"), or a relative keyword like \"30%\" or \"max\".",
                        "required": "true"
                    }
                ]
            },
            "attachments":[]
        },
    }
    req = requests.post('https://discord.com/api/v9/interactions', headers={"authorization": token}, json=payload)
    ws.close()

    show("DEPOSITED")

def Beg(channel_id, guild_id):

    payload = {
        "type":2,
        "application_id":"270904126974590976",
        "guild_id": guild_id,
        "channel_id": channel_id,
        "session_id":  res["d"]["session_id"],
        
        "data": {
            "version":"1011560371603132434",

            "id": dankCommands["beg"],
            "name":"beg",  
            "type":1,
            "options":[],
            
            "application_command": {
                "id": dankCommands["beg"],
                "application_id":"270904126974590976",
                "version":"1011560371603132434",
                "default_permission": "true",
                "default_member_permissions": "null",
                "type":1,
                
                "name":"beg",
                "description":"Beg for coins to help bolster your pocket balance",
                "dm_permission": "true"
            },
            
            "attachments": []
        },
    }
    req = requests.post('https://discord.com/api/v9/interactions', headers={"authorization": token}, json=payload)
    ws.close()

    show("BEGGED")

def Hunt(channel_id, guild_id):

    payload = {
        "type":2,
        "application_id":"270904126974590976",
        "guild_id": guild_id,
        "channel_id": channel_id,
        "session_id":  res["d"]["session_id"],
        
        "data":{
            "version":"1011560371645063237",
            "id":"1011560371171102760",
            
            "name":"hunt",
            "type":1,
            "options":[],
            "application_command":{
                "id":"1011560371171102760",
                "application_id":"270904126974590976",
                "version":"1011560371645063237",
                "default_permission": "true",
                "default_member_permissions": "null",
                
                "type":1,
                "name":"hunt",
                "description":"Grab a rifle from the shop and go hunting!",
                "dm_permission": "true"
            },
            "attachments":[]
        },
    }
    req = requests.post('https://discord.com/api/v9/interactions', headers={"authorization": token}, json=payload)
    ws.close()

    show("HUNTED")

def Dig(channel_id, guild_id):

    payload = {"type":2,"application_id":"270904126974590976","guild_id": guild_id,"channel_id": channel_id,"session_id":  res["d"]["session_id"],"data":{"version":"1011560371645063232","id":"1011560371078832204","name":"dig","type":1,"options":[],"application_command":{"id":"1011560371078832204","application_id":"270904126974590976","version":"1011560371645063232","default_permission": "true","default_member_permissions": "null","type":1,"name":"dig","description":"Dig in the dirt for bugs and other items","dm_permission":"true"},"attachments":[]},}
    req = requests.post('https://discord.com/api/v9/interactions', headers={"authorization": token}, json=payload)
    ws.close()

    show("DIGGED")
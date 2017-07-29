import prof
import requests
import os
import time
import datetime

webhook_address = "YOUR_URL_HERE"


def prof_on_start():
    prof.cons_show("Profanity has started...")
    prof.cons_show("Discord Forwarding Enabled")

def prof_post_chat_message_display(barejid, resource, message):
    st = datetime.datetime.utcnow().isoformat()
    if barejid == "TARGET_JID_HERE":
        prof.cons_show("JID IS " + barejid)
        prof.cons_show("MESSAGE IS " + message)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            }
        payload = {
                    "embeds":[{
                        "description": "```"+ message +"```\n ***THIS IS PING HAS BEEN AUTOMATICALLY FORWARDED FROM JABBER***",
                        "url": "https://discordapp.com",
                        "color": 16259585,
                        "timestamp": st,
                            "footer":{
                                "icon_url": "YOURAVATARHERE",
                                "text": "Service by YOURNAMEHERE"
                            },
                            "thumbnail":{
                              "url": "CORPORALLIANCELOGO"
                            },
                        "author":{
                          "name": barejid,
                          "url": "JIDURLTARGET",
                          "icon_url": "CORPORALLIANCELOGO"
                        }
                    }]
                  }
        r = requests.post(webhook_address, headers=headers, json=payload)
    else:
        prof.cons_show("Message not a ping")

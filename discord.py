import prof
import requests
import os
import time
import datetime
import re

webhook_address = "YOUR_URL_HERE"
footer_icon = "YOUR_AVATAR_HERE"
svc_by = "YOUR_NAME_HERE"
logo_url = "CORP/ALLIANCE_LOGO_URL_HERE"
jid_url = "LINK_FOR_JID"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

def prof_on_start():
    prof.cons_show("Profanity has started...")
    prof.cons_show("Discord Forwarding Enabled")

def prof_post_chat_message_display(barejid, resource, message):
    st = datetime.datetime.utcnow().isoformat()
    if barejid == "TARGET_JID_HERE":
        prof.cons_show("JID IS " + barejid)
        prof.cons_show("MESSAGE IS " + message)
        check = message
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', check)
        if len(urls) == 0:
            urlstr = ""
        else:
            urlstr = "**PING CONTAINS THE FOLLOWING URLS** \n> " + ' \n> '.join(urls) + "\n\n"
        prof.cons_show("URLS: "+ urlstr)
        payload = {
                    "embeds":[{
                        "description": "```"+ message +"```\n "+ urlstr +" ***THIS IS PING HAS BEEN AUTOMATICALLY FORWARDED FROM JABBER***",
                        "url": "https://discordapp.com",
                        "color": 16259585,
                        "timestamp": st,
                            "footer":{
                                "icon_url": footer_icon,
                                "text": "Service by "+ svc_by
                            },
                            "thumbnail":{
                              "url": logo_url
                            },
                        "author":{
                          "name": barejid,
                          "url": jid_url,
                          "icon_url": logo_url
                        }
                    }]
                  }
        r = requests.post(webhook_address, headers=headers, json=payload)
    else:
        prof.cons_show("Message not a ping")

def prof_on_disconnect(account_name, fulljid):
    payload = {
            "embeds":[{
                "description": ":warning:***WARNING***:warning: \n\n **JABBER PING FORWARDING IS DOWN! (Reason: D)** \n **PLEASE NOTIFY "+ svc_by +" ASAP!** \n\n :warning:***WARNING***:warning:",
                "url": "https://discordapp.com",
                "color": 16776960,
                "timestamp": st,
                    "footer":{
                        "icon_url": footer_icon,
                        "text": "Service by "+ svc_by
                    },
                    "thumbnail":{
                      "url": "http://icons.iconarchive.com/icons/martz90/hex/128/warning-icon.png"
                    },
                "author":{
                  "name": "EMERGENCY ALERT BROADCAST SYSTEM",
                  "url": "",
                  "icon_url": "http://icons.iconarchive.com/icons/martz90/hex/128/warning-icon.png"
                }
            }]
        }
    r = requests.post(webhook_address, headers=headers, json=payload)

def prof_on_shutdown():
    payload = {
            "embeds":[{
                "description": ":warning:***WARNING***:warning: \n\n **JABBER PING FORWARDING IS DOWN!** \n **PLEASE NOTIFY "+ svc_by +" ASAP! (Reason: S)** \n\n :warning:***WARNING***:warning:",
                "url": "https://discordapp.com",
                "color": 16776960,
                "timestamp": st,
                    "footer":{
                        "icon_url": footer_icon,
                        "text": "Service by "+ svc_by
                    },
                    "thumbnail":{
                      "url": "http://icons.iconarchive.com/icons/martz90/hex/128/warning-icon.png"
                    },
                "author":{
                  "name": "EMERGENCY ALERT BROADCAST SYSTEM",
                  "url": "",
                  "icon_url": "http://icons.iconarchive.com/icons/martz90/hex/128/warning-icon.png"
                }
            }]
        }
    r = requests.post(webhook_address, headers=headers, json=payload)

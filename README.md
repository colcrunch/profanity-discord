# profanity-discord

**THIS PLUGIN IS NO LONGER RECIEVING UPDATES.**

**PLEASE LOOK AT RUNNUNG AN INSTANCE OF [KILLBOT](http://github.com/colcrunch/killbot) WITH THE JabberPings EXTENSION ENABLED INSTEAD**

A plugin for proafnity to forward jabber pings on to discord through a webhook.


# Install
1. Install profanity 0.5.0+ (http://profanity.im)
   * Note: If you need manual TLS certificate management, use libmesode rather than libstrophe.
2. Install requests (http://docs.python-requests.org/en/master/)
3. Download the plugin.
4. Edit discord.py with your webhook, the jid that pings come from, logos, and any other information you want to provide along with the pings. (YOU MUST PUT SOMETHING IN FOR THE LOGO AND ICON URLS, otherwise discord will not accept the request)
5. Install the plugin in profanity with the command `/plugins install PATH_TO/discord.py`
6. Restart the client, log in, and let the pings pour in.

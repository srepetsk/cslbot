#!/usr/bin/python3 -OO
import logging
import imp
import irc.bot
from config import CHANNEL, NICK, NICKPASS, HOST
import handler


class MyBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nick, nickpass, host, port=6667):
        if nickpass != '':
            server = irc.bot.ServerSpec(host, port, nickpass)
        else:
            server = irc.bot.ServerSpec(host, port)
        irc.bot.SingleServerIRCBot.__init__(self, [server], nick, nick)
        self.channel = channel
        self.handler = handler.MyHandler()

    def on_welcome(self, c, e):
        logging.info("Connected to server")
        c.join(self.channel)

    def on_join(self, c, e):
        self.handler.channel = self.channels[CHANNEL]

    def on_pubmsg(self, c, e):
        command = e.arguments[0].strip().split()[0]
        if command == '!reload':
            imp.reload(handler)
            self.handler = handler.MyHandler()
            self.handler.channel = self.channels[CHANNEL]
        self.handler.pubmsg(c, e)

    def get_version(self):
        return "Ircbot -- 1.0"


def main():
    bot = MyBot(CHANNEL, NICK, NICKPASS, HOST)
    bot.start()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

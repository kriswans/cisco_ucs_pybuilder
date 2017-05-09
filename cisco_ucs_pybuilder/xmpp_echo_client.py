"""
    This was modified by kriswans@cisco.com to add:
    multiprocessing and conditional responses.
"""

"""
    Slixmpp: The Slick XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of Slixmpp.
    See the file LICENSE for copying permission.
"""

import logging
from getpass import getpass
from argparse import ArgumentParser
import multiprocessing
import sys

import slixmpp


class EchoBot(slixmpp.ClientXMPP):

    """
    A simple Slixmpp bot that will echo messages it
    receives, along with a short thank you message.
    """

    def __init__(self, jid, password):
        #
        p = multiprocessing.current_process()
        print ('Starting_main:', p.name, p.pid)
        sys.stdout.flush()
        #
        slixmpp.ClientXMPP.__init__(self, jid, password)

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler("session_start", self.start)

        # The message event is triggered whenever a message
        # stanza is received. Be aware that that includes
        # MUC messages and error messages.
        self.add_event_handler("message", self.message)

    def start(self, event):
        #
        p = multiprocessing.current_process()
        print ('Starting_start:', p.name, p.pid)
        sys.stdout.flush()
        #
        """
        Process the session_start event.
        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.
        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        #
        y = multiprocessing.current_process()
        print ('Starting_msg:', y.name, y.pid)
        sys.stdout.flush()
        #
        """
        Process incoming message stanzas. Be aware that this also
        includes MUC messages and error messages. It is usually
        a good idea to check the messages's type before processing
        or sending replies.
        Arguments:
            msg -- The received message stanza. See the documentation
                   for stanza objects and the Message stanza to see
                   how it may be used.
        """
        f=open("tmp/tmp_sp_builder",'r')
        flist=f.readlines()
        sp_time=str(flist[4])
        sp_time_s=sp_time.strip()
        if msg['type'] in ('chat', 'normal'):
            msg.reply("Thanks for sending\n\n < %(body)s >" % msg).send()
            msg.reply("\nThe last SDK created service profile(s) were at: "+sp_time_s+"\n").send()
            msgc=("%(body)s" % msg)
            if msgc == "yes":
                msg.reply("\nNO!\n").send()
            if msgc == "why":
                msg.reply("\nBecause I said so!\n").send()
            if msgc == "bye":
                sys.exit()
def xmpp_go(jid,password):
    z = multiprocessing.current_process()
    print ('Starting:', z.name, z.pid)
    sys.stdout.flush()

    xmpp = EchoBot(jid, password)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0004') # Data Forms
    xmpp.register_plugin('xep_0060') # PubSub
    xmpp.register_plugin('xep_0199') # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas.
    xmpp.connect()
    xmpp.process()

if __name__ == '__main__':
    import time
    # Setup the command line arguments.
    parser = ArgumentParser(description=EchoBot.__doc__)


    # JID and password options.
    parser.add_argument("-j", "--jid", dest="jid",
                        help="JID to use")
    parser.add_argument("-p", "--password", dest="password",
                        help="password to use")

    args = parser.parse_args()

    hdn=open("pvt/hdn",'r')
    hdnlist=hdn.readlines()
    pw=str(hdnlist[0])
    pw_s=pw.rstrip()

    usr=open("cfg/xmpp_cfg_fromto.txt",'r')
    usrlist=usr.readlines()
    usern=str(usrlist[0])
    usern_s=usern.rstrip()

    args.jid=usern_s
    jid=args.jid
    args.password=pw_s
    password=args.password



    if args.jid is None:
        args.jid = input("Username: ")
    if args.password is None:
        args.password = getpass("Password: ")

    # Setup the EchoBot and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    dm = multiprocessing.Process(name='XMPP_Echo_Client', target=xmpp_go, args=(jid,password))
    dm.daemon = True
    dm.start()
    time.sleep(10000)


    print('ok')

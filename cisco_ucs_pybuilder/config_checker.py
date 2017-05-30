def xmppAcctInfo():

    """Function to check for the existence of account information and credentials for the XMPP send/echo client"""
    """builds files that are not present"""

    import sys
    import glob
    import os
    import pprint

    os.chdir('cfg')

    cfgs=glob.glob("*")
    xmppcfg="xmpp_cfg_fromto.txt"
    if xmppcfg in cfgs:
        pass
    if xmppcfg not in cfgs:
        print ("Need to create a file which contains the sender and reciever of xmpp messages named : xmpp_cfg_fromto.txt|n")
        xfromto=open('xmpp_cfg_fromto.txt','w')
        xfromto.close()
        xfromto=open('xmpp_cfg_fromto.txt','a')
        xfrom=str(input("What XMPP account/JID will you be sending FROM in the format <user>@<domain>?\n:"))
        xto=str(input("What XMPP account/JID will you be sending TO in the format <user>@<domain>?\n:"))
        xfromto.write(xfrom+'\n')
        xfromto.write(xto+'\n')
        xfromto.close()

    os.chdir('..')

    usr=open("cfg/xmpp_cfg_fromto.txt",'r')
    usrlist=usr.readlines()
    usern=str(usrlist[0])
    usern_s=usern.rstrip()


    files=glob.glob("*")
    #ppfiles=pprint.pprint(files)
    pvt="pvt"

    if pvt in files:
        pass
    if pvt not in files:
        print("Need to create 'pvt' folder with 'hdn' password file\n")
        print("The hdn file will contain the password to log into the xmpp server\n")
        os.makedirs("pvt")
        cwd=(os.getcwd())
        os.chdir(cwd+'/pvt')
        xmpppwd=str(input("Please, enter your password to the XMPP server for account: {usern} \n:".format(usern=usern_s)))
        hdn=open('hdn', 'w')
        hdn.write(xmpppwd+"\n")
        hdn.close()
        os.chdir('..')

    os.chdir('pvt')

    pvtfiles=glob.glob("*")
    #pprint.pprint(pvtfiles)
    hdn='hdn'

    if hdn in pvtfiles:
        pass
    if hdn not in pvtfiles:
        print("Inside 'pvt' folder there is a 'hdn' password file\n")
        print("The hdn file will contain the password to log into the xmpp server\n")
        xmpppwd=str(input("Please, enter your password to the XMPP server for account: {usern} \n:".format(usern=usern_s)))
        hdn=open('hdn', 'w')
        hdn.write(xmpppwd+"\n")
        hdn.close()


    os.chdir('..')

xmppAcctInfo()

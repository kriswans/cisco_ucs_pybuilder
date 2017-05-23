####
#Author: kriswans@cisco.com
#https://github.com/kriswans/ucs-py-tools
###


def PolBuildout(default,handle,os_num):
    import server_lcp
    import server_scp
    import UUIDSUF
    import extmgt
    import bootpol
    server_lcp.ServerLCP(default,handle,os_num)
    server_scp.ServerSCP(default,handle,os_num)
    UUIDSUF.UUIDsuffix(default,handle)
    extmgt.ExtMgtPool(default,handle)
    bootpol.bootpol_DVDSDLOCAL(handle)

def SPTemp_and_BulkSP(handle):

    import time
    import datetime
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    f=open("tmp/tmp_sp_builder",'a')
    f.write(st)
    f.close()

    f=open("tmp/tmp_sp_builder",'r')
    flist=f.readlines()
    lcp=str(flist[0])
    lcp_s=lcp.rstrip()
    scp=str(flist[1])
    scp_s=scp.rstrip()
    uuid=str(flist[2])
    uuid_s=uuid.rstrip()
    extmgt=str(flist[3])
    extmgt_s=extmgt.rstrip()
    f.close()
    print("The Pools for the service profiles used are:\n")
    print(lcp+'\n'+scp+'\n'+uuid+'\n'+extmgt+'\n')

    f=open("prod/macp_prod",'r')
    flist=f.readlines()
    nicpola=str(flist[3])
    nicpola_s=nicpola.rstrip()
    nicpolb=str(flist[4])
    nicpolb_s=nicpolb.rstrip()
    f.close()

    from ucsmsdk.mometa.ls.LsServer import LsServer
    from ucsmsdk.mometa.vnic.VnicConnDef import VnicConnDef
    from ucsmsdk.mometa.vnic.VnicEther import VnicEther
    from ucsmsdk.mometa.vnic.VnicFcNode import VnicFcNode
    from ucsmsdk.mometa.vnic.VnicFc import VnicFc
    from ucsmsdk.mometa.fabric.FabricVCon import FabricVCon
    from ucsmsdk.mometa.ls.LsPower import LsPower

    mo = LsServer(parent_mo_or_dn="org-root", ext_ip_state="pooled", ext_ip_pool_name=(extmgt_s), name=("SDK_"+des_str+"_"+osn+"_SPTEMP"), boot_policy_name="DVD-SD-Local", ident_pool_name=(uuid_s), local_disk_policy_name="default", type="updating-template")
    mo_1 = VnicConnDef(parent_mo_or_dn=mo, san_conn_policy_name=(scp_s), lan_conn_policy_name=(lcp_s))
    mo_2 = VnicEther(parent_mo_or_dn=mo, order="4", cdn_source="vnic-name", pin_to_group_name="", cdn_prop_in_sync="yes", qos_policy_name="", admin_cdn_name="", nw_templ_name="", admin_vcon="any", addr="derived", mtu="9000", nw_ctrl_policy_name="", adaptor_profile_name="", name=(nicpolb_s), ident_pool_name="", switch_id="A", stats_policy_name="default", admin_host_port="ANY")
    mo_3 = VnicEther(parent_mo_or_dn=mo, order="3", cdn_source="vnic-name", pin_to_group_name="", cdn_prop_in_sync="yes", qos_policy_name="", admin_cdn_name="", nw_templ_name="", admin_vcon="any", addr="derived", mtu="9000", nw_ctrl_policy_name="", adaptor_profile_name="", name=(nicpola_s), ident_pool_name="", switch_id="A", stats_policy_name="default", admin_host_port="ANY")
    mo_4 = VnicFcNode(parent_mo_or_dn=mo, addr="pool-derived", ident_pool_name="node-default")
    mo_5 = VnicFc(parent_mo_or_dn=mo, order="2", cdn_source="vnic-name", pin_to_group_name="", cdn_prop_in_sync="yes", qos_policy_name="", admin_cdn_name="", nw_templ_name="", max_data_field_size="2048", admin_vcon="any", pers_bind_clear="no", addr="derived", pers_bind="disabled", adaptor_profile_name="", name="B", ident_pool_name="", switch_id="A", stats_policy_name="default", admin_host_port="ANY")
    mo_6 = VnicFc(parent_mo_or_dn=mo, order="1", cdn_source="vnic-name", pin_to_group_name="", cdn_prop_in_sync="yes", qos_policy_name="", admin_cdn_name="", nw_templ_name="", max_data_field_size="2048", admin_vcon="any", pers_bind_clear="no", addr="derived", pers_bind="disabled", adaptor_profile_name="", name="A", ident_pool_name="", switch_id="A", stats_policy_name="default", admin_host_port="ANY")
    mo_7 = FabricVCon(parent_mo_or_dn=mo, select="all", share="shared", id="1", placement="physical", transport="ethernet,fc", fabric="NONE", inst_type="auto")
    mo_8 = FabricVCon(parent_mo_or_dn=mo, select="all", share="shared", id="2", placement="physical", transport="ethernet,fc", fabric="NONE", inst_type="auto")
    mo_9 = FabricVCon(parent_mo_or_dn=mo, select="all", share="shared", id="3", placement="physical", transport="ethernet,fc", fabric="NONE", inst_type="auto")
    mo_10 = FabricVCon(parent_mo_or_dn=mo, select="all", share="shared", id="4", placement="physical", transport="ethernet,fc", fabric="NONE", inst_type="auto")
    mo_11 = LsPower(parent_mo_or_dn=mo, state="admin-up")
    handle.add_mo(mo)

    handle.commit()


    from ucsmsdk.ucsmethodfactory import ls_instantiate_n_named_template
    from ucsmsdk.ucsbasetype import DnSet, Dn

    dn_set = DnSet()
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP1")
    dn_set.child_add(dn)
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP2")
    dn_set.child_add(dn)
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP3")
    dn_set.child_add(dn)
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP4")
    dn_set.child_add(dn)
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP5")
    dn_set.child_add(dn)
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP6")
    dn_set.child_add(dn)
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP7")
    dn_set.child_add(dn)
    dn = Dn()
    dn.attr_set("value","SDK_"+des_str+"_"+osn+"_SP8")
    dn_set.child_add(dn)
    elem = ls_instantiate_n_named_template(cookie=handle.cookie, dn=("org-root/ls-SDK_"+des_str+"_"+osn+"_SPTEMP"), in_error_on_existing="true", in_name_set=dn_set, in_target_org="org-root", in_hierarchical="false")
    mo_list = handle.process_xml_elem(elem)




if __name__ == "__main__":
    import sys
    import server_lcp
    import server_scp
    import UUIDSUF
    import extmgt
    import bootpol
    from ucsmsdk.ucshandle import UcsHandle
    import time
    import os
    import multiprocessing

    ucssys=input("Enter the IP or hostname: ")
    admin=input("Enter Admin user name: ")
    pwd=input("Enter password: ")
    default=int(input("Use defaults? yes=1, no=0: "))
    osnum=int(input("Enter OS index: 1. LNX, 2. WIN, 3. VMW:  "))
    desig=int(input("Enter numeric designator for SP Template (0-99):  "))
    des_str=str(desig)
    handle = UcsHandle(ucssys,admin,pwd, port=443)#.format(ucssysf=ucssys,adminf=admin,pwdf=pwd)
    handle.login()
    if osnum==1:
        osn="LNX"
        os_ad="Linux"
        os_num=1
        os_name="Linux"
    if osnum==2:
        osn="WIN"
        os_ad="Windows"
        os_num=2
        os_name="Windows"
    if osnum==3:
        osn="VMW"
        os_ad="VMWare"
        os_num=3
        os_name="VMWare"
    if osnum > 3:
        print ("Bad value, exiting...")
        sys.exit()
    if desig < 0 or desig > 99:
        print ("Bad value, exiting...")
        sys.exit()


    PolBuildout(default,handle,os_num)
    SPTemp_and_BulkSP(handle)


    import logging
    from getpass import getpass
    from argparse import ArgumentParser
    import slixmpp
    import xmpp_msg_client
    import xmpp_echo_client
    import os
    import time
    import multiprocessing

    hdn=open("pvt/hdn",'r')
    hdnlist=hdn.readlines()
    pw=str(hdnlist[0])
    pw_s=pw.rstrip()

    usr=open("cfg/xmpp_cfg_fromto.txt",'r')
    usrlist=usr.readlines()
    usern=str(usrlist[0])
    usern_s=usern.rstrip()
    recip=str(usrlist[1])
    recip_s=recip.rstrip()

    jid=usern_s
    password=pw_s
    to=recip_s

    message=("You Have new "+os_ad+" service profiles to apply at "+ucssys)

    dm = multiprocessing.Process(name='XMPP_Send_Client', target=xmpp_msg_client.xmpp_send, args=(jid,password,to,message))
    dm.daemon = True
    dm.start()
    time.sleep(10)

    print('\nOK, starting the pybot to field incoming IMs for the next 8 hours.\n')

    sdm = multiprocessing.Process(name='XMPP_Echo_Client', target=xmpp_echo_client.xmpp_go, args=(jid,password))
    sdm.daemon = True
    sdm.start()
    time.sleep(28800)

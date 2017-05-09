###
#Author: kriswans@cisco.com, https://github.com/kriswans/ucs-py-tools
##This program creates a Lan Connectivity Policy and the parameters contained therein. This is for a dual NIC system using jumbo frames
###

def ServerLCP(default,handle):
    from ucsmsdk.ucshandle import UcsHandle
    from ucsmsdk.mometa.macpool.MacpoolPool import MacpoolPool
    from ucsmsdk.mometa.macpool.MacpoolBlock import MacpoolBlock
    from ucsmsdk.mometa.macpool.MacpoolPool import MacpoolPool
    from ucsmsdk.mometa.macpool.MacpoolBlock import MacpoolBlock
    import sys
    import shutil
    import SPQuickBuilder





    #Call the function that pulls and updates the mac pool values
    SPQuickBuilder.ReadMacpPoolvalues(default,0,0,0)
    #The selected variables are placed in the macp_prod file. They need to be reformatted for the ucsmsdk calls.
    f=open("prod/macp_prod",'r')
    flist=f.readlines()
    nm=str(flist[0])
    nm_s=nm.rstrip()
    low=str(flist[1])
    low_s=low.rstrip()
    hi=str(flist[2])
    hi_s=hi.rstrip()
    nicpola=str(flist[3])
    nicpola_s=nicpola.rstrip()
    nicpolb=str(flist[4])
    nicpolb_s=nicpolb.rstrip()
    lcp=str(flist[5])
    lcp_s=lcp.rstrip()
    macp=nm_s
    f.close()
    print(nm+'\n'+low+'\n'+hi+'\n'+nicpola+'\n'+nicpolb+'\n'+lcp+'\n')

    #zero out the sp builder config file
    sp_builder=open("tmp/tmp_sp_builder",'w')
    sp_builder.close()
    #start appending to the sp builder. lcp will be the first built, then scp, uuid, bootpol.
    sp_builder=open("tmp/tmp_sp_builder",'a')
    sp_builder.write(lcp_s+'\n')
    sp_builder.close()


    try:
        mo = MacpoolPool(parent_mo_or_dn="org-root", name=(nm_s), assignment_order="sequential")
        mo_1 = MacpoolBlock(parent_mo_or_dn=mo, to=(hi_s), r_from=low_s)
        handle.add_mo(mo)

        handle.commit()
    except:
        print("Mac Pool already exists")

    ###change the mtu for the silver priority

    from ucsmsdk.mometa.qosclass.QosclassEthClassified import QosclassEthClassified

    try:
        mo = QosclassEthClassified(parent_mo_or_dn="fabric/lan/classes", mtu="9000", priority="silver")
        handle.add_mo(mo, True)

        handle.commit()
    except:
        print("priority silver already exists")
    ####create a jumbo qos policy

    from ucsmsdk.mometa.epqos.EpqosDefinition import EpqosDefinition
    from ucsmsdk.mometa.epqos.EpqosEgress import EpqosEgress

    try:
        mo = EpqosDefinition(parent_mo_or_dn="org-root", name="jumbo")
        mo_1 = EpqosEgress(parent_mo_or_dn=mo, burst="10240", rate="line-rate", name="", prio="silver", host_control="none")
        handle.add_mo(mo)

        handle.commit()
    except:
        print("\n\nPolicy 'jumbo' already exists.\n\n")
    #####create vnic templates. Notes only the default vlan is used, with default network selected. since these are updating templates they can be changed later

    from ucsmsdk.mometa.vnic.VnicLanConnTempl import VnicLanConnTempl
    from ucsmsdk.mometa.vnic.VnicEtherIf import VnicEtherIf

    mo = VnicLanConnTempl(parent_mo_or_dn="org-root", mtu="9000", switch_id="A-B", ident_pool_name=(macp), name=(nicpola_s), qos_policy_name="jumbo", templ_type="updating-template")
    mo_1 = VnicEtherIf(parent_mo_or_dn=mo, name="default", default_net="yes")
    handle.add_mo(mo)

    handle.commit()

    from ucsmsdk.mometa.vnic.VnicLanConnTempl import VnicLanConnTempl
    from ucsmsdk.mometa.vnic.VnicEtherIf import VnicEtherIf

    mo = VnicLanConnTempl(parent_mo_or_dn="org-root", mtu="9000", switch_id="B-A", ident_pool_name=(macp), name=(nicpolb_s), qos_policy_name="jumbo", templ_type="updating-template")
    mo_1 = VnicEtherIf(parent_mo_or_dn=mo, name="default", default_net="yes")
    handle.add_mo(mo)

    handle.commit()

    #use previously created values for vnic templates and push to the target system

    from ucsmsdk.mometa.vnic.VnicLanConnPolicy import VnicLanConnPolicy
    from ucsmsdk.mometa.vnic.VnicEther import VnicEther

    mo = VnicLanConnPolicy(parent_mo_or_dn="org-root", name=(lcp_s))
    mo_1 = VnicEther(parent_mo_or_dn=mo, adaptor_profile_name="Linux", switch_id="A-B", nw_templ_name=(nicpola_s), name=(nicpola_s), order="1")
    mo_2 = VnicEther(parent_mo_or_dn=mo, adaptor_profile_name="Linux", switch_id="B-A", nw_templ_name=(nicpolb_s), name=(nicpolb_s), order="2")
    handle.add_mo(mo)

    handle.commit()
    ## Logout!
    handle.logout()

if __name__=="__main__":

#Enter login info and target system info, dcname and sysid are used in other naming conventions
    from ucsmsdk.ucshandle import UcsHandle
    try:

        ucssys=input("Enter the IP or hostname: ")
        admin=input("Enter Admin user name: ")
        pwd=input("Enter password: ")
        default=int(input("Use defaults? yes=1, no=0: "))
        handle = UcsHandle(ucssys,admin,pwd, port=443)#.format(ucssysf=ucssys,adminf=admin,pwdf=pwd)
        handle.login()
    except:
        print("Can't seem to connect")

    ServerLCP(default,handle)

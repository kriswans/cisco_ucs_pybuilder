###
#Author: kriswans@cisco.com, https://github.com/kriswans/ucs-py-tools
##This program creates a SAN Connectivity Policy and the parameters contained therein. This is for a dual HBA Linux system.
###


def ServerSCP(default,handle):
    try:
        from ucsmsdk.ucshandle import UcsHandle
        import sys
        import shutil
        import SPQuickBuilder

        #Call the function that pulls and updates the wwxn pool values
        SPQuickBuilder.ReadWWxNPoolvalues(default,0,0,0)
        #The selected variables are placed in the wwxn_prod file. They need to be reformatted for the ucsmsdk calls.
        f=open("prod/wwxn_prod",'r')
        flist=f.readlines()
        nm=str(flist[0])
        nm_s=nm.rstrip()
        low=str(flist[1])
        low_s=low.rstrip()
        hi=str(flist[2])
        hi_s=hi.rstrip()
        scp=str(flist[3])
        scp_s=scp.rstrip()
        tmpa=str(flist[4])
        tmpa_s=tmpa.rstrip()
        tmpb=str(flist[5])
        tmpb_s=tmpb.rstrip()
        f.close()
        print(nm+'\n'+low+'\n'+hi+'\n')

        ##continue building the SP builder
        sp_builder=open("tmp/tmp_sp_builder",'a')
        sp_builder.write(scp_s+'\n')
        sp_builder.close()


        from ucsmsdk.mometa.fcpool.FcpoolInitiators import FcpoolInitiators
        from ucsmsdk.mometa.fcpool.FcpoolBlock import FcpoolBlock

        mo = FcpoolInitiators(parent_mo_or_dn="org-root", assignment_order="sequential", purpose="node-and-port-wwn-assignment", name=(nm_s))
        mo_1 = FcpoolBlock(parent_mo_or_dn=mo, r_from=(low_s), to=(hi_s))
        handle.add_mo(mo)

        handle.commit()


        from ucsmsdk.mometa.vnic.VnicSanConnTempl import VnicSanConnTempl
        from ucsmsdk.mometa.vnic.VnicFcIf import VnicFcIf

        mo = VnicSanConnTempl(parent_mo_or_dn="org-root", name=(tmpa_s), templ_type="updating-template")
        mo_1 = VnicFcIf(parent_mo_or_dn=mo, name="default")
        handle.add_mo(mo)

        handle.commit()


        from ucsmsdk.mometa.vnic.VnicSanConnTempl import VnicSanConnTempl
        from ucsmsdk.mometa.vnic.VnicFcIf import VnicFcIf

        mo = VnicSanConnTempl(parent_mo_or_dn="org-root", name=(tmpb_s), switch_id="B", templ_type="updating-template")
        mo_1 = VnicFcIf(parent_mo_or_dn=mo, name="default")
        handle.add_mo(mo)

        handle.commit()


        from ucsmsdk.mometa.vnic.VnicSanConnPolicy import VnicSanConnPolicy
        from ucsmsdk.mometa.vnic.VnicFcNode import VnicFcNode
        from ucsmsdk.mometa.vnic.VnicFc import VnicFc
        from ucsmsdk.mometa.vnic.VnicFcIf import VnicFcIf

        mo = VnicSanConnPolicy(parent_mo_or_dn="org-root", descr="created from SDK", name=(scp_s))
        mo_1 = VnicFcNode(parent_mo_or_dn=mo, addr="pool-derived", ident_pool_name=(nm_s))
        mo_2 = VnicFc(parent_mo_or_dn=mo, order="1", nw_templ_name=(tmpa_s), adaptor_profile_name="Linux", name="A")
        mo_2_1 = VnicFcIf(parent_mo_or_dn=mo_2, name="default")
        mo_3 = VnicFc(parent_mo_or_dn=mo, order="2", nw_templ_name=(tmpb_s), adaptor_profile_name="Linux", name="B")
        mo_3_1 = VnicFcIf(parent_mo_or_dn=mo_3, name="default")
        handle.add_mo(mo)

        handle.commit()
    except:
        print("Check to see that SAN object doesn't already exist.")

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

    ServerSCP(default,handle)

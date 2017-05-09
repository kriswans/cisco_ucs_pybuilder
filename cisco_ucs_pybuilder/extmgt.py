####
#Author: kriswans@cisco.com
#https://github.com/kriswans/ucs-py-tools
###

def ExtMgtPool(default,handle):
    try:
        from ucsmsdk.ucshandle import UcsHandle
        import sys
        import shutil
        import SPQuickBuilder

        #Call the function that pulls and updates the wwxn pool values
        SPQuickBuilder.ReadExtMgtPoolvalues(default)
        #The selected variables are placed in the wwxn_prod file. They need to be reformatted for the ucsmsdk calls.
        f=open("prod/extmgt_prod",'r')
        flist=f.readlines()
        nm=str(flist[0])
        nm_s=nm.rstrip()
        low=str(flist[1])
        low_s=low.rstrip()
        hi=str(flist[2])
        hi_s=hi.rstrip()
        sub=str(flist[3])
        sub_s=sub.rstrip()
        gw=str(flist[4])
        gw_s=gw.rstrip()
        f.close()
        print(nm+'\n'+low+'\n'+hi+'\n')

        ##continue building the SP builder
        sp_builder=open("tmp/tmp_sp_builder",'a')
        sp_builder.write(nm_s+'\n')
        sp_builder.close()


        from ucsmsdk.mometa.ippool.IppoolPool import IppoolPool
        from ucsmsdk.mometa.ippool.IppoolBlock import IppoolBlock

        mo = IppoolPool(parent_mo_or_dn="org-root", assignment_order="sequential", name=(nm_s))
        mo_1 = IppoolBlock(parent_mo_or_dn=mo, r_from=(low_s), to=(hi_s), subnet=(sub_s), def_gw=(gw_s))
        handle.add_mo(mo)

        handle.commit()
    except:
        print("Check whether there is a duplicate Ext Mgt IP Pool")

if __name__=="__main__":
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

    ExtMgtPool(default,handle)

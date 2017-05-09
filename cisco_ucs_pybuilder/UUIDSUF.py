###
#Author: kriswans@cisco.com, https://github.com/kriswans/ucs-py-tools
##This program creates a UUID Suffix Pool and the parameters contained therein.
###


def UUIDsuffix(default,handle):
    try:
        from ucsmsdk.ucshandle import UcsHandle
        import sys
        import shutil
        import SPQuickBuilder

        #Call the function that pulls and updates the mac pool values
        SPQuickBuilder.ReadUUIDPoolvalues(default)
        #The selected variables are placed in the uuid_prod file. They need to be reformatted for the ucsmsdk calls.
        f=open("prod/uuid_prod",'r')
        flist=f.readlines()
        nm=str(flist[0])
        nm_s=nm.rstrip()
        low=str(flist[1])
        low_s=low.rstrip()
        hi=str(flist[2])
        hi_s=hi.rstrip()
        f.close()
        print(nm+'\n'+low+'\n'+hi+'\n')
        #continue building sp builder
        sp_builder=open("tmp/tmp_sp_builder",'a')
        sp_builder.write(nm_s+'\n')
        sp_builder.close()


        from ucsmsdk.mometa.uuidpool.UuidpoolPool import UuidpoolPool
        from ucsmsdk.mometa.uuidpool.UuidpoolBlock import UuidpoolBlock

        mo = UuidpoolPool(parent_mo_or_dn="org-root", assignment_order="sequential", name=(nm_s))
        mo_1 = UuidpoolBlock(parent_mo_or_dn=mo, r_from=(low_s), to=(hi_s))
        handle.add_mo(mo)

        handle.commit()
    except:
        print("Check to see if the UUID Suffix pool already exists.")

if __name__ == "__main__":
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

    UUIDsuffix(default,handle)

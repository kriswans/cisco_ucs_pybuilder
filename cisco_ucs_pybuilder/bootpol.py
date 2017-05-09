####
#Author: kriswans@cisco.com
#https://github.com/kriswans/ucs-py-tools
###


def bootpol_DVDSDLOCAL(handle):
    from ucsmsdk.ucshandle import UcsHandle
    import sys
    import shutil
    import SPQuickBuilder
    try:
        from ucsmsdk.mometa.lsboot.LsbootPolicy import LsbootPolicy
        from ucsmsdk.mometa.lsboot.LsbootVirtualMedia import LsbootVirtualMedia
        from ucsmsdk.mometa.lsboot.LsbootStorage import LsbootStorage
        from ucsmsdk.mometa.lsboot.LsbootLocalStorage import LsbootLocalStorage
        from ucsmsdk.mometa.lsboot.LsbootUsbFlashStorageImage import LsbootUsbFlashStorageImage
        from ucsmsdk.mometa.lsboot.LsbootLocalHddImage import LsbootLocalHddImage
        from ucsmsdk.mometa.lsboot.LsbootLocalLunImagePath import LsbootLocalLunImagePath
        from ucsmsdk.mometa.lsboot.LsbootEmbeddedLocalDiskImage import LsbootEmbeddedLocalDiskImage

        mo = LsbootPolicy(parent_mo_or_dn="org-root", name="DVD-SD-Local")
        mo_1 = LsbootVirtualMedia(parent_mo_or_dn=mo, access="read-only", lun_id="0", order="1")
        mo_2 = LsbootStorage(parent_mo_or_dn=mo, order="4")
        mo_2_1 = LsbootLocalStorage(parent_mo_or_dn=mo_2, )
        mo_2_1_1 = LsbootUsbFlashStorageImage(parent_mo_or_dn=mo_2_1, order="2")
        mo_2_1_2 = LsbootLocalHddImage(parent_mo_or_dn=mo_2_1, order="3")
        mo_2_1_2_1 = LsbootLocalLunImagePath(parent_mo_or_dn=mo_2_1_2, type="primary")
        mo_2_1_3 = LsbootEmbeddedLocalDiskImage(parent_mo_or_dn=mo_2_1, order="4")
        handle.add_mo(mo)

        handle.commit()
    except:
        print("\n\nDVD-SD-Local already exists\n\n")

if __name__ == "__main__":
    from ucsmsdk.ucshandle import UcsHandle
    try:
        ucssys=input("Enter the IP or hostname: ")
        admin=input("Enter Admin user name: ")
        pwd=input("Enter password: ")
        handle = UcsHandle(ucssys,admin,pwd, port=443)#.format(ucssysf=ucssys,adminf=admin,pwdf=pwd)
        handle.login()
    except:
        print("Can't seem to connect")

    bootpol_DVDSDLOCAL(handle)

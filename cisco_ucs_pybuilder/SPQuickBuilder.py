"""
    #SPQuickBuilder.py
    #Author: kriswans@cisco.com
    #This program serves as a reposotory for quick setting for various pools in UCS Manager.
    #It is intended to define several functions that will either allow the admin to select from exisiting ranges or gives the option to default
    #The fucntions will be called from other scripts that build parts of service profiles:
    ## The functions will use conditionals 1/0 to indicate default behavior. Default will not take user input for the sake of speed.
    ###
    ##
    #
"""
"""
    This is meant to serve as a function Library
    for the other pybuilder modules. It is the
    engine that R/W the pertinent text configs.
    In all cases it removes the 'used' pool items
"""

import sys
import shutil
default=0

###
##Function to read/edit MAC pool configuration values from a text file
#
def ReadMacpPoolvalues(default,macp_name,macp_low,macp_hi):
    if default==0:
        try:
            i=1
            mac_idx_list=[]
            print("The following is the list of ranges in the Mac Pool configuration: \n")
            with open("cfg/macp_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    mac_idx_list.append(rows)
                    i+=1
            range_sel=int(input("Which index/range would you like?: " ))
            range_sel=range_sel-1
            splt_me=str(mac_idx_list[range_sel])
            vnic_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk
            macp_name=vnic_in_vars[0]
            macp_low=vnic_in_vars[1]
            macp_hi=vnic_in_vars[2]
            vnpola=vnic_in_vars[3]
            vnpolb=vnic_in_vars[4]
            lcp=vnic_in_vars[5]
            macp_prod=open("prod/macp_prod",'w')
            macp_prod.write(str(macp_name)+'\n')
            macp_prod.write(str(macp_low)+'\n')
            macp_prod.write(str(macp_hi)+'\n')
            macp_prod.write(str(vnpola)+'\n')
            macp_prod.write(str(vnpolb)+'\n')
            macp_prod.write(str(lcp))
            macp_prod.close()
            #Remove the used range from the config
            mac_idx_list.pop(range_sel)
            lmil=len(mac_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(mac_idx_list[j])
                whats_left=open("tmp/tmp_mac","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/macp_cfg_def.txt","cfg/macp_cfg_def.old")
            shutil.copy("tmp/tmp_mac","cfg/macp_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_mac")
        except:
            input("Invalid Input, hit return to continue")
            ReadMacpPoolvalues(0,0,0,0)
    if default==1:
        range_sel=1
        try:
            i=1
            mac_idx_list=[]
            print("The following is the list of ranges in the Mac Pool configuration: \n")
            with open("cfg/macp_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    mac_idx_list.append(rows)
                    i+=1
            range_sel=range_sel-1
            splt_me=str(mac_idx_list[range_sel])
            vnic_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk.File macp_prod is meant to hold the current values and will be overwritten each function call
            macp_name=vnic_in_vars[0]
            macp_low=vnic_in_vars[1]
            macp_hi=vnic_in_vars[2]
            vnpola=vnic_in_vars[3]
            vnpolb=vnic_in_vars[4]
            lcp=vnic_in_vars[5]
            macp_prod=open("prod/macp_prod",'w')
            macp_prod.write(str(macp_name)+'\n')
            macp_prod.write(str(macp_low)+'\n')
            macp_prod.write(str(macp_hi)+'\n')
            macp_prod.write(str(vnpola)+'\n')
            macp_prod.write(str(vnpolb)+'\n')
            macp_prod.write(str(lcp))
            macp_prod.close()
            #Remove the used range from the config
            mac_idx_list.pop(range_sel)
            lmil=len(mac_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(mac_idx_list[j])
                whats_left=open("tmp/tmp_mac","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/macp_cfg_def.txt","cfg/macp_cfg_def.old")
            shutil.copy("tmp/tmp_mac","cfg/macp_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_mac")
        except:
            print("Error")

        ##Function to read/edit WWxN pool configuration values from a text file

def ReadWWxNPoolvalues(default,wwxn_name,wwxn_low,wwxn_hi):
    if default==0:
        try:
            i=1
            wwxn_idx_list=[]
            print("The following is the list of ranges in the WWxN Pool configuration: \n")
            with open("cfg/wwxn_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    wwxn_idx_list.append(rows)
                    i+=1
            range_sel=int(input("Which index/range would you like?: " ))
            range_sel=range_sel-1
            splt_me=str(wwxn_idx_list[range_sel])
            vhba_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk
            wwxnp_name=vhba_in_vars[0]
            wwxnp_low=vhba_in_vars[1]
            wwxnp_hi=vhba_in_vars[2]
            scp_name=vhba_in_vars[3]
            tmpa=vhba_in_vars[4]
            tmpb=vhba_in_vars[5]
            wwxn_prod=open("prod/wwxn_prod",'w')
            wwxn_prod.write(str(wwxnp_name)+'\n')
            wwxn_prod.write(str(wwxnp_low)+'\n')
            wwxn_prod.write(str(wwxnp_hi)+'\n')
            wwxn_prod.write(str(scp_name)+'\n')
            wwxn_prod.write(str(tmpa)+'\n')
            wwxn_prod.write(str(tmpb))
            wwxn_prod.close()
            #Remove the used range from the config
            wwxn_idx_list.pop(range_sel)
            lmil=len(wwxn_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(wwxn_idx_list[j])
                whats_left=open("tmp/tmp_wwxn","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/wwxn_cfg_def.txt","cfg/wwxn_cfg_def.old")
            shutil.copy("tmp/tmp_wwxn","cfg/wwxn_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_wwxn")
        except:
            print("Error in SPQuickBuilder, wwxn")

    if default==1:
        range_sel=1
        try:
            i=1
            wwxn_idx_list=[]
            print("The following is the list of ranges in the WWxN Pool configuration: \n")
            with open("cfg/wwxn_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    wwxn_idx_list.append(rows)
                    i+=1
            range_sel=range_sel-1
            splt_me=str(wwxn_idx_list[range_sel])
            vhba_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk.File wwxn_prod is meant to hold the current values and will be overwritten each function call
            wwxnp_name=vhba_in_vars[0]
            wwxnp_low=vhba_in_vars[1]
            wwxnp_hi=vhba_in_vars[2]
            scp_name=vhba_in_vars[3]
            tmpa=vhba_in_vars[4]
            tmpb=vhba_in_vars[5]
            wwxn_prod=open("prod/wwxn_prod",'w')
            wwxn_prod.write(str(wwxnp_name)+'\n')
            wwxn_prod.write(str(wwxnp_low)+'\n')
            wwxn_prod.write(str(wwxnp_hi)+'\n')
            wwxn_prod.write(str(scp_name)+'\n')
            wwxn_prod.write(str(tmpa)+'\n')
            wwxn_prod.write(str(tmpb))
            wwxn_prod.close()
            #Remove the used range from the config
            wwxn_idx_list.pop(range_sel)
            lmil=len(wwxn_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(wwxn_idx_list[j])
                whats_left=open("tmp/tmp_wwxn","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/wwxn_cfg_def.txt","cfg/wwxn_cfg_def.old")
            shutil.copy("tmp/tmp_wwxn","cfg/wwxn_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_wwxn")
        except:
            print("Error")

## Function to Create UUID Pools

def ReadUUIDPoolvalues(default):
    if default==0:
        try:
            i=1
            uuid_idx_list=[]
            print("The following is the list of ranges in the UUID Suffix configuration: \n")
            with open("cfg/uuid_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    uuid_idx_list.append(rows)
                    i+=1
            range_sel=int(input("Which index/range would you like?: " ))
            range_sel=range_sel-1
            splt_me=str(uuid_idx_list[range_sel])
            uuid_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk
            uuid_name=uuid_in_vars[0]
            uuid_low=uuid_in_vars[1]
            uuid_hi=uuid_in_vars[2]
            uuid_prod=open("prod/uuid_prod",'w')
            uuid_prod.write(str(uuid_name)+'\n')
            uuid_prod.write(str(uuid_low)+'\n')
            uuid_prod.write(str(uuid_hi))
            uuid_prod.close()
            #Remove the used range from the config
            uuid_idx_list.pop(range_sel)
            lmil=len(uuid_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(uuid_idx_list[j])
                whats_left=open("tmp/tmp_uuid","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/uuid_cfg_def.txt","cfg/uuid_cfg_def.old")
            shutil.copy("tmp/tmp_uuid","cfg/uuid_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_uuid")
        except:
            input("Invalid Input, hit return to continue")
            ReadUUIDPoolvalues(0,0,0,0)
    if default==1:
        range_sel=1
        try:
            i=1
            uuid_idx_list=[]
            print("The following is the list of ranges in the UUID Suffix Pool configuration: \n")
            with open("cfg/uuid_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    uuid_idx_list.append(rows)
                    i+=1
            range_sel=range_sel-1
            splt_me=str(uuid_idx_list[range_sel])
            uuid_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk
            uuid_name=uuid_in_vars[0]
            uuid_low=uuid_in_vars[1]
            uuid_hi=uuid_in_vars[2]
            uuid_prod=open("prod/uuid_prod",'w')
            uuid_prod.write(str(uuid_name)+'\n')
            uuid_prod.write(str(uuid_low)+'\n')
            uuid_prod.write(str(uuid_hi))
            uuid_prod.close()
            #Remove the used range from the config
            uuid_idx_list.pop(range_sel)
            lmil=len(uuid_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(uuid_idx_list[j])
                whats_left=open("tmp/tmp_uuid","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/uuid_cfg_def.txt","cfg/uuid_cfg_def.old")
            shutil.copy("tmp/tmp_uuid","cfg/uuid_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_uuid")
        except:
            print("Error")
###

def ReadExtMgtPoolvalues(default):
    if default==0:
        try:
            i=1
            extmgt_idx_list=[]
            print("The following is the list of ranges in the External Mgt IP Pool configuration: \n")
            with open("cfg/extmgt_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    extmgt_idx_list.append(rows)
                    i+=1
            range_sel=int(input("Which index/range would you like?: " ))
            range_sel=range_sel-1
            splt_me=str(extmgt_idx_list[range_sel])
            extmgt_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk
            extmgt_name=extmgt_in_vars[0]
            extmgt_low=extmgt_in_vars[1]
            extmgt_hi=extmgt_in_vars[2]
            extmgt_sub=extmgt_in_vars[3]
            extmgt_gw=extmgt_in_vars[4]
            extmgt_prod=open("prod/extmgt_prod",'w')
            extmgt_prod.write(str(extmgt_name)+'\n')
            extmgt_prod.write(str(extmgt_low)+'\n')
            extmgt_prod.write(str(extmgt_hi)+'\n')
            extmgt_prod.write(str(extmgt_sub)+'\n')
            extmgt_prod.write(str(extmgt_gw)+'\n')
            extmgt_prod.close()
            #Remove the used range from the config
            extmgt_idx_list.pop(range_sel)
            lmil=len(extmgt_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(extmgt_idx_list[j])
                whats_left=open("tmp/tmp_extmgt","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/extmgt_cfg_def.txt","cfg/extmgt_cfg_def.old")
            shutil.copy("tmp/tmp_extmgt","cfg/extmgt_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_extmgt")
        except:
            input("Invalid Input, hit return to continue")
            ReadExtMgtPoolvalues(0,0,0,0)
    if default==1:
        range_sel=1
        try:
            i=1
            extmgt_idx_list=[]
            print("The following is the list of ranges in the External Mgt IP Pool configuration: \n")
            with open("cfg/extmgt_cfg_def.txt", 'r') as ucd :
                for rows in ucd:
                    print("Index# "+str(i)+":\n")
                    print(rows)
                    print('\n')
                    extmgt_idx_list.append(rows)
                    i+=1
            range_sel=range_sel-1
            splt_me=str(extmgt_idx_list[range_sel])
            extmgt_in_vars=splt_me.split()
            #these will be formatted and copied into the variables expected by the ucsm sdk
            extmgt_name=extmgt_in_vars[0]
            extmgt_low=extmgt_in_vars[1]
            extmgt_hi=extmgt_in_vars[2]
            extmgt_sub=extmgt_in_vars[3]
            extmgt_gw=extmgt_in_vars[4]
            extmgt_prod=open("prod/extmgt_prod",'w')
            extmgt_prod.write(str(extmgt_name)+'\n')
            extmgt_prod.write(str(extmgt_low)+'\n')
            extmgt_prod.write(str(extmgt_hi)+'\n')
            extmgt_prod.write(str(extmgt_sub)+'\n')
            extmgt_prod.write(str(extmgt_gw)+'\n')
            extmgt_prod.close()
            #Remove the used range from the config
            extmgt_idx_list.pop(range_sel)
            lmil=len(extmgt_idx_list)
            j=0
            #iterate the lines/ranges that are left and write to a temp file
            while j < lmil:
                newtxt=str(extmgt_idx_list[j])
                whats_left=open("tmp/tmp_extmgt","a")
                whats_left.write(newtxt)
                j+=1
            whats_left.close()
            #backup the default config overwrite the old config file with values that are left, nullify the the temp file
            shutil.copy("cfg/extmgt_cfg_def.txt","cfg/extmgt_cfg_def.old")
            shutil.copy("tmp/tmp_extmgt","cfg/extmgt_cfg_def.txt")
            shutil.copy("tmp/null","tmp/tmp_extmgt")
        except:
            print("Error")

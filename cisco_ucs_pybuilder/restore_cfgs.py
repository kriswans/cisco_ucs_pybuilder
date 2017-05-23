####
#Author: kriswans@cisco.com
#https://github.com/kriswans/ucs-py-tools
###
import sys

def RestoreAllLast():
    import sys
    import shutil
    shutil.copy("cfg/uuid_cfg_def.old","cfg/uuid_cfg_def.txt")
    shutil.copy("cfg/macp_cfg_def.old","cfg/macp_cfg_def.txt")
    shutil.copy("cfg/wwxn_cfg_def.old","cfg/wwxn_cfg_def.txt")
    shutil.copy("cfg/extmgt_cfg_def.old","cfg/extmgt_cfg_def.txt")

def RestoreAllOriginal():
    import sys
    import shutil
    shutil.copy("cfg/uuid_cfg_def_original.txt","cfg/uuid_cfg_def.txt")
    shutil.copy("cfg/macp_cfg_def_original.txt","cfg/macp_cfg_def.txt")
    shutil.copy("cfg/wwxn_cfg_def_original.txt","cfg/wwxn_cfg_def.txt")
    shutil.copy("cfg/extmgt_cfg_def_original.txt","cfg/extmgt_cfg_def.txt")

if __name__ == "__main__":
    try:
        restore=input(str("Enter O to restore ALL the Original 'LOCAL' text configs or L for the Last 'LOCAL' text configs:\n\n: "))
        if restore == "O":
            RestoreAllOriginal()
            print("Success")
        if restore == "L":
            RestoreAllLast()
            print("Success")
        else:
            print("Invalid Input")
            sys.exit()
    except:
        print("Failed Restore")
        sys.exit()

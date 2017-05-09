###
#Author: kriswans@cisco.com, https://github.com/kriswans/ucs-py-tools
#ucs sdk xmlconverter.py lists files in the Windows user's Download,Desktop directories, indexes them for selection and conversion.
#use pip install ucsmsdk to install the ucs python sdk
###
#Step 1: Using UCSM HTML5 interface, CTRL+ALT+Q after selecting top-most pane on the web page. "Record XML" link will appear. Click link when ready.
#Step 2: Perform one or more configuration taks to record. When complete, click "Stop XML Recording" and save the output log ending in 'xmlReq.log' to the Downloads Directory (or one being searched).
#Step 3: Run this program against the saved log file.
###
#
def xmlConverter():
    from ucsmsdk.utils.converttopython import convert_to_ucs_python
    import sys
    import glob
    import os

    # lists all log files in the Downloads directory and indexes them. Grabs input for selection
    try:
        who=os.path.join(os.path.expandvars("%userprofile%"))
        who=os.path.basename(who)
        cwd=(os.getcwd())
        print("Current working directory is: {cwd}\n".format(cwd=cwd))
        print (" Here is a list of files in the Download, Desktop, or User directory, ending in 'xmlReq.log':\n")
        pth1=("/Users/{who}/Downloads/*xmlReq.log".format(who=who))
        pth2=("/Users/{who}/Desktop/*xmlReq.log".format(who=who))
        pth3=("/Users/{who}/*xmlReq.log".format(who=who))
        dirlist=(glob.glob(pth1))+(glob.glob(pth2))+(glob.glob(pth3))
        i=0
        for lines in dirlist:
            print("\nlogfile index: " + str(i) + '\n')
            print (lines)
            i+=1
        lognum=int(input("\n\nEnter xml log file index to convert to Python: "))
        dl=dirlist[lognum]
        ##
        #Grabs input for the output file name. Writes the output of sdk converter to the named file
        ##
        log_path=dl
        orig_stdout = sys.stdout
        outfile=input("\nOutput filename: ")
        pyfile=(outfile)+".py"
        #create the python output file and add some white space to the beginning
        f = open(pyfile, 'w')
        f.write("\n                                                             \n")
        f.write("\n                                                             \n")
        f.write("\n                                                             \n")
        f.write("\n                                                             \n")
        f.write("\n                                                             \n")
        sys.stdout = f
        #dumps the xml to python conversion into the file which is printed via stdout
        convert_to_ucs_python(xml=True, path=log_path)
        sys.stdout = orig_stdout
        f.close()
        f = open(pyfile, 'r+')
        #Gives the option of adding a handler to access a ucsm so that the resulting python file is set to be run against a live system
        syspush=str(input("Would you like to create a python file that will push\n this configuration to another UCS system?  y/n : "))
        try:
            if syspush == "y":
                ucssys=input("Enter the IP or hostname: ")
                admin=input("Enter Admin user name: ")
                pwd=input("Enter password: ")
                f.seek(0) #get to the first position
                f.write("from ucsmsdk.ucshandle import UcsHandle\n")
                f.write('handle = UcsHandle("{ucssysf}","{adminf}","{pwdf}", port=443)\n'.format(ucssysf=ucssys,adminf=admin,pwdf=pwd))
                f.write("handle.login()\n")
                f.close()
                print("File name:")
                print(pyfile)
                print("... has been written.")
        except:
            print("Exiting")
            sys.exit()
    except:
        print("\nInput wasn't accepted. Exiting ...")
        sys.exit()

if __name__ == "__main__":
    xmlConverter()

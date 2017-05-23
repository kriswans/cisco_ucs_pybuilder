# ucs-py-tools
A collection of home-grown programs that use Cisco's UCS Python SDK. 

I'm hoping to build a few Programs over the next several weeks that may be of some use to Cisco customers looking to use the UCSM Python SDK.

I'm currently using the UCS Platform Emulator, Python 3.6, and the 'atom' IDE running on Windows. 

Mileage may vary where OS calls are needed against other systems.


UCS PE can be obtained here: https://communities.cisco.com/docs/DOC-37827


Info on the UCS Python SDK can be found here: https://communities.cisco.com/docs/DOC-64378

The "prod" and "tmp" folders need to exist but the contents are auto-created during runtime. The files contain the temporary variables selected/created during the running of the script.

The "cfg" folder holds the ranges of values that will feed various UCS pool configurations. 

Features exist for the creation of individual Lan Connectivity Policies, SAN Connectivity Policies, UUID Suffix Pools, and IP Pools.

A seature exists for creating service profile templates by first creating the requisite Lan Connectivity Policies, SAN Connectivity Policies, UUID Suffix Pools, IP Pools, and Boot Bolicy (only a single boot policy exists right now). Upon creation of the SP template a bulk creation of SPs occur. Post SP creation an XMPP client sends a message from a defined source to a defined destination. An echo client then listens to report the last created SP event as a reply to any text recieved.

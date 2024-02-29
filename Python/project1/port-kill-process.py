# script that kills a process according to the port
# or returns that there is no process in that port

#need to use standard library, inherent library of python
# we need to use lsof in linux
# which shows processes and files using ports or sockets
# lsof -n -i4TCP these switches: no host name(-n) (i4)(ivp4)
# make sure nginx is running and is showing in the ports of lsof command!
# then we want to do it on server in port 5000, so we create a server
# so we do in bash : python3 -m http.server 5000 &   <<<< we use "&" to create a process to tun in the background!
# make sure again in lson -n -i4TCP  don't forget sudo!

# we use parser because its a script running with arguments
import subprocess # this allows me to use linux bash commands!
import os
from argparse import ArgumentParser



parser = ArgumentParser(description='kill the running processes listening on a given port')
parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_args().port
port_name = parser.parse_args().port_name
try:
    net_result = subprocess.run(
        ["sudo", "netstat", "-tanup", "|", "grep %s " % port],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    result = subprocess.run( # this didn't work too good
        ['lsof', '-n', 'i4TCP:%s' % port],  # we create it as a list/array not as a whole string/argument
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
 # print (net_result) # this was to check what comes out of this parsing process

except subprocess.CalledProcessError:
    print(f"No process listening on port {port}")
else:
    listening = None

    for line in net_result.stdout.splitlines(): #()[1] <<means what column
        if "LISTEN" in str(line):
            listening = line # listening is the process and port now, with all columns
            break
    if listening:
        pid_temp = str(listening.split()[6]) # the process id we need is in column 6
        pid_pr = pid_temp.split("b'")[1] # we don't know what b' came from
        pid = int(pid_pr.split("/")[0]) # make it a number and not a string so we can kill the process via number
        #pid = int(listening.split()[1]) # process id [1] is column
        os.kill(pid, 9) # kill is built in python, 9 is forcefully
        print(f"Killed process {pid}")
    else:
        print(f"No process listening port {port}")

# we use python for this and not bash, because sometimes in windows there is no powershell that can support
# these libraries, so we use python which is common both to linux and windows

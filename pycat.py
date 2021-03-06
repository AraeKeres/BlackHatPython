import sys
import socket
import getopt
import threading
import subprocess

# Global Variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print "Netcat replacement from BHP"
    print
    print "Usage: pycat.py -t target_host -p port"
    print "-l --listen  -listen on [host]:[port] for incoming connection"
    print "-e --execute=file_to_run - execute the given file upon receiving a connection"
    print "-c --command - initialize a command shell"
    print "-u --upload=destination - upon receiving conneciton upload a file and write to [destination]"
    print
    print "Examples: "
    print "pycat.py -t 192.168.0.1 -p 5555 -l -c"
    print "pycat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "pycat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./pycat.py -t 192.168.0.1 -p 5555"
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu",
                                   ["help", "listen", "execute", "target",
                                    "port", "command", "upload"])

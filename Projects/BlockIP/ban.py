import argparse
import os
from ipaddress import ip_network, ip_address

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    IP Blocker
    
    Examples:
    ------------------------
    ban -a 69.69.69.69
    ban -1 69.69.69.69/24
    
    """)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", metavar="<IP Address>")
    parser.print_help()

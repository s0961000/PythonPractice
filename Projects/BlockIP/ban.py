import argparse
import os
from ipaddress import ip_network, ip_address


def is_ip(raw_ip):
    # check ip is legitimate
    try:
        # convert to IP Object
        ip_net = ip_network(raw_ip)
    except ValueError as e:
        print(f"Error Converting {raw_ip} to IP Address.")
        exit()
    return ip_net


def is_important_ip(ip_obj):
    try:
        with open("important_ips.txt", "r") as lines:
            for line in lines:
                ip_net = is_ip(line.strip())
                if ip_obj in ip_net:
                    return True
            return False
    except FileNotFoundError:
        print("Important IP File Not Found. Exiting.")
        exit()
    return


def in_list(ip_obj):
    try:
        with open("blocked_ips.txt", "r") as lines:
            for line in lines:
                if str(ip_obj) == line.strip():
                    return True
            return False
    except FileNotFoundError:
        print("blocked_ips.txt Not Found. Exiting")
        exit()


def add_ip(raw_ip):
    results = []
    ip_net = is_ip(raw_ip)
    try:
        with open("blocked_ips.txt", "a") as blocked_ips:
            for ip_obj in ip_net:
                # Check if private
                if ip_obj.is_private:
                    results.append(f"{ip_obj} is a Private IP and was not added.")
                # Check if important
                elif is_important_ip(ip_obj):
                    results.append(f"{ip_obj} in an Important IP and was not added.")
                # Check if in list already
                elif in_list(ip_obj):
                    results.append(f"{ip_obj} already blocked and was not added.")
                # Add IP
                else:
                    blocked_ips.write(f"{str(ip_obj)}\n")
                    results.append(f"{ip_obj} was added!")
    except Exception as e:
        print("Error Reading blocked_ips.txt")
        exit()
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    IP Blocker
    
    Examples:
    ------------------------
    ban -a 69.69.69.69
    ban -1 69.69.69.69/24
    
    """)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", help="Add IP Address to Blocklist", metavar="<IP Address>")
    args = parser.parse_args()

    # Handling User Input
    if args.add:
        output = add_ip(args.add)
        for value in output:
            print(value)
        with open("output.txt", "w") as output_file:
            for value in output:
                output_file.write(f"{value}\n")

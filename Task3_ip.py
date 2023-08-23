import re
import subprocess

def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)\d{1,3}$'
    return re.match(pattern, ip)

def is_pingable(ip):
    
    result = subprocess.run(['ping', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        return True
    else:
        return False

 


def write_pinging_ips_to_file(pinging_ips):
    with open("Pinging_IPs.txt", "a") as file:
        file.write("\n")
        for ip in pinging_ips:
            file.write(ip + '\n')

def main():
    valid_ips = []
    pinging_ips = []
    invalid_ips = []

    while True:
        ip = input("Enter an IP address: ")
        if is_valid_ip(ip):
            if is_pingable(ip):
                pinging_ips.append(ip)
                valid_ips.append(ip)
                print("IP is pinging. Added to valid and pinging IPs.")
                with open("valid_ip.txt", "a") as file:
                 file.write(ip + '\n')
            else:
                invalid_ips.append(ip)
                valid_ips.append(ip)

                print("IP is not pinging. Added to valid IPs.")
                with open("valid_ip.txt", "a") as file:
                 file.write(ip + '\n')
                with open("non_pinging.txt", "a") as file:
                 file.write(ip + '\n')
        else:
            print("Invalid IP address format. Please enter a valid IP.")
        
        response = input("Do you want to continue? (Yes/No): ").lower()
        if response == "no":
            if pinging_ips:
                write_pinging_ips_to_file(pinging_ips)
                print("Pinging IPs have been written to 'Pinging_IPs.txt'.")
            else:
                print("No pinging IPs to write.")
            break
        elif response != "yes":
            print("Invalid response. Please enter 'Yes' or 'No'.")

if __name__ == "__main__":
    main()

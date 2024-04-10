import socket
import time

def send_udp_packets(ip, port, duration):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_to_send = b'X' * 1200  # 1200 bytes packet size
        start_time = time.time()
        packets_sent = 0
        while (time.time() - start_time) < duration:
            sock.sendto(bytes_to_send, (ip, port))
            packets_sent += 1
            print(f"Sent {packets_sent} UDP packets", end='\r')
            time.sleep(0.01)  # Delay to control the rate of packet sending
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    print("Starting UDP packet sender...")

    ip = input("Enter the IP address of the target: ")
    port = int(input("Enter the port number of the target: "))
    duration = int(input("Enter the duration to send UDP packets (in seconds): "))
    
    send_udp_packets(ip, port, duration)
    print("\nUDP packet sending completed.")

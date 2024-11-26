import os
import sys
import random
import json
import tarfile
import re
from datetime import datetime, timedelta
from scapy.all import *

def create_ctf_pcap(output_file, flag, num_dummy_packets=0):
    packets = []
    time = datetime(2002, 9, 20, 13, 27, 0)
  
    # Convert flag to binary
    binary_flag = ''.join(format(ord(c), '08b') for c in flag)
    print(binary_flag)
    print(len(binary_flag))
    
    packet_counter = 0
    flag_bit_index = 0
    
    pkt = IP(src=f"192.168.1.{random.randint(1,254)}", dst=f"10.0.0.{random.randint(1,254)}")/\
          UDP(sport=random.randint(1024,65535), dport=random.randint(1,65535))/\
          Raw(load=os.urandom(64))
    pkt.time = time.timestamp();

    packets.append(pkt)
  
    while ((packet_counter < num_dummy_packets) or (packet_counter < len(binary_flag))):
        pkt = IP(src=f"192.168.1.{random.randint(1,254)}", dst=f"10.0.0.{random.randint(1,254)}")/\
              UDP(sport=random.randint(1024,65535), dport=random.randint(1,65535))/\
              Raw(load=os.urandom(64))

        if flag_bit_index < len(binary_flag):
            interval_ms = 20 if binary_flag[flag_bit_index] == '1' else 5
            flag_bit_index += 1
        else:
            interval_ms = random.uniform(10, 50)
        
        time = (time + timedelta(milliseconds=interval_ms))
        pkt.time = (time).timestamp()
        
        packets.append(pkt)
        packet_counter += 1
  
    wrpcap(output_file, packets)
    with tarfile.open("/challenge/artifacts.tar.gz", "w:gz") as tar:
        tar.add(output_file)
  
    return packets, binary_flag

def main():
  
  try:
    
    # Craft flag ==========================================================
    flag = os.environ.get("FLAG")
    
    if flag == "":
      print("Flag was not read from environment. Aborting.")
      sys.exit(2)
    else:
      # Get hash part
      flag_rand = re.search("{.*}$", flag)
      if flag_rand == None:
        print("Flag isn't wrapped by curly braces. Aborting.")
        sys.exit(3)
      else:
        flag_rand = flag_rand.group()
        flag_rand = flag_rand[1:-1]
        flag_rand = flag_rand.zfill(8)
    
    flag = "picoCTF{t1m3_" + flag_rand + "}"
    packets, binary_representation = create_ctf_pcap("traffic.pcap", flag, num_dummy_packets=0)
    # =====================================================================
    
    # Create and update metadata.json =====================================
    metadata = {}
    metadata['flag'] = str(flag)
    json_metadata = json.dumps(metadata)
    
    with open("/challenge/metadata.json", "w") as f:
      f.write(json_metadata)
    # =====================================================================
  
  except subprocess.CalledProcessError:
    print("A subprocess got an error")
    sys.exit(1)

if __name__ == "__main__":
  main()

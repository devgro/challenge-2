# Scanner

- Namespace: picoctf/18739f24
- ID: Timer
- Type: custom
- Category: Forensics
- Points: 1
- Templatable: no
- MaxUsers: 0

## Description

You are trying to find a secret code being transmitted across a network. You 
were able to gain access to the network and pick up some traffic that was 
being sent across it. Find the flag hidden in the capture.

Download the flag {{url_for("traffic.pcap", "here")}}.

## Details

## Hints

- Download the file and open it in wireshark or scapy to examine it
- Look at all the different fields of the packets
- The data and headers aren't the only information in the packet...
- Long is 1, short is 0

## Solution Overview

Download `traffic.pcap`, open it in Wireshark or scapy, and try to find the hidden flag.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Learn to look through wireshark traces and find necessary information.

## Attributes

- author: Devan Grover
- organization: CMU
- event: 18749 CTF

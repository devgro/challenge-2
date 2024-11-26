# Scanner

This is a forensics challenge meant to test the attacker's knowledge of packets,
networking, and packet dissection. The challenge consists of a program that 
generates a new wireshark capture on each build based on the cmgr flag env
variable.

## Pre-requisites

1. You have `Wireshark` or `Scapy` installed.

## Overview

When approaching the problem, the user will be greeted with a bunch of packets
that seem to have random information in them. The information in the packets
is actually completely random, the data isn't stored there. The data is encoded
in binary, but it is stored in the intervals between the packets. Each two 
packets have an interval of either 20ms or 5ms between them. If the interval is
20ms, then the user will record a 1, and if its 5ms the user will record a 0.
Once they have put this binary together, it can be converted to ASCII to 
get the flag.

### File Listing

  1. [Dockerfile] builds the container used for the challenge.
  2. [problem.md] specifies the name of the problem, the description, and other 
     metadata about the problem
  3. [requirements.txt] installs the required packages for python
  4. [setup-challenge.py] Generates the required capture and sets the flag

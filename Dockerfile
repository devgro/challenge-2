# References base image by SHA to avoid drift. This is Ubuntu 24.04. You will
# probably want to update the hash when working on a new challenge.
FROM ubuntu:20.04 AS base

# Install python3
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip


# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && \
    chmod 700 /challenge

# * Copy capture and setup script to the image
COPY setup-challenge.py /app/
COPY requirements.txt /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
# RUN tar czvf /challenge/artifacts.tar.gz traffic.pcap

FROM base AS challenge
ARG FLAG

RUN python3 setup-challenge.py

#
# This is a dummy command that keeps the container running. cmgr will keep
# restarting the container if it exits.
CMD ["tail", "-f", "/dev/null"]

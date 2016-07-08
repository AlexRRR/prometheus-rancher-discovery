FROM debian:jessie
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \
    && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y python3-urllib3 \
    && rm -Rf /var/lib/apt /var/cache/apt
COPY prom-rancher-sd.py /
RUN chmod +x /prom-rancher-sd.py
VOLUME /prom-rancher-sd-data
CMD ["/prom-rancher-sd.py"]

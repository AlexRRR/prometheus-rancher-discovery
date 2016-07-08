#!/usr/bin/python3.4

# Copyright 2016 Daniel Dent (https://www.danieldent.com/)

import time
import urllib.parse
import urllib.request
import json

API_URL = 'http://rancher-metadata.rancher.internal/2015-12-19/containers'


def get_current_services():
    headers = {
        'User-Agent': "prom-rancher-sd/0.1",
        'Accept': 'application/json'
    }
    req = urllib.request.Request(API_URL, headers=headers)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf8 '))


def is_monitored_service(service):
    return 'labels' in service and 'prometheus.port' in service['labels']


def monitoring_config(service):
    targets = [service['primary_ip'] + ':' +
               service['labels']['prometheus.port']]
    labels = {
        'name': service['name'],
        'service_name': service['service_name'],
        'stack_name': service['stack_name']
    }
    if 'alert.group' in service['labels']:
        labels['alert_group'] = service['labels']['alert.group']
    return {
        "targets": targets,
        "labels": labels
    }


def get_monitoring_config():
    return list(
        map(monitoring_config,
            filter(is_monitored_service, get_current_services())))


if __name__ == '__main__':
    while True:
        with open('/prom-rancher-sd-data/rancher.json', 'w') as config_file:
            json.dump(get_monitoring_config(), config_file, indent=2)
            config_file.write('\n\n')
        time.sleep(30)

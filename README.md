# Prometheus-Rancher Service Discovery Bridge

This utility is a fork of https://github.com/DanielDent/prom-rancher-sd

prom-rancher-sd polls [Rancher's metadata service](http://docs.rancher.com/rancher/metadata-service/) and looks for containers with the `prometheus.port` label. 

A configuration file suitable for use by [Prometheus](http://prometheus.io/) is written to enable services to be monitored automatically. Prometheus will scrape `/metrics` via HTTP by connecting to the container's primary IP on the port specified by the `prometheus.port` label.`

## Prometheus configuration

Prometheus must be configure to read the generated files via `file_sd_configs` 

```
- job_name: 'rancher-discovery'
  file_sd_configs:
  - files:
    - /prom-rancher-sd-data/rancher.json
````

## Alert groups

The label `alert.group` might be added to the service, the value of is set as a prometheus label for the service, and is useful for routing alerts to specific groups using alertmanager.

## Testing

Test with the unittest discovery: 

```python -m unittest discovery```


## License

Copyright 2016 Alejandro Ramirez

Licensed under the Apache License, Version 2.0 (the "License");
you may not use these files except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Third-party contents included in builds of the image are licensed separately.

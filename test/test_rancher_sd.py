import unittest
import sys
import os
from unittest.mock import MagicMock

# append module root directory to sys.path
sys.path.append('../')

import prom_rancher_sd


class DiscoveryTests(unittest.TestCase):
    """Tests for `prom-rancher-sd.py`"""
    def setUp(self):
        self.rancher_response = [{
                'primary_ip': "127.0.0.1",
                'name': 'test_name',
                'service_name': 'test_service_name',
                'stack_name': 'test_stack_name',
                'labels': {
                    'prometheus.port': '8080'
                }
        }]
        self.expected_result = [{
            'targets': ['127.0.0.1:8080'],
            'labels': {
                'name': 'test_name',
                'service_name': 'test_service_name',
                'stack_name': 'test_stack_name'
            }
        }]
        prom_rancher_sd.get_current_services = MagicMock(
            return_value=self.rancher_response)

    def test_target_no_alerts(self):
        """target has no alert.group defined"""
        self.assertEqual(prom_rancher_sd.get_monitoring_config(),
                         self.expected_result)

    def test_target_w_alerts(self):
        """target has alert.group label defined"""
        self.rancher_response[0]['labels']['alert.group'] = 'ops'
        self.expected_result[0]['labels']['alert_group'] = 'ops'
        self.assertEqual(prom_rancher_sd.get_monitoring_config(),
                         self.expected_result)

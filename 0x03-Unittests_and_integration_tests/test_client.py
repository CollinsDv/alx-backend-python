#!/usr/bin/env python3
"""
usage: client.GithubOrgClient class
"""
import unittest
import unittest.mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """testing GithubOrgClient class"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org_name, get_json_mock):
        """tests org method
        """
        get_json_mock.return_value = {
            "payload": True
        }
        GithubOrgClient(org_name).org

        get_json_mock.assert_called_once()

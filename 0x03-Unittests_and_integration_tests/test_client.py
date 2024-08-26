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

    """
    memoize turns methods into properties(mock.PropertyMock).

    Implement the test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url.

    Use patch as a context manager to patch GithubOrgClient.org and
        make it return a known payload.

    Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
    """
    def test_public_repos_url(self):
        """tests GithubOrgClient._public_repos_url"""
        with unittest.mock.patch("client.GithubOrgClient.org",
                                 new_callable=unittest.mock.PropertyMock
                                 ) as mock_org:
            mock_org.return_value = {"repos_url": True}

            assert GithubOrgClient('Google')._public_repos_url

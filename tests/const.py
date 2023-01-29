"""Constants for integration_blueprint tests."""
from custom_components.npm_switches.const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_NPM_URL,
)

# Mock config data to be used across multiple tests
MOCK_CONFIG = {
    CONF_USERNAME: "test_username",
    CONF_PASSWORD: "test_password",
    CONF_NPM_URL: "http://test:81",
}

MOCK_NPM_URL = "http://test:81"

MOCK_TOKEN = {
    "token": "abcd12345",
    "expires": "2023-01-25T01:37:00.107Z",
}

MOCK_PROXY_HOSTS_LIST = [
    {
        "id": 33,
        "created_on": "2022-11-27T22:46:21.000Z",
        "modified_on": "2022-12-11T22:48:53.000Z",
        "owner_user_id": 1,
        "domain_names": ["my.domain.com"],
        "forward_host": "192.168.1.1",
        "forward_port": 8123,
        "access_list_id": 0,
        "certificate_id": 35,
        "ssl_forced": 0,
        "caching_enabled": 0,
        "block_exploits": 0,
        "advanced_config": "",
        "meta": {
            "letsencrypt_agree": False,
            "dns_challenge": False,
            "nginx_online": True,
            "nginx_err": None,
        },
        "allow_websocket_upgrade": 0,
        "http2_support": 0,
        "forward_scheme": "https",
        "enabled": 1,
        "locations": [],
        "hsts_enabled": 0,
        "hsts_subdomains": 0,
    },
    {
        "id": 32,
        "created_on": "2022-11-17T00:49:25.000Z",
        "modified_on": "2023-01-24T00:36:53.000Z",
        "owner_user_id": 1,
        "domain_names": ["other.domain.com"],
        "forward_host": "192.168.1.2",
        "forward_port": 8080,
        "access_list_id": 0,
        "certificate_id": 35,
        "ssl_forced": 0,
        "caching_enabled": 0,
        "block_exploits": 1,
        "advanced_config": "",
        "meta": {
            "letsencrypt_agree": False,
            "dns_challenge": False,
            "nginx_online": True,
            "nginx_err": None,
        },
        "allow_websocket_upgrade": 1,
        "http2_support": 0,
        "forward_scheme": "http",
        "enabled": 0,
        "locations": [],
        "hsts_enabled": 0,
        "hsts_subdomains": 0,
    },
]

MOCK_PROXY_HOSTS_DICT = {
    "33": {
        "id": 33,
        "created_on": "2022-11-27T22:46:21.000Z",
        "modified_on": "2022-12-11T22:48:53.000Z",
        "owner_user_id": 1,
        "domain_names": ["my.domain.com"],
        "forward_host": "192.168.1.1",
        "forward_port": 8123,
        "access_list_id": 0,
        "certificate_id": 35,
        "ssl_forced": 0,
        "caching_enabled": 0,
        "block_exploits": 0,
        "advanced_config": "",
        "meta": {
            "letsencrypt_agree": False,
            "dns_challenge": False,
            "nginx_online": True,
            "nginx_err": None,
        },
        "allow_websocket_upgrade": 0,
        "http2_support": 0,
        "forward_scheme": "https",
        "enabled": 1,
        "locations": [],
        "hsts_enabled": 0,
        "hsts_subdomains": 0,
    },
    "32": {
        "id": 32,
        "created_on": "2022-11-17T00:49:25.000Z",
        "modified_on": "2023-01-24T00:36:53.000Z",
        "owner_user_id": 1,
        "domain_names": ["other.domain.com"],
        "forward_host": "192.168.1.2",
        "forward_port": 8080,
        "access_list_id": 0,
        "certificate_id": 35,
        "ssl_forced": 0,
        "caching_enabled": 0,
        "block_exploits": 1,
        "advanced_config": "",
        "meta": {
            "letsencrypt_agree": False,
            "dns_challenge": False,
            "nginx_online": True,
            "nginx_err": None,
        },
        "allow_websocket_upgrade": 1,
        "http2_support": 0,
        "forward_scheme": "http",
        "enabled": 0,
        "locations": [],
        "hsts_enabled": 0,
        "hsts_subdomains": 0,
    },
}

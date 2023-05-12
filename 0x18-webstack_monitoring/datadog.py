#!/usr/bin/python3
""" Get information about your live hosts in Datadog."""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.datadoghq.com/api/v1/hosts"
    api_key = sys.argv[1]
    app_key = sys.argv[2]
    payload = {'api_key': api_key, 'application_key': app_key}
    r = requests.get(url, params=payload)
    print(r)
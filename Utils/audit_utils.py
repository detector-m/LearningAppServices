#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :audit_utils.py
@说明        :
@时间        :2020/07/21 16:38:22
@作者        :Riven
@版本        :1.0.0
'''

import base64, logging, socket, sys

sys.path.append('..')
from Utils.collection_utils import get_first_existing
from Utils.tornado_utils import get_proxied_ip

HOSTNAME = 'hostname'
IP = 'ip'
PROXIED_USERNAME = 'proxied_username'
PROXIED_IP = 'proxied_ip'
PROXIED_HOSTNAME = 'proxied_hostname'
AUTH_USERNAME = 'auth_username'

LOGGER = logging.getLogger('script_server.audit_utils')

def get_all_audit_names(request_handler):
    result = {}

    auth_username = request_handler.application.identification.identify_for_audit(request_handler)
    if auth_username:
        result[AUTH_USERNAME] = auth_username

    basic_auth_username = find_basic_auth_username(request_handler)
    if basic_auth_username:
        result[PROXIED_USERNAME] = basic_auth_username

    proxied_ip = get_proxied_ip(request_handler)
    if proxied_ip:
        result[proxied_ip] = proxied_ip

        proxied_hostname = _resolve_hostname(proxied_ip)
        if proxied_hostname:
            result[PROXIED_HOSTNAME] = proxied_hostname

    remote_ip = request_handler.request.remote_ip
    result[IP] = remote_ip

    hostname = _resolve_hostname(remote_ip)
    if hostname:
        result[HOSTNAME] = hostname

    return result

def _resolve_hostname(ip):
    try:
        (hostname, _, _) = socket.gethostbyaddr(ip)
        return hostname
    except:
        LOGGER.warning('Could not get hostname for' + ip)
        return None

def get_audit_name(all_audit_names):
    audit_types = [AUTH_USERNAME, PROXIED_USERNAME, PROXIED_HOSTNAME, PROXIED_IP, HOSTNAME, IP]

    for name_type in audit_types:
        name = all_audit_names.get(name_type)

        if name:
            return name
    
    return None

def get_audit_name_from_request(request_handler):
    audit_names = get_all_audit_names(request_handler)

    return get_audit_name(audit_names)

def find_basic_auth_username(request_handler):
    auth_header = request_handler.request.headers.get('Authorization')
    if (auth_header is None) or (not auth_header.lower().startswith('basic')):
        return None

    encoding = sys.getdefaultencoding()
    credential_bytes = base64.b64decode(auth_header[6:])
    credentials = credential_bytes.decode(encoding)
    username = credentials.split(':')[0]

    return username

def get_audit_username(all_audit_names):
    return get_first_existing(all_audit_names, AUTH_USERNAME, PROXIED_USERNAME)

if __name__ == '__main__':
    print(__file__)
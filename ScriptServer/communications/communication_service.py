#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :communication_service.py
@说明        :
@时间        :2020/07/21 10:23:25
@作者        :Riven
@版本        :1.0.0
'''

import logging
import threading

_THREAD_PREFIX = 'CommunicationThread-'

LOGGER = logging.getLogger('script_server.communication_service')

class CommunicationsService:
    def __init__(self, destinations) -> None:
        self._destionations = destinations

    def send(self, title, body, files=None):
        if not self._destionations:
            return

        def _send():
            for destination in self._destionations:
                try:
                    destination.send(title, body, files)
                except:
                    LOGGER.exception('Cound not send message to ' + str(destination))
        
        thread = threading.Thread(target=_send, name=_THREAD_PREFIX + title)
        thread.start()
    
    @staticmethod
    def _wait():
        for thread in threading.enumerate():
            if thread.name.startswith(_THREAD_PREFIX):
                thread.join
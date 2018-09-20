"""
This module is used to connect APIs of SWORDFISH.
"""

import json
import sys
import httplib
import warnings
import requests,os
from SWORDFISH_API import SWORDFISH_API
from robot.api import logger

warnings.filterwarnings('ignore')

class Connection(object):
    '''Base class for all SWORDFISH library files'''
    __instance = None

    def __new__(cls):

        if Connection.__instance is None:
            Connection.__instance = object.__new__(cls)

        return Connection.__instance

    def connect(self, rest_ip_addr, auth_token=''):
        '''
        Creates a rest session to SWORDFISH.
        '''
        self.rest_ip_addr = rest_ip_addr
        self.token = auth_token
        self.geturl = SWORDFISH_API(self.rest_ip_addr)
        req = requests.Session()
        req.verify = False
        req.headers = {"Content-Type": "application/json",}
        self.IS_SECURE = "false"
        sessiontoken = "Token " + self.token
        headers = {"Authorization": sessiontoken }
        req.headers.update(headers)
        self.req = req

    def _form_body(self,kwargs):
        """
        Method for forming body parameters
        - **parameters**, **types**, **return** and **return types**::
            :param args: All required and optional parameters list for SWORDFISH keyword
            :param kwargs: User defined parameters
            :type args: list
            :type kwargs: dict
        """
        body = {}
        for key in kwargs:
            body[key] = kwargs[key]
        return body

    def search(self, data, fkey, skey=None):
        '''searches the json data with the keys and display respective values.
        - **parameters**, **types**, **return** and **return types**::
                :param data : json data
                :param fkey : first key to be searched
                :param skey : second key to be searched
                :type data: dict
                :type fkey: string
                :type skey: string
                :return fout: returns list of values associated with fkey
                :return outdict: returns dictionary of values associated with fkey and skey
                :rtype fout: list
                :rtype outdict: dict
        '''
        data = data['Response']
        fout = []
        sout = []
        for item in data:
            if isinstance(item, dict):
                fout.append(item[fkey])
                if skey:
                    sout.append(item[skey])
            else:
                return ("No key with that input")
        if not skey:
            if len(fout) == 1:
                logger.info(fout[0])
                return fout[0]
            else:
                logger.info(fout)

#!/usr/bin/python
''' Module for SWORDFISH create operations '''
from Connection import Connection
from robot.api import logger
import json
import requests
import time

class SWORDFISH_Setup(Connection):
    """
    SWORDFISHsetup Class for setup commands
    """

    def create_chassis(self, **kwargs):
        """
        Create Chassis.
        - **parameters**, **types**, **return** and **return types**::
            :param name(req): name of a chassis
            :param orgid(req): id of an chassis
            :param secret_key(req): secret key of an chassis
            :param email(req): email of an chassis
            :param contact_person(req): name of contact person
            :param secret_key_end_time(req): secret key end time of an chassis(ex: yyyy-mm-dd time)
            :param location(req): location of an chassis
            :type all_params: string
            
            :return : status code.
        """
        
        body = self._form_body(kwargs)
        logger.info(body)
        url = self.geturl.chassis()
        resp = self.req.post(url, json=body)
        logger.info(resp.json())
        output={}
        output['status_code']=resp.status_code
        output['json_resp']=resp.json()
        return output


#!/usr/bin/python
''' Module for SWORDFISH delete/Teardown operations '''
from Connection import Connection
from robot.api import logger
import json
import requests
import time

class SWORDFISH_Delete(Connection):
    """
    Hitachi setup Class for setup commands
    """
    def delete_chassis(self, Id):
        """
        Delete organization.
        - **parameters**, **types**, **return** and **return types**::
            :parm Id: Id of the Chassis
            :type Id: string
            
            :return : status code.
        """
        url = self.geturl.chassis_id(Id)
        logger.info("deleting Chassis : %s" %Id)
        resp = self.req.delete(url)
        logger.info(resp.json())
        response = int(resp.text)
        logger.info("Delete Chassis Response is: %d" %response)
        return response

    

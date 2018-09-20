''' Module for SWORDFISH modify operations '''
from Connection import Connection
from robot.api import logger
import json
import requests

class SWORDFISH_Modify(Connection):
    """
    SWORDFISH modifications keywords
    """

    def update_chassis(self,name,**kwargs):
        """
            Updates organization details.

            - **parameters**, **types**, **return** and **return types**::

                :param name(req): name of the organization
                :orgid(opt): new organization id
                :secret_key(opt): new oraganization secret_key
                :email(opt): new organization mail
                :contact_person(opt): new organization contact person
                :secret_key_end_time(opt): new secret key end time
                :location(opt): new organization location
                :param type(all): string
                :return : response code and organization details
                
        """ 
        #kwargs['Name']=name
        body =self._form_body(kwargs)
        url =self.geturl.chassis_id(name)
        logger.info("URL is: %s" %url)
        resp =self.req.patch(url,json=body)
        logger.info("Updating Chassis details %s" %name)
        logger.info(resp.json())
        output={}
        output['status_code']=resp.status_code
        output['json_resp']=resp.json()
        return output
		
    
    

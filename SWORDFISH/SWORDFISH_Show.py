''' Module for SWORDFISH show operations '''
from Connection import Connection
import requests
import pprint
from robot.api import logger

class SWORDFISH_Show(Connection):
    '''
    SSOCH show operations to get the information.
    '''
    def get_chassis(self, Id):
        """
        Getting all Chassis information.
        - **parameters**, **types**, **return** and **return types**::
            :parm Id: Chassis Id
            
            :return : status code.
        """
        url = self.geturl.chassis_id(Id)
        resp = self.req.get(url)
        logger.info(resp.json())
        output={}
        output['status_code']=resp.status_code
        output['json_resp']=resp.json()
        return output

    def get_task_response(self, task_id):
        """
        Getting task response information.
        - **parameters**, **types**, **return** and **return types**::
            :param task_id: task id
            :type task_id: string
            
            :return : status code.
        """
        url = self.geturl.task_response(str(task_id))
        resp = self.req.get(url)
        resp_dic={}
        resp_dic['status_code']=resp.status_code
        if type(resp.json()) == dict:
            if 'status' in resp.json().keys():
                resp_dic['json_resp']=resp.json()['status']
                resp_dic['Response']=resp.json()['Response']
            else:
                resp_dic = resp.json()
        else:
            if 'INPROGRESS' in resp.json():
                d1 = {}
                d1['status'] = 'INPROGRESS'
                resp_dic['json_resp']=d1
        return resp_dic 

   
    def findvalue_dic(self,dic1,key):
        """
        Finds the value of a key from nested dictionary
         - **parameters**, **types**, **return** and **return types**::
            :param dic1: provide dictionary.
            :type dic1: dictionary
            :param key: provide key to find the value of it from dic1
            :type key: string
            
            :return :value of key.
        """
        for k,value in dic1.iteritems():
            if k==key:
                global value
                break
            elif isinstance(value,dict):
                self.findvalue_dic(value,key)
        return value
        
    def con_uni_to_str(self, uni_val):
        """
        """
        str_val = uni_val.encode('ascii')
        return str_val
    

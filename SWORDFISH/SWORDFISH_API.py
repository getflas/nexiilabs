"""
This module is used to form SWORDFISH URL using APIs
"""
class SWORDFISH_API():
    """
    This class is a global class for generating urls required for SWORDFISH
    """
    rest_ip_addr = None
    port = None
    base_url = None
    object_url = None
    service_url = None

    def __init__(self, rest_ip_addr):
        """
            Generates base url required for SWORDFISH Rest.

            - **parameters**, **types**, **return** and **return types**::

                :param rest_ip_addr: I P address of the rest server where rest api is installed
                :type rest_ip_addr: string
        """
        self.rest_ip_addr = rest_ip_addr
        self.base_url = "http://" + \
            self.rest_ip_addr + \
            "/redfish/v1/"

    def chassis(self):
        """
        Generates url for getting Chassis information
            - **parameters**, **types**, **return** and **return types**::
                :None
                
                :return url: rest url for Chassis
                :return type: string
        """
        url = self.base_url + "Chassis"
        return url

    def chassis_id(self, chassis_id):
        """
        Generates url for getting specific chassis information
            - **parameters**, **types**, **return** and **return types**::
                :param chassis_id: id of a chassis
                :typr chassis_id: string
              
                :return url: rest url for chassis
                :return type: string
        """
        url = self.chassis() + "/" + chassis_id
        return url

"""
Main Library for all SWORDFISH keywords.
"""


from SWORDFISH_Setup import SWORDFISH_Setup
from SWORDFISH_Delete import SWORDFISH_Delete
from SWORDFISH_Show import SWORDFISH_Show
from SWORDFISH_Modify import SWORDFISH_Modify


class SWORDFISH(SWORDFISH_Setup, SWORDFISH_Show, SWORDFISH_Delete,SWORDFISH_Modify):
    """
    Class for SWORDFISH Library which inherits SWORDFISH_Setup,SWORDFISH_Delete,SWORDFISH_Show and
    SWORDFISH_Modify classes and its methods
    """

    def __init__(self):
        """Constructor"""
        pass

    

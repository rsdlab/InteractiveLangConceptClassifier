#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file SeedNoid_Mobile_idl_example.py
 @brief Python example implementations generated from SeedNoid_Mobile.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import RTC, RTC__POA



class LifterPoseInterface_i (RTC__POA.LifterPoseInterface):
    """
    @class LifterPoseInterface_i
    Example class implementing IDL interface RTC.LifterPoseInterface
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # LIFTER_STATE checkState()
    def checkState(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # LIFTER_STATE setLifterTime(in double MoveTime)
    def setLifterTime(self, MoveTime):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_VALUE sendLifterAngle(in LifterAngle targetLifterAngle)
    def sendLifterAngle(self, targetLifterAngle):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_VALUE sendLifterPose(in Point3D targetLifterPose)
    def sendLifterPose(self, targetLifterPose):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_VALUE getLifterAngle(out LifterAngle currentLifterAngle)
    def getLifterAngle(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result, currentLifterAngle

    # RETURN_VALUE getLifterPose(out Point3D currentLifterPose)
    def getLifterPose(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result, currentLifterPose



class TargetPositionInterface_i (RTC__POA.TargetPositionInterface):
    """
    @class TargetPositionInterface_i
    Example class implementing IDL interface RTC.TargetPositionInterface
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # TARGETPOSITION_STATE checkState()
    def checkState(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # TARGETPOSITION_STATE checkArrived()
    def checkArrived(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_VALUE setPositionParam(in Pose2D targetPose)
    def setPositionParam(self, targetPose):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_VALUE moveStart()
    def moveStart(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_VALUE moveStop()
    def moveStop(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = LifterPoseInterface_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print(orb.object_to_string(objref))

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()


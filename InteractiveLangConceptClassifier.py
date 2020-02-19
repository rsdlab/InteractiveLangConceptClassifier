#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file InteractiveLangConceptClassifier.py
 @brief InteractiveLangConceptClassifier
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import SpeechManage_idl
import InteractiveManage_idl
import ActionManage_idl
import SeedNoid_Mobile_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from SpeechManage_idl_example import *
from InteractiveManage_idl_example import *

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import Manage, Manage__POA
import Action, Action__POA
import RTC, RTC__POA

from collections import namedtuple


# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
interactivelangconceptclassifier_spec = ["implementation_id", "InteractiveLangConceptClassifier",
		 "type_name",         "InteractiveLangConceptClassifier",
		 "description",       "InteractiveLangConceptClassifier",
		 "version",           "1.0.0",
		 "vendor",            "hiroyasu",
		 "category",          "Category",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class InteractiveLangConceptClassifier
# @brief InteractiveLangConceptClassifier
#
#
class InteractiveLangConceptClassifier(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_stringdata = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._stringoutOut = OpenRTM_aist.OutPort("stringout", self._d_stringdata)

		"""
		"""
		self._speechmanagePort = OpenRTM_aist.CorbaPort("speechmanage")
		"""
		"""
		self._actionmanagePort = OpenRTM_aist.CorbaPort("actionmanage")
		"""
		"""
		self._interactivemanagePort = OpenRTM_aist.CorbaPort("interactivemanage")
		"""
		"""
		self._LiftermanagePort = OpenRTM_aist.CorbaPort("Liftermanage")

		"""
		"""
		self._SpeechManageProvider = SpeechManage_i()
		"""
		"""
		self._InteractiveManageProvider = InteractiveManage_i()


		"""
		"""
		self._ActionManageRequire = OpenRTM_aist.CorbaConsumer(interfaceType=Action.ActionManage)
		"""
		"""
		self._lifterRequired = OpenRTM_aist.CorbaConsumer(interfaceType=RTC.LifterPoseInterface)

                self.targetPose = OpenRTM_aist.instantiateDataType(RTC.Point3D)
                
		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable

		# Set InPort buffers

		# Set OutPort buffers
		self.addOutPort("stringout",self._stringoutOut)

		# Set service provider to Ports
		self._speechmanagePort.registerProvider("SpeechManage", "Manage::SpeechManage", self._SpeechManageProvider)
		self._interactivemanagePort.registerProvider("InteractiveManage", "Manage::InteractiveManage", self._InteractiveManageProvider)

		# Set service consumers to Ports
		self._actionmanagePort.registerConsumer("ActionManage", "Action::ActionManage", self._ActionManageRequire)
		self._LiftermanagePort.registerConsumer("lifter", "RTC::LifterPoseInterface", self._lifterRequired)

		# Set CORBA Service Ports
		self.addPort(self._speechmanagePort)
		self.addPort(self._actionmanagePort)
		self.addPort(self._interactivemanagePort)
		self.addPort(self._LiftermanagePort)

                self.ProductFlag = 0
                self.PositionFlag = 0
                self.ActionFlag = 0

                #self.Point3D = namedtuple('Point3D', 'x y z')
                #self.targetPose = self.Point3D(1, 2, 3)

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The activated action (Active state entry action)
	# former rtc_active_entry()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK

	##
	#
	# The deactivated action (Active state exit action)
	# former rtc_active_exit()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
                errorID = 0
                if self._SpeechManageProvider.Flag == 1 and self._InteractiveManageProvider.Flag == 1:
                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("1") == self._SpeechManageProvider.textconcept.index("0"):
                                        self.ProductFlag = 1
                                        errorID = 4
                        except :
                                errorID = errorID - 1

                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("1") == self._SpeechManageProvider.textconcept.index("1"):
                                        self.ProductFlag = 2
                                        errorID = 4
                        except :
                                errorID = errorID - 1
                                        
                        try :        
                                if self._InteractiveManageProvider.interactionconcept.index("1") == self._SpeechManageProvider.textconcept.index("2"):
                                        self.ProductFlag = 3
                                        errorID = 4
                        except :
                                errorID = errorID - 1
                                
                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("1") == self._SpeechManageProvider.textconcept.index("3"):
                                        self.ProductFlag = 4
                                        errorID = 4
                        except :
                                errorID = errorID - 1

                        if errorID < 1 and self.PositionFlag > 0 and self.ActionFlag > 0 and self.ProductFlag == 0:
                                print("No Object Word")
                                self._d_stringdata.data = "何を対象にしますか"
		                self._stringoutOut.write()
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                return RTC.RTC_OK

                        errorID = 0

                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("2") == self._SpeechManageProvider.textconcept.index("0"):
                                        self.PositionFlag = 2
                                        errorID = 7
                        except :
                                errorID = errorID - 1

                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("2") == self._SpeechManageProvider.textconcept.index("1"):
                                        self.PositionFlag = 2
                                        errorID = 7
                        except :
                                errorID = errorID - 1

                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("2") == self._SpeechManageProvider.textconcept.index("2"):
                                        self.PositionFlag = 2
                                        errorID = 7
                        except :
                                errorID = errorID - 1

                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("2") == self._SpeechManageProvider.textconcept.index("3"):
                                        self.PositionFlag = 2
                                        errorID = 7
                        except :
                                errorID = errorID - 1

                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("2") == self._SpeechManageProvider.textconcept.index("4"):
                                        self.PositionFlag = 1
                                        errorID = 7
                        except :
                                errorID = errorID - 1

                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("2") == self._SpeechManageProvider.textconcept.index("5"):
                                        self.PositionFlag = 2
                                        errorID = 7
                        except :
                                errorID = errorID - 1
                        
                        try :
                                if self._InteractiveManageProvider.interactionconcept.index("2") == self._SpeechManageProvider.textconcept.index("6"):
                                        self.PositionFlag = 3
                                        errorID = 7
                        except :
                                errorID = errorID - 1
                                
                        if errorID < 1 and self.ProductFlag > 0 and self.ActionFlag > 0 and self.PositionFlag == 0:
                                print("No Position Word")
                                self._d_stringdata.data = "どこにしますか"
		                self._stringoutOut.write()
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                return RTC.RTC_OK

                        errorID = 0                                
                                
                        try :
                                if "7" in self._SpeechManageProvider.textconcept:
                                        self.ActionFlag = 1
                                        errorID = 2
                        except :
                                errorID = errorID - 1

                        try :
                                if "8" in self._SpeechManageProvider.textconcept:
                                        self.ActionFlag = 2
                                        errorID = 2
                        except :
                                errorID = errorID - 1
                                
                        if errorID < 1 and self.ProductFlag > 0 and self.PositionFlag > 0 and self.ActionFlag == 0:
                                print("No Action Word")
                                self._d_stringdata.data = "何をしますか"
		                self._stringoutOut.write()
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                return RTC.RTC_OK

                        if (self.ProductFlag == 1 and self.PositionFlag == 1 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ペットボトル　上　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("petaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdpet")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 1 and self.PositionFlag == 1 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ペットボトル　上　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("petaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 1 and self.PositionFlag == 2 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ペットボトル　中　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("petaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdpet")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0

                        if (self.ProductFlag == 1 and self.PositionFlag == 2 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ペットボトル　中　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("petaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 1 and self.PositionFlag == 3 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ペットボトル　下　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("petaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdpet")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 1 and self.PositionFlag == 3 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ペットボトル　下　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdpet")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("petaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdpetaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0

                        if (self.ProductFlag == 2 and self.PositionFlag == 1 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" おにぎり　上　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("oniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdoni")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 2 and self.PositionFlag == 1 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" おにぎり　上　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("oniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 2 and self.PositionFlag == 2 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" おにぎり　中　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("oniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdoni")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0

                        if (self.ProductFlag == 2 and self.PositionFlag == 2 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" おにぎり　中　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("oniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 2 and self.PositionFlag == 3 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" おにぎり　下　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("oniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdoni")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 2 and self.PositionFlag == 3 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" おにぎり　下　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdoni")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("oniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdoniaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0

                        if (self.ProductFlag == 3 and self.PositionFlag == 1 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" サンドイッチ　上　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("sandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdsand")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 3 and self.PositionFlag == 1 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" サンドイッチ　上　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("sandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 3 and self.PositionFlag == 2 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" サンドイッチ　中　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("sandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdsand")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0

                        if (self.ProductFlag == 3 and self.PositionFlag == 2 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" サンドイッチ　中　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("sandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 3 and self.PositionFlag == 3 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" サンドイッチ　下　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("sandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholdsand")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 3 and self.PositionFlag == 3 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" サンドイッチ　下　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holdsand")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("sandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholdsandaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                        if (self.ProductFlag == 4 and self.PositionFlag == 1 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ドリンク　上　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("drinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholddrink")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 4 and self.PositionFlag == 1 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.50
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ドリンク　上　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("drinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 4 and self.PositionFlag == 2 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ドリンク　中　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("drinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholddrink")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0

                        if (self.ProductFlag == 4 and self.PositionFlag == 2 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.30
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ドリンク　中　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("drinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 4 and self.PositionFlag == 3 and self.ActionFlag == 1):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ドリンク　下　把持 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homenohold")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("drinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homeholddrink")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
                                
                        if (self.ProductFlag == 4 and self.PositionFlag == 3 and self.ActionFlag == 2):
                                """LifterMoveTime = 5000
                                if self._lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
                                        print( "Set Lifter Time" )
	                                self.targetPose.x = 0.0
	                                self.targetPose.z = 0.10
	                                if self._lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
                                                print( "Failure" )
                                time.sleep(LifterMoveTime/1000)
                                """
                                print(" ドリンク　下　設置 ")
                                ut = time.time()
                                print(int(ut*100000))
                                """self._ActionManageRequire._ptr().read("homeholddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("holddrink")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("drinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("noholddrinkaction")
                                time.sleep(3)
                                self._ActionManageRequire._ptr().read("homenohold")
                                """
                                self._SpeechManageProvider.Flag = 0
                                self._InteractiveManageProvider.Flag = 0
                                self.ProductFlag = 0
                                self.PositionFlag = 0
                                self.ActionFlag = 0
	
		return RTC.RTC_OK
        
        #def LifterMover(self, movement):
        #        LifterMoveTime = 5000
        #        if m_lifterRequired._ptr().setLifterTime(LifterMoveTime) == RTC.LIFTER_SET_PARAM_OK:
        #                print( "Set Lifter Time" )
	#                self.targetPose.x = 0.0
	#                self.targetPose.z = movement
	#                if m_lifterRequired._ptr().sendLifterPose(self.targetPose) != RTC.RETURN_MOVE_OK:
        #                        print( "Failure" )
        #        time.sleep(LifterMoveTime/1000)

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK


def InteractiveLangConceptClassifierInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=interactivelangconceptclassifier_spec)
    manager.registerFactory(profile,
                            InteractiveLangConceptClassifier,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    InteractiveLangConceptClassifierInit(manager)

    # Create a component
    comp = manager.createComponent("InteractiveLangConceptClassifier")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()


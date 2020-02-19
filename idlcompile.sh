#!/bin/sh
IDL_PATH=`rtm-config --rtm-idldir`
omniidl -bpython -I$IDL_PATH idl/SpeechManage.idl idl/InteractiveManage.idl idl/ActionManage.idl idl/SeedNoid_Mobile.idl idl/BasicDataType.idl idl/ExtendedDataTypes.idl 
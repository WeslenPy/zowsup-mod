import os,sys
sys.path.append(os.getcwd())

# coding=UTF-8
import logging

from yowsup.stacks import YowStackBuilder
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from app.yowbot_layer import SendLayer
from conf.constants import SysVar
from yowsup.common.tools import WATools
from axolotl.util.keyhelper import KeyHelper
from yowsup.profile.profile import YowProfile
from proto import wsend_pb2
from common.utils import Utils
from app.bot_env import BotEnv
from app.device_env import DeviceEnv
from app.network_env import NetworkEnv
from app.yowbot_values import YowBotType
from app.param_not_enough_exception import ParamsNotEnoughException
from yowsup.structs import ProtocolEntity

import os,time,threading,uuid,json,inspect,time,socks

from yowsup.registration.existsrequest import WAExistsRequest

from yowsup.config.v1.config import Config

config = Config(
    phone="5521920240014",
    cc="55",
    mcc="000",
    mnc="000",
    sim_mnc="000",
    sim_mcc="000"
)

config.id="5521920240014"

# Utils.init_log(logging.DEBUG)    

SysVar.loadConfig()  

botId = "5521920240014"
path ="C://account/"
profile = YowProfile(path+botId)   
env = BotEnv(deviceEnv=DeviceEnv("android"),networkEnv=NetworkEnv("direct"))

wa = WAExistsRequest(config=profile,env=env)
print("\n")
print(wa.sendGetRequest())
"""
"""

import os
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
today_log_file_name = "~%s.log" % datetime.date.today().strftime("%Y%m%d")
#logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("-HMI Backend-")
logger.setLevel(logging.INFO)

log_info_dir = os.path.join(current_dir, "../../my_heap") # absdir
if not os.path.exists(log_info_dir):
    os.makedirs(log_info_dir)
log_path = os.path.join(log_info_dir, today_log_file_name)
handler = logging.FileHandler(log_path, mode="a")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
handler_filter = logging.Filterer()
handler_filter.filter = lambda record: True if record.msg.startswith("[WebSocket]") else False
handler.addFilter(filter=handler_filter)
logger.addHandler(handler)


handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

logger.addHandler(handler)


path = os.path.join(current_dir, "../../my_heap/rotating.log")
print("path: %s" % path)
handler = RotatingFileHandler(filename=path, maxBytes=1<<20, backupCount=2)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

path = os.path.join(current_dir, "../../my_heap/timeRotating.log")
#handler = TimedRotatingFileHandler(filename=path, interval=)
# TODO use config to set logger
a = "unicode"
b = {"a": 1, "b": "kkkk"}
logger.info("[WebSocket] asd")
logger.warn("asfasf")
logger.warn("%s" % a)
logger.warn("%s" % str(b))

try:
    1/0
except:
    logger.error("failed to excute division zero", exc_info = True)
print("---end---")



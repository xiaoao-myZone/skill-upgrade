import os
import logging
import datetime

today_log_file_name = "~%s.txt" % datetime.date.today().strftime("%Y%m%d")
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("-HMI Backend-")
log_info_dir = "/home/log_collection/backend" # absdir
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
# TODO use config to set logger
#logger.info("asd")

# mention your custom log
import sys
import os
import logging

#whenever you log the info
#it will save the timestamp
#what kind of log
#4m where you run the code
# finally the message

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")

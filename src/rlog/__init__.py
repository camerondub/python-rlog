import os
import logging
import logging.handlers

from decouple import config

# file paths
log_dir = config("LOG_DIR", default="/tmp")
os.makedirs(log_dir, exist_ok=True)
log_label = config("LOG_LABEL", default="reo")
log_base = "/".join([log_dir, log_label])
log_file = ".".join([log_base, ".log"])
err_file = ".".join([log_base, ".err"])

# formatter
formatter = logging.Formatter("%(asctime)s %(levelname)s [%(filename)s.%(funcName)s]: %(message)s")

# normal log file
logfile_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=104857600, backupCount=9
)
logfile_handler.setLevel(logging.DEBUG)
logfile_handler.setFormatter(formatter)

# err log file
errfile_handler = logging.handlers.RotatingFileHandler(
    err_file, maxBytes=104857600, backupCount=9
)
errfile_handler.setLevel(logging.WARNING)
errfile_handler.setFormatter(formatter)

# console log stream
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# register handlers
logging.getLogger().addHandler(console)
logging.getLogger().addHandler(logfile_handler)
logging.getLogger().addHandler(errfile_handler)
logging.getLogger().setLevel(logging.DEBUG)

# log methods
debug = logging.debug
info = logging.info
warning = logging.warning
error = logging.error
critical = logging.critical

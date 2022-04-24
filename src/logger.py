import logging
import os

logging.basicConfig(
    filename=format(os.getcwd()) + "\\robo.log",
    format="%(asctime)s | %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger("logger")

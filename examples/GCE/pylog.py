# sudo apt update
# sudo apt install -y python3 python3-dev python3-venv
# sudo apt-get -y install wget
# wget https://bootstrap.pypa.io/get-pip.py
# sudo python3 get-pip.py
# pip install google-cloud-logging


import google.cloud.logging

client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()

import logging
text = "Hello, world!"
logging.warning(text)
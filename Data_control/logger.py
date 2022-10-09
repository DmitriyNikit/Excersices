import logging

logs = logging.getLogger('GeneralLogger')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(fmt='%(levelname)-8s %(message)s'))
logs.addHandler(handler)
logs.setLevel(logging.INFO)

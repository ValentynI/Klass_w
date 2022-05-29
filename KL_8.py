import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='logs_example.log',
                    filemode='w',
                    format='NEW LOG - %(asctime)s - %(levelname)s: %(message)s')
logging.debug('debug example')
logging.info('info example')
logging.warning('warning example')
logging.error('error example')
logging.critical('critical example')
try:
    print(abeme)
except BaseException as error:
    logging.critical(type(error).__name__ + ": " + str(error))
try:
    print(10/0)
except Exception as e:
    logging.exception(e)
import logging
import sys, os
import traceback
logging.basicConfig(level=logging.DEBUG,
                    filename='logs_example.log',
                    filemode='w',
                    format='NEW LOG - %(asctime)s - %(levelname)s: %(message)s')
logging.debug('debug example')
logging.info('info example')
logging.warning('warning example')
logging.error('error example')
logging.critical('critical example')


def abeme(args):
    pass


try:
    print(abeme)
except BaseException as error:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logging.critical(type(error).__name__ + ": " + str(error) + '::' + repr(traceback.format_tb(exc_tb)))
try:
    print(10/0)
except Exception as e:
    logging.exception(e)
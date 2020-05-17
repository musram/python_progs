import logging





if __name__ == "__main__":

    #can declare basicConfig only once in a file

    
    #logging.basicConfig(level=logging.DEBUG)
    #logging.debug('This will get logged')


    #logging to file
    #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    #logging.warning('This will get logged')

    #logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
    #logging.warning('This is a Warning')    

    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('Admin logged out')


    #logging variable data

    name = "Sai"
    logging.error('{} raised the error'.format(name))

    #capturing the stack trace

    a = 5
    b = 0
    try:
        c = a/b
    except Exception as e:
        #logging.error("Exception occurred", exc_info=True)
        logging.exception("Exception occurred") # with .exception  exc_info is default set to True
        #logging.critical("Exception occurred", exc_true=True) # with .criticla or other than exception set  exc_info  to True

    #create custom logger handlers

    logger = logging.getLogger(__name__)

    #create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('file.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.warning('This is a warning')
    logger.error('This is an error')



    #loading logging params from file
    import logging.config

    logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

    # Get the logger specified in the file
    logger = logging.getLogger(__name__)



    logger.debug('This is a debug message')


    #logging using yaml files

    import logging.config
    import yaml

    with open('config.yaml', 'r') as f:
         config = yaml.safe_load(f.read())
         logging.config.dictConfig(config)

    logger = logging.getLogger(__name__)

    logger.debug('This is a debug message')
    

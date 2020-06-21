#https://martinheinz.dev/blog/24

import logging

if __name__ == "__main__":
    
    logging.basicConfig(
        filename='application.log',
        level=logging.WARNING,
        format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )




    logging.error("Some serious error occurred.")
    logging.warning('Function you are using is deprecated.')


    import yaml
    from logging import config

    with open("config.yaml", 'rt') as f:
        config_data = yaml.safe_load(f.read())
        config.dictConfig(config_data)


    logger =  logging.getLogger(__name__)

    logger.debug('This is a debug messge')


    """
    __repr__ for more readable logs

    """


    """
    __missing__ for dictionaries

    """

    class MyDict(dict):
        def __missing__(self, key):
            message = f'{key} not present in the dictionary!'
            logging.warning(message)
            return message  # Or raise some error instead
    
    d = MyDict(a=1, b=1)
    print(d['a'])
    print(d['z'])


    """
    Running the application with-i argument (python3 -i app.py) causes it to start interactive shell as soon as the program exits. At that point you can inspect variables and functions.

If that's not good enough, you can bring a bigger hammer - pdb - Python Debugger. pdb has quite a few features which would warrant an article on its own. But here is example and a rundown of the most important bits

    """
    SOME_VAR = 42

    class SomeError(Exception):
        pass

    def func():
        raise SomeError("Something went wrong...")

    func()


    

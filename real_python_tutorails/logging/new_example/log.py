import yaml
import  logging.config


if __name__ == "__main__":
    
    with open("config.yaml", 'rt') as f:
        config_data = yaml.safe_load(f.read())
        logging.config.dictConfig(config_data)

    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message')


    

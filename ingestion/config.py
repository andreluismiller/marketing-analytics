import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def load_config():
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)
    
def get_target_db_config(config):
    target_config = config['target']
    return {
        'host': target_config['host'],
        'port': target_config['port'],
        'database': target_config['database'],
        'user': target_config['user'],
        'password': os.getenv('TARGET_DB_PASSWORD')
    }
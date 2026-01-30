import asyncpg
from ingestion.config import load_config

async def create_target_pool(target_config):
    """Cria pool de conexão para o banco de destino"""
    return await asyncpg.create_pool(
        host=target_config['host'],
        port=target_config['port'],
        database=target_config['database'],
        user=target_config['user'],
        password=target_config['password'],
        min_size=3,
        max_size=10
    )
from datetime import datetime
from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis = RedisRepository(redis_conn)

# redis.insert('Eu sou', 'legal')
# value = redis.get('Eu sou')

# redis.insert_hash("meu_hash", "campo_1", "Este e meu valor")
# value = redis.get_hash("meu_hash", "campo_1")

data_atual = datetime.now()
data_atual = data_atual.strftime('%Y-%m-%d')

redis.insert_hash_ex(data_atual, "banana", 3.12, 10)
redis.insert_hash(data_atual, "morango", 5.12)
redis.insert_hash(data_atual, "uva", 4.12)
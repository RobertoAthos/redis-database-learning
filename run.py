from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis = RedisRepository(redis_conn)

redis.insert('Eu sou', 'legal')
value = redis.get('Eu sou')

redis.insert_hash("meu_hash", "campo_1", "Este e meu valor")
value = redis.get_hash("meu_hash", "campo_1")

print(value)

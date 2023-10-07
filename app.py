import redis

""" Basic redis commands """

redis = redis.Redis(host='localhost', port=6379, db=0, password='redis!')

# Chave valor
redis.set('chave_1', 'outro_valor')
valor = redis.get('chave_1').decode('utf-8')
redis.delete("chave_1")


# Hash -> return and set the value of the key by the hash name
redis.hset("meu_hash", "nome", "Roberto")
redis.hset("meu_hash", "idade", 18)
redis.hset("meu_hash", "cidade", "Porto Seguro")
redis.hdel("meu_hash", "idade")

nome = redis.hget('meu_hash', 'nome').decode('utf-8')
print(nome)


# Exist
is_chave_1 = redis.exists("chave_1")
hash_key = redis.exists("meu_hash")
field_key = redis.hexists("meu_hash","nome")

print(is_chave_1)
print(hash_key)
print(field_key)

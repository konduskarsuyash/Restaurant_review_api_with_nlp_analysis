import redis
from django.conf import settings

# Initialize Redis connection
redis_client = redis.StrictRedis.from_url(settings.CACHES['default']['LOCATION'])

class Leaderboard:
    def __init__(self, name):
        self.name = name

    def add_score(self, entity_id, score):
        redis_client.zadd(self.name, {entity_id: score})
       

    def remove_entity(self, entity_id):
        redis_client.zrem(self.name, entity_id)
       

    def get_top_entities(self, num=10):
        top_entities = redis_client.zrevrange(self.name, 0, num - 1, withscores=True)
        return top_entities

    def get_rank(self, entity_id):
        rank = redis_client.zrevrank(self.name, entity_id)
        return rank

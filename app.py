from flask import Flask, request, jsonify
import redis
import time
import os

app = Flask(__name__)
redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST","localhost"), port=6379, db=0)

def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr

def is_rate_limited(ip, endpoint, limit):
    current_time = int(time.time())
    key = f"{ip}:{endpoint}"
    request_count = redis_client.get(key)

    if request_count is None:
        redis_client.set(key, 1, ex=10)
        return False
    elif int(request_count) < limit:
        redis_client.incr(key)
        return False
    else:
        return True

@app.route('/<endpoint>', methods=['GET'])
def rate_limited_endpoint(endpoint):
    ip = get_client_ip()
    limit = int(os.getenv('RATE_LIMIT',5))

    if is_rate_limited(ip, endpoint, limit):
        return jsonify({"message": "Rate limit exceeded"}), 429
    return jsonify({"message": "Request successful"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

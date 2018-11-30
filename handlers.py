import wikipedia
def index(**kwargs):
    request = kwargs.get('request')
    query = json.loads(request)
    totalsum = sum(query.values())
    return {"Sum of all numbers": totalsum}

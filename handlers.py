import wikipedia


def index(**kwargs):
    request = kwargs.get('request')
    if 'query' in request:
        query = request.get('query')
        try:
            summary = wikipedia.summary(query, auto_suggest=False, redirect=False)
        except Exception as e:
            print('ERROR:', e)
            summary = "No exact match found for {}".format(query)
        finally:
            return {"summary": summary}
    else:
        return {"error": "Must pass the 'query' parameter"}

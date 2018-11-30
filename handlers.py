from os import environ


def index(**kwargs):
    request = kwargs.get('request')
    totalsum = sum(request.values())
    return {"summary": totalsum}
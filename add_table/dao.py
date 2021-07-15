from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()


def bank_get2():
    res = es.search(index="bank", body={"query": { "match": { "bank": "국민은행" }}, "size": 0, "aggs": { "b_1": {"terms": { "field": "customers"}}}})
    datas = res['aggregations']['b_1']['buckets']

    datas = json.dumps(datas, ensure_ascii=False) 

    return datas


if __name__== "__main__":
    bank_get2()

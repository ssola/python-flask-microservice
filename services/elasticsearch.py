from elasticsearch import Elasticsearch


class ElasticSearchFactory(object):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def create(self) -> Elasticsearch:
        return Elasticsearch(
            [{'host': self.host, 'port': self.port}]
        )


class ElasticSearchIndex(object):
    def __init__(
            self,
            elastic_factory: ElasticSearchFactory,
            index_name: str,
            doc_type: str,
            index_mapper: dict
    ):
        """
        It creates the index if it doesn't exists

        :param elasticsearch:
        :param index_name:
        :param doc_type:
        :param index_mapper:
        """
        self.index_name = index_name
        self.index_mapper = index_mapper
        self.doc_type = doc_type
        self.elastic_factory = elastic_factory
        self.instance = None

    def connection(self) -> Elasticsearch:
        if not self.instance:
            self.instance = self.elastic_factory.create()

            if not self.instance.indices.exists(self.index_name):
                self.instance.indices.create(
                    index=self.index_name,
                    body=self.index_mapper
                )

        return self.instance

    def index(self, payload: dict) -> bool:
        return self.connection().index(
            index=self.index_name,
            doc_type=self.doc_type,
            body=payload
        )

    def exists_by_url(self, url: str) -> bool:
        matches = self.connection().search(
            index=self.index_name,
            doc_type=self.doc_type,
            body={
                "query": {
                    "query_string": {
                        "query": 'url:"{}"'.format(url)
                    }
                }
            }
        )

        hits = matches['hits']['hits']

        if hits:
            return True

        return False

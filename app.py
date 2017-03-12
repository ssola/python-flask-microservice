import os
import connexion

from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from services.elasticsearch import ElasticSearchIndex, ElasticSearchFactory


def configure(binder: Binder) -> Binder:
    binder.bind(
        ElasticSearchIndex,
        ElasticSearchIndex(
            ElasticSearchFactory(
                os.environ['ELASTICSEARCH_HOST'],
                os.environ['ELASTICSEARCH_PORT'],
            ),
            'rooms_index',
            'room',
            {}
        )
    )

    return binder


if __name__ == '__main__':
    app = connexion.App(__name__, 9090, specification_dir='swagger/')
    app.add_api('indexer.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()

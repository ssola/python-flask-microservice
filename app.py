import connexion

from decouple import config
from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from conf.elasticsearch_mapper import room_mapping
from services.elasticsearch import ElasticSearchIndex, ElasticSearchFactory


def configure(binder: Binder) -> Binder:
    binder.bind(
        ElasticSearchIndex,
        ElasticSearchIndex(
            ElasticSearchFactory(
                config('ELASTICSEARCH_HOST'),
                config('ELASTICSEARCH_PORT'),
            ), 'rooms', 'room', room_mapping))

    return binder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('indexer.yaml', resolver=RestyResolver('api'))

    FlaskInjector(app=app.app, modules=[configure])

    app.run(port=9090)
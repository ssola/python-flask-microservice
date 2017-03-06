import connexion

from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver

from services.provider import ItemsProvider


def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name": "Test 1"}])
    )

    return binder


if __name__ == '__main__':
    app = connexion.App(__name__, 9090, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()
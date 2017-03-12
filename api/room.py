from flask_injector import inject

from services.elasticsearch import ElasticSearchIndex


class Room(object):
    @inject(indexer=ElasticSearchIndex)
    def post(self, indexer: ElasticSearchIndex, room) -> dict:
        """
        This wil return a location, kind of 'Camden, London'.
        We need to have some data like lat/lon for that input.
        """
        indexer.index({})

        return room

class_instance = Room()

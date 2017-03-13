room_mapping = {
    "settings": {
        "number_of_shards": 3,
        "number_of_replicas": 2
    },
    "room": {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "description": { "type": "string"},
            "price": { "type": "integer"},
            "recurrency": { "type": "keyword"},
            "provider": { "type": "keyword"},
            "url": { "type": "keyword"},
            "monthly_price": { "type": "integer"},
            "property_size": {"type": "keyword"},
            "is_visible": {"type": "keyword"},
            "coordinates": {"type": "geo_point"},
            "area": {
                "id": { "type": "string"},
                "name": { "type": "keyword"},
                "coordinates": { "type": "geo_point"},
                "country": { "type": "keyword"},
                "city": {"type": "keyword"}
            },
            "images": [{
                "url": { "type": "string"}
            }]
        }
    }
}

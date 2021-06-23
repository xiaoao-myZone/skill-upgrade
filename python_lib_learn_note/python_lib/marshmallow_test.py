from marshmallow import Schema, fields

from datetime import date
from pprint import pprint



class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

# bowie = dict(name="David Bowie")
# album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))
# pprint(album)
# schema = AlbumSchema()
# result,error = schema.dump(album)
# print("type of result is %s" %type(result))
# pprint(result, indent=2)
# pprint(error)

class TaskUnitSchema(Schema):
    token = fields.Str()
    shelf_id = fields.Int()
    bin_id = fields.Int()
    sku_dropped = fields.Bool()

class TaskSchema(Schema):
    batch_id = fields.Str()
    data = fields.Nested(TaskUnitSchema, many=True) # 如果是嵌套一层object, 则many=False

json_data = {
    "batch_id": 12345,
    "data": [
        {
            "token": "1600000",
            "shelf_id": 1,
            "bin_id": 2,
            "sku_dropped": True
        },
        {
            "token": "1600001",
            "shelf_id": 1,
            "bin_id": 1,
            "sku_dropped": False
        }
    ]
}
taskschema = TaskSchema()
res, err = taskschema.dump(json_data)
print(type(res))
pprint(res)
pprint(err)

# When the value name if json is keyword in python
# https://stackoverflow.com/questions/51727441/marshmallow-how-can-i-map-the-schema-attribute-to-another-key-when-serializing

class TemporalExtentSchema(Schema):
    # Marshmallow 2
    t_from = fields.String(required=True, dump_to='from', load_from='from')
    # Marshmallow 3
    t_from = fields.String(required=True, data_key='from')
    to = fields.String(required=True)
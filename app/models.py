import peewee as pw

db = pw.SqliteDatabase('./db/okapa.db')

class OkBaseModel(pw.Model):

  class Meta:
    database = db

class OkLicense(OkBaseModel):
  id = pw.PrimaryKeyField()
  name = pw.CharField()
  url = pw.CharField()

class OkResourceType(OkBaseModel):
  id = pw.PrimaryKeyField()
  name = pw.CharField()

class OkResource(OkBaseModel):
  id = pw.PrimaryKeyField()
  name = pw.CharField()
  type = pw.ForeignKeyField(OkResourceType)
  description = pw.TextField()
  license = pw.ForeignKeyField(OkLicense)

class OkResourceComposition(OkBaseModel):
  parent = pw.ForeignKeyField(OkResource, related_name='components')
  child = pw.ForeignKeyField(OkResource)

  class Meta:
    primary_key = pw.CompositeKey('parent','child')

class OkMediaType(OkBaseModel):
  id = pw.PrimaryKeyField()
  name = pw.CharField()

class OkMedia(OkBaseModel):
  id = pw.PrimaryKeyField()
  name = pw.CharField()
  type = pw.ForeignKeyField(OkMediaType)
  url = pw.CharField()

class OkResourceToMedia(OkBaseModel):
  resource = pw.ForeignKeyField(OkResource)
  media = pw.ForeignKeyField(OkMedia)

  class Meta:
    primary_key = pw.CompositeKey('resource','media')


if __name__ == '__main__':
    db.connect()
    db.create_tables([OkLicense,
                      OkResourceType,
                      OkResource,
                      OkResourceComposition,
                      OkMediaType,
                      OkMedia,
                      OkResourceToMedia
    ], safe=False)

import bottle as bt
import jinja2 as j2

from models import * 
from playhouse.shortcuts import model_to_dict

#
# app config
#

TEMPLATE_PATH='./templates/'
STATIC_PATH='./static/'

#
# hook database connection lifecycle to request handlers
#

@bt.hook('before_request')
def _connect_db():
    db.connect()

@bt.hook('after_request')
def _close_db():
    if not db.is_closed():
        db.close()

#
# For now the root, challenges, and experiments pages are static
#

@bt.get('/')
def root_index():
    return bt.static_file('index.html', root=TEMPLATE_PATH)

@bt.get('/challenges/')
def challenge_index():
    return bt.static_file('challenges.html', root=TEMPLATE_PATH)

@bt.get('/experiments/')
def experiment_index():
    return bt.static_file('experiments.html', root=TEMPLATE_PATH)

@bt.get('/resources/')
def resource_index():
    return bt.static_file('resources.html', root=TEMPLATE_PATH)

#
# Resource CRUD
#

@bt.get('/api/resources')
def api_resource_index():
    resources = OkResource.select()
    result = [model_to_dict(r) for r in resources]
    return { 'data': result }

@bt.post('/api/resources')
def api_resource_create():
    data = bt.request.json
    new_resource = OkResource(**data)
    new_resource.save()
    return { 'data': { 'id': new_resource.id} }

@bt.get('/api/resources/<id>')
def api_resource_get(id):
    resource = OkResource.get(OkResource.id == id)
    return { 'data': model_to_dict(resource) }

@bt.put('/api/resources/<id>')
def api_resource_update(id):
    data = bt.request.json
    OkResource.update(**data).where(OkResource.id == id).execute()

@bt.delete('/api/resources/<id>')
def api_resource_delete(id):
    resource = OkResource.get(OkResource.id == id)
    resource.delete_instance()

#
# Resource Types CRUD
#

@bt.get('/api/rtypes')
def api_rtype_index():
    rtypes = OkResourceType.select()
    result = [model_to_dict(r) for r in rtypes]
    return { 'data': result }

@bt.post('/api/rtypes')
def api_rtype_add():
    data = bt.request.json
    new_rtype = OkResourceType(**data)
    new_rtype.save()
    return { 'data': { 'id': new_rtype.id } }

@bt.get('/api/rtypes/<id>')
def api_rtype_get(id):
    rtype = OkResourceType.get(OkResourceType.id == id)
    return { 'data': model_to_dict(rtype) }

@bt.put('/api/rtypes/<id>')
def api_rtype_update(id):
    data = bt.request.json
    OkResourceType.update(**data).where(OkResourceType.id == id)

@bt.delete('/api/rtypes/<id>')
def api_rtype_delete(id):
    rtype = OkResourceType.get(OkResourceType.id == id)
    rtype.delete_instance()

#
# Media CRUD
#

@bt.get('/api/media')
def api_media_index():
    media = OkMedia.select()
    result = [model_to_dict(m) for m in media]
    return { 'data': result }
    
@bt.post('/api/media')
def api_media_add():
    data = bt.request.json
    new_media = OkMedia(**data)
    new_media.save()
    return { 'data': {'id': new_media.id} }

@bt.get('/api/media/<id>')
def api_media_get(id):
    media = OkMedia.get(OkMedia.id == id)
    return { 'data': model_to_dict(media) }
    
@bt.put('/api/media/<id>')
def api_media_update(id):
    data = bt.request.json
    OkMedia.update(**data).where(OkMedia.id == id).execute()

    
@bt.delete('/api/media/<id>')
def api_media_delete(id):
    media = OkMedia.get(OkMedia.id == id)
    media.delete_instance()
    
#
# License CRUD
#

@bt.get('/api/licenses')
def api_license_index():
    licenses = OkLicense.select()
    result = [model_to_dict(l) for l in licenses]
    return { 'data': result }

@bt.post('/api/licenses')
def api_license_add():
    data = bt.request.json
    new_license = OkLicense(**data)
    new_license.save()
    return { 'data': {'id': new_license.id} }

@bt.get('/api/licenses/<id>')
def api_license_get(id):
    license = OkLicense.get (OkLicense.id == id)
    return { 'data': model_to_dict(license) }

@bt.put('/api/licenses/<id>')
def api_license_update(id):
    data = bt.request.json
    OkLicense.update(**data).where(OkLicense.id == id).execute()
    
@bt.delete('/api/licenses/<id>')
def api_license_delete(id):
    license = OkLicense.get(OkLicense.id == id)
    license.delete_instance()

#
# Static file route
#

@bt.get('/static/<filepath:path>')
def static(filepath):
    return bt.static_file(filepath, root=STATIC_PATH)

#
# Start the app
#

bt.run(host='localhost', port=8080, debug=True)

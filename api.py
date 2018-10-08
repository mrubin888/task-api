# api.py

import falcon

from resources import tasks 
from resources import things

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class TasksResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

# Create a callable WSGI app
app = falcon.API()

things = things.ThingsResource()
tasks = tasks.TasksResource()

app.add_route('/things', things)
app.add_route('/tasks', tasks)
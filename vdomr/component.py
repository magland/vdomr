import base64
from IPython.display import Javascript
import uuid
import abc

class Component(object):
  def __init__(self):
    self._div_id=str(uuid.uuid4())
  @abc.abstractmethod
  def render(self):
    return None
  def refresh(self):
    html=self.render().to_html()
    html_encoded=base64.b64encode(html.encode('utf-8')).decode('utf-8')
    js="document.getElementById('{}').innerHTML=atob('{}'); console.log('test1');".format(self._div_id,html_encoded)
    display(Javascript(js))
  def _repr_html_(self):
    html=self.render().to_html()
    return '<div id={}>'.format(self._div_id)+html+'</div>'


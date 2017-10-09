import os
import tornado.ioloop
import tornado.web
import tornado.log
import requests
import urllib

from dotenv import load_dotenv
from jinja2 import Environment, PackageLoader, select_autoescape

load_dotenv('.env')

PORT = int(os.environ.get('PORT', '8000'))

ENV = Environment(
    loader=PackageLoader('weather', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
) 

class TemplateHandler(tornado.web.RequestHandler):
    def render_template (self, tpl, context):
        template = ENV.get_template(tpl)
        self.write(template.render(**context))

class MainHandler(TemplateHandler):
    def get (self):
        return self.render_template("home.html", {})

    def post (self):
        location = self.get_body_argument('location')
        encodeLocation = urllib.parse.quote_plus(location)
        # Request to Google Maps
        payload = {'address': encodeLocation, 'key': os.environ['KEY']}
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        print(response.url)
        data = response.json()
        location = data['results'][0]['formatted_address']
        # Retrieve lat and long from Google Maps 
        data = response.json()
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        # Houston, TX example for dark sky 
        # lat = '29.7535882'
        # lng = '-95.1797696'
        # Request to DarkSky 
        response = requests.get('https://api.darksky.net/forecast/{}/{},{}'.format(os.environ['SECRET_KEY'], lat, lng))
        data = response.json()
        summary = data['currently']['summary']
        icon = data['currently']['icon']
        temp = data['currently']['temperature']
        return self.render_template("home.html", {'location': location, 'summary': summary, 'icon': icon, 'temp': temp})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/static/(.*)", 
        tornado.web.StaticFileHandler, {'path': 'static'}),
    ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(PORT, print('Creating magic on port {}'.format(PORT)))
    tornado.ioloop.IOLoop.current().start()
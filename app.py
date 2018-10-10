import connexion
import os

from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from services.provider import ItemsProvider

def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"IdContenedor": os.getenv('HOSTNAME')}])
    )

if __name__ == '__main__':
	app = connexion.App(__name__, specification_dir='swagger/', swagger_ui=True)
	app.add_api('my_app.yaml', resolver=RestyResolver('api'))
	FlaskInjector(app=app.app,modules=[configure])
	# app.run(host='0.0.0.0',port=9090)
	port_service = 9090
	if os.getenv('PORT') :
		port_service = int(os.getenv('PORT'))
	
	app.run(host='0.0.0.0',port=port_service)
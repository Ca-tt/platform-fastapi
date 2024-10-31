from api.api import API

api = API()
app = api.app

api.set_route(route_path="/", return_data="welcome_message")
api.set_route(route_path="/projects", return_data="projects")
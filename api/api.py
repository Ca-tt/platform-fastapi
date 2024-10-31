from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.projects import Projects


class API:
    def __init__(self):
        self.app = FastAPI()
        self.app.mount("/img", StaticFiles(directory="api/static/img"), name="img")
        
        
        self.projects = Projects()
        self.projects.set_ids_for_projects()
        
    
    def set_route(self, route_path: str ="/", return_data: Union[str, dict] = ""):
        @self.app.get(route_path)
        def api_method():
            data_to_return = self.use_variable(return_data)
            return data_to_return
        
    def use_variable(self, variable_name):
        self.variables = {
            "welcome_message": "Welcome to EXPAND API ⭐",
            "projects": self.projects.get_all_projects()
        }
        
        return self.variables[variable_name]
        



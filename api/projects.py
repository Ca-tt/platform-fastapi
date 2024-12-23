from api.utils.Logger import Logger
from api.data.projects.js import JS_PROJECTS
from api.data.projects.projects import PROJECTS

ALL_PROJECTS = JS_PROJECTS + PROJECTS

class Projects:
    def __init__(self):
        self.logger = Logger()
        self.all_projects = ALL_PROJECTS
        
    def set_ids_for_projects(self):
        id = -1
        
        for project in self.all_projects:
            id += 1
            project["id"] = id
            
        self.logger.info(f"id's pinned!")
    
    def get_all_projects(self) -> list[dict]:
        return self.all_projects
        
            

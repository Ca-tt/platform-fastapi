from typing import TypedDict

class ProjectT(TypedDict): 
    name: str

    language: str
    category: str
    subcategory: str
    task_type: str
    difficulty: dict[str, int]

    title: str
    description: str
    
    skills_to_improve: list[str]
    reward: str
    
    link: str
    preview_image: str

    isTeamProject: bool 
    other_languages: list[str]
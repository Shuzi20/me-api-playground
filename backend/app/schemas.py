from pydantic import BaseModel
from typing import List, Optional

# ---------- Skill ----------
class SkillBase(BaseModel):
    name: str
    level: Optional[str] = None

class SkillCreate(SkillBase):
    pass

class SkillUpdate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    class Config:
        from_attributes = True


# ---------- Project ----------
class ProjectBase(BaseModel):
    title: str
    description: str
    repo_url: Optional[str]
    demo_url: Optional[str]

class ProjectCreate(ProjectBase):
    skill_ids: List[int] = []

class ProjectUpdate(ProjectBase):
    skill_ids: List[int] = []

class Project(ProjectBase):
    id: int
    skills: List[Skill] = []
    class Config:
        from_attributes = True


# ---------- Experience ----------
class ExperienceBase(BaseModel):
    company: str
    role: str
    description: str
    start_date: str
    end_date: Optional[str]

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceUpdate(ExperienceBase):
    pass

class Experience(ExperienceBase):
    id: int
    class Config:
        from_attributes = True


# ---------- Link ----------
class LinkBase(BaseModel):
    label: str
    url: str

class LinkCreate(LinkBase):
    pass

class LinkUpdate(LinkBase):
    pass

class Link(LinkBase):
    id: int
    class Config:
        from_attributes = True


# ---------- Profile ----------
class ProfileBase(BaseModel):
    full_name: str
    email: str
    headline: str
    location: str
    summary: str

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    skills: List[Skill] = []
    projects: List[Project] = []
    experiences: List[Experience] = []
    links: List[Link] = []
    class Config:
        from_attributes = True

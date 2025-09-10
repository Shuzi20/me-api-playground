from sqlalchemy.orm import Session
from . import models, schemas

# ---------- Profile ----------
def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, profile_id: int, updates: schemas.ProfileUpdate):
    db_profile = db.query(models.Profile).get(profile_id)
    if db_profile:
        for key, value in updates.dict().items():
            setattr(db_profile, key, value)
        db.commit()
        db.refresh(db_profile)
    return db_profile

def delete_profile(db: Session, profile_id: int):
    profile = db.query(models.Profile).get(profile_id)
    if profile:
        db.delete(profile)
        db.commit()
    return profile

def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()


# ---------- Skills ----------
def create_skill(db: Session, skill: schemas.SkillCreate, profile_id: int):
    db_skill = models.Skill(**skill.dict(), profile_id=profile_id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def update_skill(db: Session, skill_id: int, updates: schemas.SkillUpdate):
    db_skill = db.query(models.Skill).get(skill_id)
    if db_skill:
        for key, value in updates.dict().items():
            setattr(db_skill, key, value)
        db.commit()
        db.refresh(db_skill)
    return db_skill

def delete_skill(db: Session, skill_id: int):
    skill = db.query(models.Skill).get(skill_id)
    if skill:
        db.delete(skill)
        db.commit()
    return skill


# ---------- Projects ----------
def create_project(db: Session, project: schemas.ProjectCreate, profile_id: int):
    db_project = models.Project(
        title=project.title,
        description=project.description,
        repo_url=project.repo_url,
        demo_url=project.demo_url,
        profile_id=profile_id
    )
    if project.skill_ids:
        db_project.skills = db.query(models.Skill).filter(models.Skill.id.in_(project.skill_ids)).all()
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: int, updates: schemas.ProjectUpdate):
    db_project = db.query(models.Project).get(project_id)
    if db_project:
        db_project.title = updates.title
        db_project.description = updates.description
        db_project.repo_url = updates.repo_url
        db_project.demo_url = updates.demo_url
        if updates.skill_ids:
            db_project.skills = db.query(models.Skill).filter(models.Skill.id.in_(updates.skill_ids)).all()
        db.commit()
        db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    project = db.query(models.Project).get(project_id)
    if project:
        db.delete(project)
        db.commit()
    return project


# ---------- Experiences ----------
def create_experience(db: Session, experience: schemas.ExperienceCreate, profile_id: int):
    db_exp = models.Experience(**experience.dict(), profile_id=profile_id)
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp

def update_experience(db: Session, exp_id: int, updates: schemas.ExperienceUpdate):
    db_exp = db.query(models.Experience).get(exp_id)
    if db_exp:
        for key, value in updates.dict().items():
            setattr(db_exp, key, value)
        db.commit()
        db.refresh(db_exp)
    return db_exp

def delete_experience(db: Session, exp_id: int):
    exp = db.query(models.Experience).get(exp_id)
    if exp:
        db.delete(exp)
        db.commit()
    return exp


# ---------- Links ----------
def create_link(db: Session, link: schemas.LinkCreate, profile_id: int):
    db_link = models.Link(**link.dict(), profile_id=profile_id)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def update_link(db: Session, link_id: int, updates: schemas.LinkUpdate):
    db_link = db.query(models.Link).get(link_id)
    if db_link:
        for key, value in updates.dict().items():
            setattr(db_link, key, value)
        db.commit()
        db.refresh(db_link)
    return db_link

def delete_link(db: Session, link_id: int):
    link = db.query(models.Link).get(link_id)
    if link:
        db.delete(link)
        db.commit()
    return link

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Me-API Playground")
@app.get("/")
def root():
    return {"message": "Me-API backend is running"}
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

# ---------- Profiles ----------
@app.post("/profiles", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db, profile)

@app.get("/profiles/{profile_id}", response_model=schemas.Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    return crud.get_profile(db, profile_id)

@app.put("/profiles/{profile_id}", response_model=schemas.Profile)
def update_profile(profile_id: int, profile: schemas.ProfileUpdate, db: Session = Depends(get_db)):
    return crud.update_profile(db, profile_id, profile)

@app.delete("/profiles/{profile_id}")
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    return crud.delete_profile(db, profile_id)


# ---------- Skills ----------
@app.post("/profiles/{profile_id}/skills", response_model=schemas.Skill)
def add_skill(profile_id: int, skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    return crud.create_skill(db, skill, profile_id)

@app.put("/skills/{skill_id}", response_model=schemas.Skill)
def update_skill(skill_id: int, skill: schemas.SkillUpdate, db: Session = Depends(get_db)):
    return crud.update_skill(db, skill_id, skill)

@app.delete("/skills/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    return crud.delete_skill(db, skill_id)


# ---------- Projects ----------
@app.post("/profiles/{profile_id}/projects", response_model=schemas.Project)
def add_project(profile_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project, profile_id)

@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    return crud.update_project(db, project_id, project)

@app.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    return crud.delete_project(db, project_id)


# ---------- Experiences ----------
@app.post("/profiles/{profile_id}/experiences", response_model=schemas.Experience)
def add_experience(profile_id: int, experience: schemas.ExperienceCreate, db: Session = Depends(get_db)):
    return crud.create_experience(db, experience, profile_id)

@app.put("/experiences/{exp_id}", response_model=schemas.Experience)
def update_experience(exp_id: int, experience: schemas.ExperienceUpdate, db: Session = Depends(get_db)):
    return crud.update_experience(db, exp_id, experience)

@app.delete("/experiences/{exp_id}")
def delete_experience(exp_id: int, db: Session = Depends(get_db)):
    return crud.delete_experience(db, exp_id)


# ---------- Links ----------
@app.post("/profiles/{profile_id}/links", response_model=schemas.Link)
def add_link(profile_id: int, link: schemas.LinkCreate, db: Session = Depends(get_db)):
    return crud.create_link(db, link, profile_id)

@app.put("/links/{link_id}", response_model=schemas.Link)
def update_link(link_id: int, link: schemas.LinkUpdate, db: Session = Depends(get_db)):
    return crud.update_link(db, link_id, link)

@app.delete("/links/{link_id}")
def delete_link(link_id: int, db: Session = Depends(get_db)):
    return crud.delete_link(db, link_id)

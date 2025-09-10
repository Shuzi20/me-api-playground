from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Many-to-many: projects <-> skills
project_skills = Table(
    "project_skills",
    Base.metadata,
    Column("project_id", ForeignKey("projects.id"), primary_key=True),
    Column("skill_id", ForeignKey("skills.id"), primary_key=True)
)

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    headline = Column(String)
    location = Column(String)
    summary = Column(Text)

    skills = relationship("Skill", back_populates="profile")
    projects = relationship("Project", back_populates="profile")
    links = relationship("Link", back_populates="profile")
    experiences = relationship("Experience", back_populates="profile")


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String, nullable=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))

    profile = relationship("Profile", back_populates="skills")
    projects = relationship("Project", secondary=project_skills, back_populates="skills")


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    repo_url = Column(String, nullable=True)
    demo_url = Column(String, nullable=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))

    profile = relationship("Profile", back_populates="projects")
    skills = relationship("Skill", secondary=project_skills, back_populates="projects")


class Experience(Base):
    __tablename__ = "experience"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    role = Column(String)
    description = Column(Text)
    start_date = Column(String)
    end_date = Column(String, nullable=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))

    profile = relationship("Profile", back_populates="experiences")


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    url = Column(String)
    profile_id = Column(Integer, ForeignKey("profiles.id"))

    profile = relationship("Profile", back_populates="links")

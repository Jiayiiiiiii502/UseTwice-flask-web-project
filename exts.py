# exts.py:import sql-alchemy and create instance
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# create actual instance of sql-alchemy and mail
db=SQLAlchemy()
mail=Mail()
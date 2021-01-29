from .Utils.Constants import *
from .DataAccess.CategoryRepository import CategoryRepository

#print(DB_PATH)

p = CategoryRepository()

p.get_all()
from CRUD_Operations import app, db
app.app_context().push()
db.create_all()
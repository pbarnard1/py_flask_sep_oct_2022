from flask_app import app # Bug fix: "flask_app", NOT "flask_ap", for folder name
# Bug fix: "__init__.py", NOT "_init_.py" - need two "_" on each side
from flask_app.controllers import games # Bug fix: flask_app.controllers, NOT .controller - make sure folder names match

if __name__=="__main__":
    app.run(debug=True)

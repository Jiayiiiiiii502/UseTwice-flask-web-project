from flask import Flask, render_template
import config
from views import user_bp,object_bp

app = Flask(__name__)

# combine config
app.config.from_object(config)

# combine views
app.register_blueprint(user_bp)
app.register_blueprint(object_bp)



if __name__ == '__main__':
    app.run()

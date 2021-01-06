"""Server for Shopify Backend Challenge"""

from flask import (Flask, render_template, request, session, jsonify)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
import upload_api


app = Flask(__name__)
app.secret_key = "images"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """show initial landing page"""

    return render_template('imageupload.html')


def get_image_library():
    """get all images from library"""

    image_library = crud.get_image_library_json()
    return jsonify(image_library)


@app.route('/newimage', methods=['POST'])
def upload_item():
    """Upload new image to repository"""

    image = request.files.get('file')
    print(image)
    if image:
        image_url = upload_api.upload_closet_image(image)
        image_name = request.form.get('image_name')
        image_description = request.form.get('image_description')

        new_image = crud.create_image(image_name, image_description, image_url)
        session['image_id'] = new_image.image_id

        return jsonify(crud.jsonify_image(new_image))


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=False, host='0.0.0.0')

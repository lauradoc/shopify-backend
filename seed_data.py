"""creating initial data"""

import json

import crud
import model
import server

model.connect_to_db(server.app)
model.db.create_all()


def seed_image():
    """preloaded images for image library"""

    with open('data/image_data.json') as f:
        image_data = json.loads(f.read())

    for image in image_data:
        image_name = image['image_name']
        image_description = image['image_description']
        image_url = image['image_url']

        new_image = crud.create_image(image_name, image_description, image_url)


seed_image()

"""CRUD operations. Utility functions for creating data"""

from model import db, Image, connect_to_db


def create_image(image_name, image_description, image_url):
    """Creates new image in database to add to library"""

    image = Image(image_name=image_name,
                  image_description=image_description, image_url=image_url)

    db.session.add(image)
    db.session.commit()

    return image


def jsonify_image(image):
    """jsonify image data to use in js to view full image repository"""

    json_image = {
        'id': image.item_id,
        'image_name': image.image_name,
        'image_description': image.image_description,
        'image_url': image.image_url
    }

    return json_image


def get_image_library_json():
    """display all images from library"""

    image_library_json = []
    images = Image.query.all()
    for image in images:
        image_dict = {
            "id": image.image_id,
            "image_name": image.image_name,
            "image_description": image.image_description,
            "image_url": image.image_url
        }

    return image_library_json


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

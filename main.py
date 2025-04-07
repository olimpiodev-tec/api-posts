from flask import Flask, request
from werkzeug.utils import secure_filename
from controller.post_controller import *
from controller.comment_controller import get_comments_by_post_id_ctrl, get_comments_ctrl

UPLOADS_PHOTO = 'photos'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOADS_PHOTO

@app.route('/posts', methods=['GET'])
def get_posts():
    return get_posts_ctrl()

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    return get_post_by_id_ctrl(post_id)

@app.route('/posts', methods=['POST'])
def create_post():
    path_save_photo = ''

    if 'photo_post' in request.files:
        try:
            photo = request.files['photo_post']
            photo_name = secure_filename(photo.filename)
            path_save_photo = UPLOADS_PHOTO + '/' + photo_name
            photo.save(path_save_photo)
        except Exception as error:
            print(error)
            return 'Erro ao salvar foto'
    else:
        return 'Post não contém foto'

    post = request.form.to_dict()
    post['photo_path'] = path_save_photo
    print(post)
    return create_post_ctrl(post)

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    return update_post_ctrl(post_id, request.json)

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    return delete_post_ctrl(post_id)

@app.route('/posts/<int:post_id>/comments/', methods=['GET'])
def get_comments_by_post_id(post_id):
    return get_comments_by_post_id_ctrl(post_id)

@app.route('/comments', methods=['GET'])
def get_comments():
    return get_comments_ctrl()

if __name__ == '__main__':
    app.run(debug=True)
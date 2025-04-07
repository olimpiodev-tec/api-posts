from flask import Flask, request
from werkzeug.utils import secure_filename
from controller.post_controller import get_posts_ctrl, get_post_by_id_ctrl
from controller.comment_controller import get_comments_ctrl

UPLOADS_PHOTO = 'photos'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOADS_PHOTO

@app.route('/posts', methods=['GET'])
def get_posts():
    return get_posts_ctrl()

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    return get_post_by_id_ctrl(post_id)

@app.route('/comments', methods=['GET'])
def get_comments():
    return get_comments_ctrl()

@app.route('/posts', methods=['POST'])
def create_post():
    # Primeiro vamos salvar a foto
    if 'photo_post' in request.files:
        photo = request.files['photo_post']
        photo_name = secure_filename(photo.filename)
        photo_path = UPLOADS_PHOTO + '/' + photo_name
        photo.save(photo_path)

        return 'Post criado com sucesso'
    else:
        return 'Post não contém foto'

if __name__ == '__main__':
    app.run(debug=True)


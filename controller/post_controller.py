from database.conexao import get_db_connection
from models.post import Post

def get_posts_ctrl():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                post_id, author, title 
            FROM 
                posts;
        """
    )

    results = cursor.fetchall()

    if len(results) == 0:
        return 'Sem posts para mostrar'

    cursor.close()
    conn.close()

    posts = []

    for result in results:
        post = Post(post_id=result[0],
                    author=result[1],
                    title=result[2])
        posts.append(post.to_json())

    return posts


def get_post_by_id_ctrl(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                post_id, author, title, photo_path
            FROM 
                posts
            WHERE 
                post_id = %s
        """, (post_id,)
    )

    result = cursor.fetchone()

    if len(result) == 0:
        return 'Post não encontrado'

    cursor.close()
    conn.close()

    post = Post(post_id=result[0],
                author=result[1],
                title=result[2],
                photo_path=result[3])

    return post.to_json()

def create_post_ctrl(post_data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO 
                posts (author, title, photo_path)
            VALUES 
                (%s, %s, %s) RETURNING post_id;
        """, (post_data.get('author'), post_data.get('title'), post_data.get('photo_path'))
    )

    post_id = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    post = get_post_by_id_ctrl(post_id)

    return post

def update_post_ctrl(post_id, post_data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            UPDATE 
                posts 
            SET 
                author=%s, title=%s
            WHERE 
                post_id=%s;
        """, (post_data.get('author'), post_data.get('title'), post_id)
    )

    conn.commit()
    conn.close()

    return 'Post atualizado'

def delete_post_ctrl(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            DELETE 
                FROM 
            posts 
                WHERE 
            post_id = %s
        """, (post_id,)
    )

    conn.commit()
    conn.close()

    return 'Post removido com sucesso'
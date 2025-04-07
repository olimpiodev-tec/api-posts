from database.conexao import get_db_connection
from models.comment import Comment

def get_comments_ctrl():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                comment_id, post_id, description
            FROM
                comments;
        """
    )

    results = cursor.fetchall()

    if len(results) == 0:
        return 'Sem comentários para mostrar'

    cursor.close()
    conn.close()

    comments = []

    for result in results:
        comment = Comment(comment_id=result[0],
                          post_id=result[1],
                          description=result[2])
        comments.append(comment.to_json())

    return comments

def get_comments_by_post_id_ctrl(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT
                comment_id, post_id, description
            FROM
                comments
            WHERE post_id = %s
        """, (post_id,)
    )

    results = cursor.fetchall()

    if len(results) == 0:
        return f'Sem comentários para post {post_id}'

    cursor.close()
    conn.close()

    comments = []

    for result in results:
        comment = Comment(comment_id=result[0],
                          post_id=result[1],
                          description=[2])
        comments.append(comment)

    return comments

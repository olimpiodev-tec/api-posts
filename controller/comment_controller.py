from database.conexao import get_connection
from models.comment import Comment

def get_comments_ctrl():
    """Busca todos os comentários"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT 
                comment_id, post_id, description 
            FROM 
                comments;
        """
    )

    resultados = cursor.fetchall()

    if len(resultados) == 0:
        return 'Sem comentários cadastrados'

    cursor.close()
    conn.close()

    comments = []

    for resultado in resultados:
        comment = Comment(comment_id=resultado[0],
                          post_id=resultado[1],
                          description=resultado[2])
        comments.append(comment.to_json())

    return comments
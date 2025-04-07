from database.conexao import get_connection
from models.post import Post

def get_posts_ctrl():
    """Busca a lista de posts"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT post_id, author, title FROM posts;
        """
    )

    resultados = cursor.fetchall()

    if len(resultados) == 0:
        return 'Sem posts cadastrados'

    cursor.close()
    conn.close()

    posts = []

    for resultado in resultados:
        post = Post(post_id=resultado[0],
                    author=resultado[1],
                    title=resultado[2])
        posts.append(post.to_json())

    return posts

def get_post_by_id_ctrl(post_id):
    """Busca um post pelo seu identificador"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT post_id, author, title FROM posts
        WHERE post_id = %s 
        """, (post_id,)
    )

    resultado = cursor.fetchone()

    if len(resultado) == 0:
        return 'Post não encontrado'

    cursor.close()
    conn.close()

    post = Post(post_id=resultado[0],
                author=resultado[1],
                title=resultado[2])

    return post.to_json()
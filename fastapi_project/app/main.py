import time
from fastapi import FastAPI, Response, status, HTTPException
from app.models.Post import Post
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='root', password='root', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")

        break
    except Exception as error:
        print("An exception occurred")
        print("Error : ", error)
        time.sleep()


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}


@app.get("/posts/latest")
def get_latest_post():
    cursor.execute(
        """SELECT * FROM public.posts  ORDER BY created_at  desc LIMIT 1 """)
    latest_post = cursor.fetchone()
    return {"data": latest_post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):

    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")
    return {"post_details": post}


@app.post("/createpost", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):

    cursor.execute(
        """  INSERT INTO posts(title, content, published) VALUES(%s, %s ,%s) RETURNING * """,
        (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    cursor.execute(
        """DELETE FROM posts WHERE id = %s  RETURNING * """, (str(id)),)
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    cursor.execute(
        """UPDATE posts SET title = %s, content= %s, published = %s WHERE id = %s  RETURNING * """,
        (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    return {"data": updated_post}

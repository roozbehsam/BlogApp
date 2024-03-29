# BlogApp
A Blog App Back-end Using: Django, Postgres, Docker, JWT

### Installation
1. Make a copy of `.env.example` and rename it to `.env`
2. Fill `.env` values with your desired ones
3. Run `docker-compose build` then `docker-compose up -d`

### Run Tests
Simply run `pytest` in root directory of the project.


### End-Points

|   |   |                                        |
|---|---|----------------------------------------|
| GET  |  /api/post/post_pk/comment/ | Lists all the comments related to a post |
|  GET |  /api/post/post_pk/comment/comment_pk/	 | Retrieves a specific comment           |
|  POST |  /api/post/post_pk/comment/	 | Creates a comment                      |
|PUT   | /api/post/post_pk/comment/comment_pk/	  | Modifies a comment                     |
|  DELETE |  /api/post/post_pk/comment/comment_pk/ | Deletes a comment|

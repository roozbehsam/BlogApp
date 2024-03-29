# BlogApp
A Blog App Back-end Using: Django, Postgres, Docker, JWT

### Installation
1. Make a copy of `.env.example` and rename it to `.env`
2. Fill `.env` values with your desired ones
3. Run `docker-compose build` then `docker-compose up -d`

### Run Tests
Simply run `pytest` in the root directory of the project.

### Development Environment
You can use both non-dockerized and dockerized for your development environment

`docker-compose -f docker-compose-dev.yml up -d (service name)` or just run all the services without specifying any.

### End-Points

Note: BREAD (browse, read, edit, add, delete)

|       |                                                                     |
|-------|---------------------------------------------------------------------|
| BREAD | /api/post/post_pk/comment/<br/>/api/post/post_pk/comment/comment_pk/ |
| BREAD | /api/post/<br/>/api/post/post_pk/                                              |


|      |                                  |
|------|----------------------------------|
| POST | api/auth/login/                  |                                        |
|   POST   | api/auth/register/               |
|   POST   | api/auth/refresh (refresh token) |
|   POST   | api/post/post_pk/like/           |
|   POST   | api/post/post_pk/remove_like/    |

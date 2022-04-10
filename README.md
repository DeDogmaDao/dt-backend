# DeDogmaDao backend

## used technologies:
- django/python
- postgres
- web3

# Todo:
- how to run doc
- Gunicorn worker setup
- Setup PgBouncer
- Celery
- Translations

---

# how to setup ci/cd:
- `build`: docker build -t <url/backend/backend:latest> .
- `push`: docker push image to docker-registry
- `deploy`:
  - NOTE: if the github secrets are not set in shell?. export all of them before deployment:
    - `export DEBUG=${{ secrets.DEBUG }} `
  - download docker-compose.deploy.yml file/ or pull/fetch repo 
  - create docker network: command -> `docker network create ddd_network || true`
  - create docker volumes for database and media files: command:
    - media files volume: `docker volume create --name=mediafiles || true`
  - bring down old running images: `docker-compose -f docker-compose.deploy.yml down`
  - make up new images: `docker-compose -f docker-compose.deploy.yml up -d`
  
---
### download single file from github by personal token
`curl -H "Authorization: token $PERSONAL_GITHUB_TOKEN" https://raw.githubusercontent.com/DeDogmaDao/dt-backend/master/docker-compose.deploy.yml > docker-compose.deploy.yml`

NOTE: if this works by github token(ci token), its better to use it. rather than persoanl token!
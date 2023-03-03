# Assignment_autocompany

## Set up the docker environment

Use this command in the project directory :

`docker-compose up -d --build`

(the --build option is only required if you updated the source code)

This will start a container :

    - Postgres Database

## Access APIs via Swagger
`http://localhost:8000/api/schema/swagger-ui`


## Stop and remove containers on the local environment

Use this command in the project directory :

`docker-compose down -v`

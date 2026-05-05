# adminer

> Ref: <https://github.com/vrana/adminer/>

## Usage

> - For example, your database container is named `papertorepo-db-1`, and you want to connect to it.
> - The original method is to run `psql` command inside the database container, like this:
>
>   ```bash
>   docker exec -it papertorepo-db-1 psql -U papertorepo -d papertorepo
>   ```
>
> - But with Adminer, you can run a separate container and connect to the database container through Docker network, which is more convenient and user-friendly, as below:

- Run in front attached mode, and remove when exit.

  ```bash
  NET=$(docker inspect -f '{{range $name, $_ := .NetworkSettings.Networks}}{{println $name}}{{end}}' papertorepo-db-1 | head -n1) && docker run --rm --name papertorepo-adminer --network "$NET" -p 8081:8080 adminer:latest
  ```

- Run in detached mode, and stop/remove manually.

  ```bash
  # Run
  NET=$(docker inspect -f '{{range $name, $_ := .NetworkSettings.Networks}}{{println $name}}{{end}}' papertorepo-db-1 | head -n1) && docker run -d --name papertorepo-adminer --network "$NET" -p 8081:8080 adminer:latest

  # Check status
  docker ps | grep papertorepo-adminer

  # Stop and remove
  docker stop papertorepo-adminer
  docker rm papertorepo-adminer
  ```

- Then you can access Adminer web interface at: <http://127.0.0.1:8081/?pgsql=papertorepo-db-1&username=papertorepo&db=papertorepo&ns=public>

# MIGRATIONS

In order to make the application easier to maintanain and scalable, we use migrations to handle the database changes.

## Managing the modifications

There are few commands to use to create or delete a table change

### Create the revison file

```alembic revision --autogenerate -m "create inital tables"```

### Upgrade the database

```alembic upgrade head```

### Downgrade if needed

```alembic downgrade -1```

## Useful commands

In this section, I’ll describe some useful Alembic commands, but I recommend exploring the [Alembic commands page](https://alembic.sqlalchemy.org/en/latest/api/commands.html) to learn more.

- Display the current revision for a database: `alembic current`.
- View migrations history: `alembic history --verbose`.
- Revert all migrations: `alembic downgrade base`.
- Revert migrations one by one: `alembic downgrade -1`.
- Apply all migrations: `alembic upgrade head`.
- Apply migrations one by one: `alembic upgrade +1`.
- Display all raw SQL: `alembic upgrade head --sql`.
- Reset the database: `alembic downgrade base && alembic upgrade head`.

## REFERENCES

[FastAPI - https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
[SQLAlchemy - https://www.sqlalchemy.org/](https://www.sqlalchemy.org/)
[Alembic - https://alembic.sqlalchemy.org/en/latest](https://alembic.sqlalchemy.org/en/latest)

# Setting up PostgresDB

## 1. Create DB named `bnb_django`

```shell
sudo -u postgres psql
create database bnb_django;
```

## 2. Create user with password and modify a few of the connection parameters.

```shell
create user dev with password 'passwordhere';
alter role dev set client_encoding to 'utf8';
alter role dev set default_transaction_isolation to 'read commited';
alter role dev set timezone to 'UTC';
```

## 3, Grant database user access

```shell
grant all privileges on database bnb_django to dev;
```

## 4. View list of databases.

```shell
\list
```

## 5. View list of users.

```shell
\du
```
CREATE DATABASE loandb;
CREATE USER loanuser WITH ENCRYPTED PASSWORD 'loanpw';
ALTER ROLE loanuser SET client_encoding TO 'utf8';
ALTER ROLE loanuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE loanuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE loandb TO loanuser;

ALTER ROLE  loanuser CREATEDB ; -- Required only for running Unit tests locally.
\q

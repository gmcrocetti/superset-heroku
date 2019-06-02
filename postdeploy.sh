#!/bin/sh

flask fab create-admin \
    --username admin \
    --firstname user \
    --lastname user \
    --email admin@fab.org \
    --password 123
superset db upgrade
superset init

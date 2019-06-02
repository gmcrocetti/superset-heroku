#!/bin/sh

flask fab create-admin
superset db upgrade
superset init

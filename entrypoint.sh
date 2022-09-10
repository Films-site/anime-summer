#!/bin/sh

yarn install && yarn dev

exec "$@"

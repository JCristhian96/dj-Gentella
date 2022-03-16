#!/bin/bash
./manage.py dumpdata --format json --indent 4 users.User > apps/users/fixtures/users.json
echo "Backup realizado exitosamente"
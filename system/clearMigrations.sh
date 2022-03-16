#!/bin/bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
echo "Migraciones eliminadas exitosamente"
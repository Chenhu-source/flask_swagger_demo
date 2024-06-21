#!/bin/bash

swagger_file="swagger/swagger.yaml"
if [ -f "$swagger_file" ]; then
    rm "$swagger_file"
fi

python3 -m flask_restx.api api spec > "$swagger_file"
echo "Swagger documentation generated at $swagger_file"


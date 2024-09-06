FROM isaui/python:django-deps-latest

WORKDIR /app

COPY . .

RUN echo '#!/bin/bash\n\
PROJECT_NAME=$(find . -maxdepth 2 -type f -name "wsgi.py" | cut -d "/" -f 2)\n\
if [ -z "$PROJECT_NAME" ]; then\n\
    echo "Error: Could not find Django project."\n\
    exit 1\n\
fi\n\
echo "Django project name: ${PROJECT_NAME}"\n\
gunicorn ${PROJECT_NAME}.wsgi:application\n'\
> /app/run.sh && chmod +x /app/run.sh

CMD ["/app/run.sh"]
FROM python:3-alpine

MAINTAINER JOHAN Sports <antonis@johan-sports.com>

# Get latest root certificates
RUN apk add --update ca-certificates && update-ca-certificates

# Install required packages
RUN pip install wscelery

# Force stdin/stdout/stderr to be completelly unbuffered
ENV PYTHONUNBUFFERED=1

# Default port
EXPOSE 1337

# Run as non-root user
USER nobody

ENTRYPOINT ["wscelery"]

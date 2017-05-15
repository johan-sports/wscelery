#!/bin/sh

if [ ! -z "${BROKER_URL}" ]; then
    echo "Using broker URL: ${BROKER_URL}"
fi

wscelery --broker=${BROKER_URL}

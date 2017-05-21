#!/bin/bash
#
# Script to use with 'letsencrypt-auto renew' to update the certificate
# validation endpoint and token.

LETS_ENCRYPT_FILE_NAME="lets_encrypt_validation"

echo "---" > $LETS_ENCRYPT_FILE_NAME
echo "layout: null" >> $LETS_ENCRYPT_FILE_NAME
echo "permalink: /.well-known/acme-challenge/$CERTBOT_TOKEN" >> $LETS_ENCRYPT_FILE_NAME
echo "---" >> $LETS_ENCRYPT_FILE_NAME

echo $CERTBOT_VALIDATION >> $LETS_ENCRYPT_FILE_NAME

git add $LETS_ENCRYPT_FILE_NAME
git commit -m "Renewing letsencrypt certificate"
git push

# Sleep to allow the change to get built by gitlab
SLEEP_TIME=120
sleep 120

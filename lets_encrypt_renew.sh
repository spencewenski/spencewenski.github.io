#!/bin/bash
#
# Script to automatically renew the letsencrypt script for the website

while true; do
  echo
  read -p "Warning!!! This script should not be used if more than one letsencrypt
certificate is managed on this device.

Are you sure you wish to continue? (yes/no) " yn
  case $yn in
    [Yy]* ) echo; echo 'Okay, running script.'; break;;
    [Nn]* ) echo; echo 'Okay, exiting'; exit;;
    * ) echo "Please answer yes or no.";;
  esac
done

# Get the directory that contains this script
CUR_DIR_NAME=""
if [[ $(uname -s) == "Darwin" ]]; then
  CUR_DIR_NAME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
else
  CUR_DIR_NAME="$(dirname $(readlink -f $0))"
fi

# Make sure lets encrypt scripts are installed
TOOLS_DIR="$HOME/tools"
LETS_ENCRYPT_SCRIPT_DIR="$TOOLS_DIR/letsencrypt"
if [ ! -d "$LETS_ENCRYPT_SCRIPT_DIR" ]; then
  LETS_ENCRYPT_URL="https://github.com/letsencrypt/letsencrypt"
  echo "Lets encrypt scripts not installed; installing from $LETS_ENCRYPT_URL"
  mkdir -p $TOOLS_DIR
  pushd $TOOLS_DIR > /dev/null
  git clone --depth 1 $LETS_ENCRYPT_URL
  popd > /dev/null
fi

# Use '--debug' flag to override experimental warning on mac
$LETS_ENCRYPT_SCRIPT_DIR/letsencrypt-auto renew --debug --manual-auth-hook $CUR_DIR_NAME/authenticator.sh --manual-public-ip-logging-ok

echo "
Now, go to the 'Pages' tab of the gitlab project and paste
/etc/letsencrypt/live/YOURDOMAIN.org/fullchain.pem to the Certificate (PEM) field
and /etc/letsencrypt/live/YOURDOMAIN.org/privkey.pem to the Key (PEM) field.

See https://about.gitlab.com/2016/04/11/tutorial-securing-your-gitlab-pages-with-tls-and-letsencrypt/
for more details."

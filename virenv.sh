#!/usr/bin/env bash

RED='\033[0;31m'
YELLOW='\033[1;33m'
GRAY='\033[1;30m'
NC='\033[0m'

if [ "$#" != 1 ]; then
    echo -e "${YELLOW}Usage:${NC} 1. if you want to (re)install the virtualenv in this dir,"
    echo -e "          please run '${YELLOW}$0 install${NC}'"
    echo -e "       2. if you want remove all file of the virtualenv in this dir,"
    echo -e "          please run '${YELLOW}$0 clean${NC}'"
    echo ""
    echo -e "${RED}Notice:${NC} if you run '${YELLOW}$0 install${NC}', this script will delete all files and"
    echo -e "        dirs list below:"
    echo -e "        ${RED}./.Python ./bin ./include ./lib${NC}"
    exit
fi

if [ "$1" == "install" ]; then
  echo "Cleaning up the virtualenv in this dir..."
  rm -rf .Python bin include lib > /dev/null 2>&1
  echo "done."
  echo ""
  sleep 2

  echo -e "Setting up the virtualenv in this dir...${GRAY}"
  virtualenv -p $(which python3) .

  if [ "$?" != 0 ]; then
    echo -e "${RED}Error:${NC} Setup virtualenv failing!"
    exit -1
  fi

  echo -e "${NC}"
  sleep 2

  echo -e "Installing below pip requirements...${GRAY}"
  source ./bin/activate
  cat requirements.txt 2> /dev/null

  if [ "$?" != 0 ]; then
    echo -e "${RED}Error:${NC} file requirements.txt missing!"
    exit -1
  fi

  pip install -U -r requirements.txt 1> /dev/null
  echo -e "${NC}done."
  echo ""
  echo -e "Please run '${YELLOW}source bin/activate${NC}' to activate the virtualenv."
  exit
fi

if [ "$1" == "clean" ]; then
  echo "Cleaning up the virtualenv in this dir..."
  rm -rf .Python bin include lib > /dev/null 2>&1
  echo "done."
  exit
fi

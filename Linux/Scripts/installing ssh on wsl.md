#!/bin/bash

echo "Installing SSH..."
sudo apt update
sudo apt install openssh-server -y

echo "Starting SSH..."
sudo service ssh start

echo "Enabling SSH to start on boot..."
sudo systemctl enable ssh

echo "Checking the status of the SSH service..."
sudo service ssh status
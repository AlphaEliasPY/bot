#!/bin/bash

# Detenemos el servicio del bot si ya está en ejecución
sudo systemctl stop bot.service

# Actualizamos el repositorio
cd /path/to/repo
git pull origin main

# Reiniciamos el servicio del bot
sudo systemctl start bot.service

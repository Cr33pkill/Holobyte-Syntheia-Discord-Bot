# SPDX-FileCopyrightText: © 2025 Cr33pkill
# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
#
# TheMain.py
#
# Copyright (C) ItzDavid And Cr33pkill, all rights reserved.
# This code is dual-licensed under MIT License and
# Python Software Foundation License 2.0
#
# If used in whole or in part under the MIT License
# the Copyright notice must be retained.
#
# © Cr33pkill 2025
#
# This a sub file for the Syntheia bot
# imports all the libraries used in the bot

import os

def dotenv_find():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(current_directory, '.env')
    return dotenv_path

def dotenv_load(file_path):
    var_list = []
    var_data_list = []
    """Load environment variables from a .env file."""
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} file not found!")
        return
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
                var_list.append(key.strip())
                var_data_list.append(value.strip())
    for i in range(len(var_list)):
        var_list[i] = var_list[i].replace('"', '').replace("'", '').strip()
        var_data_list[i] = var_data_list[i].replace('"', '').replace("'", '').strip()
    print(f"Environment variables loaded successfully: {var_list} , {var_data_list}")
    return var_data_list
#!/usr/bin/python3

import os
import subprocess
import sqlite3
import uuid
import datetime
import base64
import time
from cryptography.fernet import Fernet

dank_database = "dank_memories.db"
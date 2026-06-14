from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from datetime import timedelta
from unidecode import unidecode
import cx_Oracle
import requests
import smtplib
import locale
import os
import sys

sys.path.append(r"C:\rpa\Python")
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


class ApiCOMPANY_NAME:
    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa

    def consulta_precos(self, cnpj_cliente):
        pass # Logica de negocio removida por seguranca corporativa

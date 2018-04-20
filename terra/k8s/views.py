from django.shortcuts import render

# Create your views here.
from src.azure import Azclass as Azclass
from src.config import Config
from django.shortcuts import HttpResponseRedirect
configjson_file="/home/damato/projetos/dados.json"
envVars = Config(configjson_file)
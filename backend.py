import docker 
import asyncio
from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient


import nvsmi
import time 
import sys 
from dataclasses import dataclass 
from threading import Event
from typing import List
import aiodocker
import grpc 

import logging
import json
import numpy as np 
import subprocess
import base64

from mixing_types.mixing_service_pb2 import MixingRequest, MixingResponse
from mixing_types.mixing_service_pb2_grpc import MixingServiceStub

import streamlit as st

class Animator:
    def __init__(self, host, secure_connection=False, username=None, password=None):
        self.host = host 
        if secure_connection:
            self.channel = grpc.secure_channel(
                host, grpc.ssl_channel_credentials()
            )   

        else:
            self.channel = grpc.insecure_channel(
                host
            ) 
            
        if username and password:
            auth = base64.b64encode(f'{username}:{password}'.encode('ascii')).decode('ascii')
            self.metadata = [
                ('authorization', f'Basic {auth}')
            ]

        else:
            self.metadata = []

    def run(self, args):
        stub = MixingServiceStub(self.channel)

        mixing_request = MixingRequest(**args)

        print(mixing_request)

        mixing_response = stub.Generate(
            mixing_request, 
            metadata=self.metadata   
        )

        for chunk in mixing_response:
            yield chunk.video



        


    
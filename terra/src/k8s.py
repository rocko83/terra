#!/usr/bin/env python
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import urllib3
urllib3.disable_warnings()


class Connection():

    def __init__(self, server, token):
        self.server = server
        self.token = token

    def setConnection(self):
        self.configuration = client.Configuration()
        self.configuration.host = self.server
        self.configuration.verify_ssl = False
        self.configuration.api_key = {"authorization":"Bearer " + self.token}
        self.client = client
        self.client = self.client.Configuration.set_default(self.configuration)
        client.Configuration.set_default(self.configuration)

    def listPodsForAllNamespaces(self):
        self.v1 = client.CoreV1Api()
        pods = self.v1.list_pod_for_all_namespaces(watch=False)
        for i in pods.items:
          print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    def setNamespace(self,namespace):
        self.namespace = namespace

    def listNamespacedPods(self,namespace):
        self.v1 = client.CoreV1Api()
        pods = self.v1.list_namespaced_pod(self.namespace)
        for i in pods.items:
          print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    def listStorageClass(self):
        self.v1 = client.StorageV1Api()
        scs = self.v1.list_storage_class(watch=False)
        for i in scs.items:
          print(i.metadata.name)

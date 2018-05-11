from kubernetes import client as kubernetes_client
import urllib3
urllib3.disable_warnings()

class Kuby():
    def __init__(self,server,token):
        self.token = token
        self.server = server
        self.setConnection()

    def setConnection(self):
        try:
            self.configuration = kubernetes_client.Configuration()
            self.configuration.host = self.server
            self.configuration.verify_ssl = False
            self.configuration.api_key = {"authorization":"Bearer " + self.token}
            self.client = kubernetes_client
            self.client = self.client.Configuration.set_default(self.configuration)
            kubernetes_client.Configuration.set_default(self.configuration)
            self.v1 = kubernetes_client.CoreV1Api()
        except:
            print("Fail to connect to cluster")
    def getNamespaces(self):
        try:
            nss = self.v1.list_namespace()
            array = []
            for ns in nss.items:
                array.append(ns.metadata.name)
            return array
        except ValueError:
            print("Fail to get namespaces")
            return False
    def getNamespacesDetails(self,namespace):
        try:
            nss = self.v1.list_namespace()
            array = []
            for ns in nss.items:
                if ns.metadata.name == namespace:
                    print(ns)
            return array
        except ValueError:
            print("Fail to get namespaces")
            return False
    def getPodLog(self,namespace,pod,container):
        try:
            logs = self.v1.read_namespaced_pod_log(pod,namespace,container=container)
            return logs
        except ValueError:
            print("Failt to get log")
            return  False
    def getPodContainers(self,namespace,podname):
        try:
            pods = self.v1.list_namespaced_pod(namespace)
            array = []
            for pod in pods.items:
                if pod.metadata.name == podname and pod.metadata.namespace == namespace:
                    for container in pod.spec.containers:
                        array.append(container.name)
                        array.append(pod.metadata.name)
                        array.append(pod.metadata.uid)
                        array.append(pod.metadata.namespace)
            return array
        except ValueError:
            print("Fail to get pod containers")

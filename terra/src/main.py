#!/usr/bin/env python
#  coding=utf-8
#!C:\Python27\python.exe

from k8s import Connection
from kuby import Kuby
import argparse

class Main():

    def get_args():

        parser = argparse.ArgumentParser()

        parser.add_argument('--server',
                            required=True,
                            action='store',
                            help='Server Address')

        parser.add_argument('--token',
                            required=True,
                            action='store',
                            help="ApiToken")

        parser.add_argument('--namespace',
                            required=False,
                            action='store',
                            help="Namespace")

        args = parser.parse_args()

        return args

    args = get_args()
    k8s = Kuby(args.server,args.token)
    '''
    result = k8s.getNamespaces()
    if result == False:
        print("Error")
    else:
        for i in result:
            print(i)
    result = k8s.getNamespacesDetails("default")
    if result == False:
        print("Error")
    else:
        for i in result:
            print(i)
        print(result)
    
    #result = k8s.getPodLog("","")
    result = k8s.getPodContainers("","")
    if result == False:
        print("Error")
    else:
        for i in result:
            print(i)
    '''
    result = k8s.getPodLog("","","")
    if result == False:
        print("Error")
    else:
        print(result)
    result = k8s.getPodContainers("", "")
    if result == False:
        print("Error")
    else:
        for i in result:
            print(i)
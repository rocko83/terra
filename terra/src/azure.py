import azurerm
import json
class Azclass:
    def __init__(self,config):
        self.appid = config.getDados("AZ_APPID")
        self.dn = config.getDados("AZ_DISPLAYNAME")
        self.name = config.getDados("AZ_NAME")
        self.passwd = config.getDados("AZ_PASSWD")
        self.tenant = config.getDados("AZ_TENANT")
        self.subscription = config.getDados("AZ_SUBSCRIPTION")

    def getRegion(self):
        try:
            location = azurerm.list_locations(self.access_token, self.subscription)
            array = []
            for locale in location['value']:
                array2 = []
                array2.append(locale['displayName'])
                array2.append(locale['name'])
                array.append(array2)
            return array
        except ValueError:
            print("Fail to get Locations list")
            return  False

    def getResourceGroup(self):
        try:
            resource_groups = azurerm.list_resource_groups(self.access_token, self.subscription)
            array = []
            for rg in resource_groups['value']:
                #print(rg["name"] + ', ' + rg['location'] + ', ' + rg['properties']['provisioningState'])
                array2 = []
                array2.append(rg["name"])
                array2.append(rg['location'])
                array2.append(rg['properties']['provisioningState'])
                array.append(array2)
            return array

        except ValueError:
            print("Fail to get list of resource groups")
            return False

    def getVnet(self,region):
        try:
            vnets = azurerm.list_vnets(self.access_token, self.subscription)
            array = []
            for vnet in vnets['value']:
                if vnet['location'] != region:
                    continue
                else:
                    for subnet in vnet['properties']['subnets']:
                        #print(subnet['name'] + ', ' + vnet['name'] + ', vnetLocation=' + vnet['location'] + ', ' +
                        #      subnet['properties']['addressPrefix'] + ', ' + subnet['properties']['provisioningState'])
                        array2 = []
                        array2.append(subnet['name'])
                        array2.append(vnet['name'])
                        array2.append(vnet['location'])
                        array2.append(subnet['properties']['addressPrefix'])
                        array2.append(subnet['properties']['provisioningState'])
                        array2.append(subnet['id'])
                        array.append(array2)
            return array

        except ValueError:
            print("Fail to get Vnet list")
            return False
    def getImage(self,region):
        try:
            images = azurerm.list_vm_images_sub(self.access_token, self.subscription)
            array = []

            for image in images['value']:
                if image['location'] != region:
                    continue
                else:
                    #print(image['name'] + ', ' + image['location'] + ', ' + str(
                    #    image['properties']['storageProfile']['osDisk']['diskSizeGB']) + ', ' +
                    #      image['properties']['storageProfile']['osDisk']['storageAccountType'])
                    array2 = []
                    array2.append(image['name'])
                    array2.append(image['location'])
                    array2.append(image['properties']['storageProfile']['osDisk']['diskSizeGB'])
                    array2.append(image['properties']['storageProfile']['osDisk']['storageAccountType'])
                    array2.append(image['id'])
                    array.append(array2)
            return array

        except ValueError:
            print("Fail to get image list")
            return False

    def getVmSize(self,region):
        try:
            # https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/vmSizes?api-version={apiVersion}
            vmsizes = azurerm.do_get(
                "https://management.azure.com/subscriptions/" + self.subscription + "/providers/Microsoft.Compute/locations/" + region + "/vmSizes?api-version=2015-06-15",
                self.access_token)
            array = []
            for vmsize in vmsizes['value']:
                array2 = []
                array2.append(vmsize['memoryInMB'])
                array2.append(vmsize['maxDataDiskCount'])
                array2.append(vmsize['name'])
                array2.append(vmsize['resourceDiskSizeInMB'])
                array2.append(vmsize['osDiskSizeInMB'])
                array2.append(vmsize['numberOfCores'])
                array.append(array2)
            return array
        except ValueError:
            print("Fail to get VmSize for region" + region)
            return  False
    def getDiskType(self,config):
        try:
            array = []
            disktype = config.getData('azure')
            for type in disktype['disktype']:
                array.append(type)
            return array
        except ValueError:
            print("Fail to get list of diskTypes")
            return False
    def getTags(self,config):
        try:
            array = []
            tags = config.getData('azure')
            for tag in tags['tags']:
                array.append(tag)
            return array
        except ValueError:
            print("Fail to get list of diskTypes")
            return False
    def login(self):
        try:
            self.access_token = azurerm.get_access_token(self.tenant, self.appid, self.passwd)
            return True

        except ValueError:
            print("Azure login error")
            return False
    def getOsType(self,config):
        try:
            array = []
            ostypes = config.getData('azure')
            for ostype in ostypes['ostype']:
                array.append(ostype)
            return array
        except ValueError:
            print("Fail to get list of diskTypes")
            return False
    def getAuth(self,config):
        try:
            auth = json.loads(str(config.getData('azure')).replace('\'', '\"'))
            array = []
            array.append(auth['authentication']['user'])
            array.append(auth['authentication']['passwd'])
            return array
        except ValueError:
            print("Fail to get default credentials for virtual machine")
            return  False
    def getDiskCache(self,config):
        try:
            diskcaches = json.loads(str(config.getData('azure')).replace('\'', '\"'))
            array = []
            for diskcache in diskcaches['diskcache']:
                array.append(diskcache)
            return array
        except ValueError:
            print("Fail to get default credentials for virtual machine")
            return  False
    def teste(self,config):
        return  False
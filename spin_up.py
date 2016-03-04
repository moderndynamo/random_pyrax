import pyrax
import pprint

print "What is your username?"
username = raw_input()
print "API Key:"
apikey = raw_input()
print "What datacenter/region do you want to use?"
datacenter = raw_input()

pp = pprint.PrettyPrinter(indent=4)

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_default_region(datacenter)
pyrax.set_credentials(username, apikey)

imgs = pyrax.cloudservers.images.list()
for img in imgs:
    print img.name, " -- ID:", img.id

print "What is the ID of the image you want to spin up from?"
image_name = raw_input()

flvs = pyrax.cloudservers.list_flavors()
for flv in flvs:
    print "Name:", flv.name
    print "  ID:", flv.id
    print "  RAM:", flv.ram
    print "  Disk:", flv.disk
    print "  VCPUs:", flv.vcpus

print "What is the ID of the flavor you want to use?"
flave = raw_input()

print "What should we call this server?"
new_server_name = raw_input()

server = pyrax.cloudservers.servers.create(new_server_name, image_name, flave)

pyrax.utils.wait_for_build(server, verbose="True")

print "ID:", server.id
print "Status:", server.status
print "Admin password:", server.adminPass
print "Networks:", server.networks

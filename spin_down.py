import pyrax
import time
import datetime

def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please enter ")


print "What is your username?"
username = raw_input()
print "API Key:"
apikey = raw_input()
print "What datacenter/region do you want to use?"
datacenter = raw_input()

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_default_region(datacenter)
pyrax.set_credentials(username, apikey)

servers =  pyrax.cloudservers.servers.list()

print "What server do you want to spin down?\n"

for server in servers:
    print server.name, " -- ID:", server.id

srvr = raw_input()
srvrname = pyrax.cloudservers.servers.get(srvr).name

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H%M%S')

imgexec = pyrax.cloudservers.servers.create_image(srvr, srvrname + "-" + st)
image = pyrax.cloudservers.images.get(imgexec)
pyrax.utils.wait_until(image, "status", ["ACTIVE","ERROR"], interval=10, attempts=0, verbose=True, verbose_atts="progress")

qn = yes_or_no("Do you want to delete the server as well?")

if qn == True:
    pyrax.cloudservers.servers.delete(srvr)
    print "Server deletion requested. All done!"
else:
    print "All done! Thanks for playing."


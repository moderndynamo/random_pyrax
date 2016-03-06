import ConfigParser
import pyrax
import time
import datetime

settings = ConfigParser.ConfigParser()
settings.read('.spinconfig')

# set defaults for execution
username = settings.get('credentials', 'RAX_USERNAME')
apikey = settings.get('credentials', 'RAX_API_KEY')
datacenter = settings.get('credentials', 'RAX_REGION')

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_default_region(datacenter)
pyrax.set_credentials(username, apikey)

cs = pyrax.cloudservers

# define spinup() function

def spinup():
	imgs = cs.images.list()
	for img in imgs:
	    print img.name, " -- ID:", img.id

	print "\nWhat is the ID of the image you want to spin up from?\n"
	image_name = raw_input("ID: ")

	flvs = cs.list_flavors()
	for flv in flvs:
	    print "Name:", flv.name
	    print "  ID:", flv.id
	    print "  RAM:", flv.ram
	    print "  Disk:", flv.disk
	    print "  VCPUs:", flv.vcpus

	print "\nWhat is the ID of the flavor you want to use?\n"
	flave = raw_input("Flavor ID: ")

	print "\nWhat should we call this server?\n"
	new_server_name = raw_input("Server name: ")

	server = cs.servers.create(new_server_name, image_name, flave)

	pyrax.utils.wait_for_build(server, verbose="True")

	print "\nID:", server.id
	print "\nStatus:", server.status
	print "\nAdmin password:", server.adminPass
	print "\nNetworks:", server.networks, "\n"

# Define yes or no function. Credit: https://github.com/garrettdreyfus/

def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please enter ")

# Define spindown() function

def spindown():
	servers =  cs.servers.list()

	print "\nWhat is the ID server do you want to spin down?\n"

	for server in servers:
	    print server.name, " -- ID:", server.id

	srvr = raw_input("Server ID: ")
	srvrname = cs.servers.get(srvr).name

	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H%M%S')

	imgexec = cs.servers.create_image(srvr, srvrname + "-" + st)
	image = cs.images.get(imgexec)
	pyrax.utils.wait_until(image, "status", ["ACTIVE","ERROR"], interval=10, attempts=0, verbose=True, verbose_atts="progress")

	qn = yes_or_no("\nDo you want to delete the server as well? ")

	if qn == True:
	    cs.servers.delete(srvr)
	    print "\nServer deletion requested. All done!\n"
	else:
	    print "\nAll done! Thanks for playing.\n"


# begin main procedures

print "\nWhat would you like to do?\n"
print "1) Spin up a server\n"
print "2) Image and spin down a server\n"

usr_input = input("Choice: ")

while usr_input not in [1, 2]:
	usr_input = input("Choice: ")

if usr_input == 1:
	spinup()
elif usr_input == 2:
	spindown()
else:
	sys.exit()


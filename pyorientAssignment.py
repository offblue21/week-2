
import pyorient
import sys

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "1093153B2C895D46C0654EF3C9CCD6EEE2D745CF3ADBB5A1AF8FADB7B0CF817B")
db_name = "soufun"
db_username = "admin"
db_password = "admin"

if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_open( db_name, db_username, db_password )
	print db_name + " opened successfully"
else:
	print "database [" + db_name + "] does not exist! session ending..."
	sys.exit()

lat1 = 22.532498
lat2 = 22.552317

lng1 = 114.044329
lng2 = 114.076644

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'

records = client.command(query.format(lat1, lat2, lng1, lng2))

numListings = len(records)

print 'received ' + str(numListings) + ' records'

# [ANALYZE THE RETURNED RECORDS TO DETERMINE THE MINIMUM, MAXIMUM, AND AVERAGE PRICE OF THE LISTINGS]
# Hint: the loop that you need to look into each record is already provided below.
# To find the average price, add up all the prices and divide by the number of results
# To find the minimum price, create a variable and initialize it to a very large number, 
# then test each price to see if it is smaller than the current minimum. If it is, update 
# the minimum variable with that price. You can do something similar to find the maximum.

sumPrice = 0
minPrice = 10000000000000
maxPrice = 1

for record in records:
	print record.price	
	sumPrice += record.price
	avrPrice = sumPrice/len(records)
	
	if record.price < minPrice:
	    minPrice = record.price
        if record.price > maxPrice:
            maxPrice = record.price
            	  
   
# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

print 'min price: ' + str(minPrice)
print 'max price: ' + str(maxPrice)
print 'average price: ' + str(avrPrice)

client.db_close()
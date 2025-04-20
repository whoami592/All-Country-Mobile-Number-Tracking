import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

# Enter the mobile number you want to hack
mobile_number = input("Enter the mobile number to hack: ")

# Parse the mobile number
parsed_number = phonenumbers.parse(mobile_number, "CH")

# Get the carrier of the mobile number
carrier_name = carrier.name_for_number(parsed_number, "en")

# Get the geolocation of the mobile number
geolocation = geocoder.description_for_number(parsed_number, "en")

# Print the hacked information
print("Hacked Information:")
print("Mobile Number:", mobile_number)
print("Carrier:", carrier_name)
print("Geolocation:", geolocation)
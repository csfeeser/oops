#!/usr/bin/env python3

# Check hostname against expected value
hostname = input("What value should we set for hostname?")

## use the lower method to test if input value matches expected value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches the expected config")

## Always print out to the user
print("Exiting the script")
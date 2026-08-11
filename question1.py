parking=int(input("Enter Parking Hours:"))
if parking > 2:
    parking_charges=30 * parking
elif parking <=5 :
    parking_charges=25 * parking
else :
    parking_charges=20 * parking
if parking_charges > 150:
    service_charge = 20
else:
    service_charge = 0

final_amount = parking_charges + service_charge

print("Parking Charge: ₹", parking_charges)
print("Service Charge: ₹", service_charge)
print("Final Amount: ₹", final_amount)
    
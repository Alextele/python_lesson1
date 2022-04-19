def get_vat (payment, persent=20):
	try:
		payment = float(payment)
		vat = payment/100*persent
		return round(vat,2)
	except TypeError:
		return "Can't count. Check data"
result = get_vat(20,10)
print (result)
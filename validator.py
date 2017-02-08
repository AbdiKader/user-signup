def user_name(user):
	user = user.strip()
	if ' ' not in user:
		return True
	else:
		return False
def password(passw):
	return passw
def password_confirm(passwo):
	return passwo
def validate_pass():
	pass1 = password(passw)
	pass2 = password_confirm(passwo)
	if pass1 == pass2:
		return True
	else:
		return False
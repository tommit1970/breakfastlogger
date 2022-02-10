import bcrypt
import time

password = b'SecretPassword55'

start = time.time()
hashed = bcrypt.hashpw(password,bcrypt.gensalt(rounds=12)).decode()
# rounds=12 by default
end = time.time()

file = 'hashsaver.txt'
fileHandler = open(file, 'w')
fileHandler.write(hashed)
fileHandler.close()

diff = end-start
print(diff)

# print(hashed)

# username = request.form.get('username') # or mail
# username = request.form.get('password').encode('utf-8')

# look user up in DB using username

# The password is hashed differently everytime
# b'$2b$12$0CwI5IDivOVPf3BMX9gQe.YvCoieV6QSsYLTkHaed0dmzY8/Ib.Om'

# b'$2b$12$kQ6A0Allp2jQCHnrg2n0auofdSLpY5NcBj3F2tW313cTysd0Ib/Lu'

# b'$2b$12$BAvTcsIWTS9sswAyKEooSO0pIZz25Zj8upOlqxQRAvpRYJa4phyha'

# bcrypt has a function to compare even though the hash is different

if bcrypt.checkpw(password, hashed.encode()):
	print("It matches")
	# return redirect(url_for('user_profile'))
else:
	print("Din't match")
	# flash("Invalid credetials", "warning")
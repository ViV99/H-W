from datetime import date
import time
import random

users = ["Valera_Asanov", "Vyacheslav_Kopeicev", "Vladimir_Lila", 
"Leonid_Volkanin", "Ulyana_Alekseeva", "Pavel_Egorov", "Pavel_Gein", 
"Mikhail_Volkov", "Alexander_Gein", "Vladimir_Putin", "Maxim_Skurikhin"]
path_main = ["user/", "root/", "python/", "cpp/", "dev/"]
path_folder = [".config/", ".bash/", "script/", "code/", "main/"]

while(True):
	f = open('logs.txt', 'a')
	
	s = random.randint(0, 2)
	serenity = ""
	http = 0
	req_user = users[random.randint(0, len(users) - 1)]
	req_time = random.randint(1, 100)
	if (s == 0):
		serenity = "INFO"
		http = 200 + random.randint(0, 5)
	elif (s == 1):
		serenity = "WARN"
		http = 400 + random.randint(0, 99) % 10 * 10
	else:
		serenity = "ERROR"
		http = 500 + random.randint(0, 99) % 10 * 10
	
	res_path = path_main[random.randint(0, len(path_main) - 1)] + path_folder[random.randint(0, len(path_folder) - 1)]
	f.write(str(date.today()) + " " + serenity + " " + str(http) + " " + req_user 
	+ " " + str(req_time) + " " + res_path + "\n")
	
	f.close()
	time.sleep(10)

import os, time, configparser

config = configparser.ConfigParser()
config.read("config.ini")

db_name = config.get("Credentials", "db_name")
db_user = config.get("Credentials", "db_user") 
db_password = config.get("Credentials", "db_password")
db_host = config.get("Credentials", "db_host")

source = "/home/user/mysql-dump"
dump_dir = source + os.sep + time.strftime("%d.%m.%Y")

if not os.path.exists(dump_dir):
    os.mkdir(dump_dir)

dump_file = time.strftime("%H:%M:%S")
target = dump_dir + os.sep + dump_file + ".sql"

dump_command = f"mysqldump -h {db_host} -u {db_user} {db_name} > {target}"

if os.system(dump_command) == 0:
    print("Success")
else:
    print("Error")


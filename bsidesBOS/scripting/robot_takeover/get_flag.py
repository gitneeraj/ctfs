import requests
import re
import sys

user_agent_re = re.compile("^(User-agent: )(.*)")
loc_re = re.compile("^(Disallow: )(/.*\.txt)")

url = "http://challenge.ctf.games:30095"

flag = {}
while(len(flag.keys()) < 35):
	robots = requests.get(url+"/robots.txt").content.decode('ascii')

	chunks = robots.split("\n\n")
	for chunk in chunks:
		lines = chunk.split("\n")
		user_agent = user_agent_re.match(lines[0])[2]

		for line in lines[1:]:

			try:
				loc = loc_re.match(line)[2]
			except:
				continue

			headers = {
				'User-Agent': user_agent,
			}

			res = requests.get(url+loc, headers=headers).content.decode('ascii')

			if "INDEX" in res:
				flag_index = int(re.match(".* INDEX (\d+).*INDEX (\d+)", res)[1])
				name_index = int(re.match(".* INDEX (\d+).*INDEX (\d+)", res)[2])

				flag[flag_index] = loc[name_index+1]
				sys.stdout.write("".join([v for (k, v) in sorted(flag.items())]))
				sys.stdout.flush()
				sys.stdout.write('\r')
				sys.stdout.flush()

print("WIN!")
print("".join([v for (k, v) in sorted(flag.items())]))
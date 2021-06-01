import random,string

flag = ""
enc_flag = "MmypTSPBJ{q6k_e1s_q1Ld8I}"
random.seed("FINDIT")
for c in enc_flag:
  if c.islower():
	  d = chr(ord(c) - random.randrange(0,26))
	  if d.islower():
	  	flag += d
	  else:
	  	flag += chr(ord(d) + 26)
  elif c.isupper():
	  d = chr(ord(c) - random.randrange(0,26))
	  if d.isupper():
	  	flag += d
	  else:
	  	flag += chr(ord(d) + 26)
  elif c.isdigit():
	  d = chr(ord(c) - random.randrange(0,10))
	  if d.isdigit():
	  	flag += d
	  else:
	  	flag += chr(ord(d) + 10)
  else:
	  flag += c

print(flag)

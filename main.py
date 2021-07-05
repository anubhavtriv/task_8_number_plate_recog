#!/usr/bin/python3
import cgi
import os
import subprocess as sp
print("content-type: text/html")
print()
f=cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "HR 26 BR 9044":
	print('''<pre>
	Car Number: 256 D 259
	Car Model: Nissan Cooper	
	Registration Name: Nikhil Tiwari
    Registration Number: HJk452XXXXXXX
	Registration Date: 27/8/2015
	Fuel Type: Petrol
	Location: Delhi, India
	Vehicle Class: SUV
	Insurance Upto: 26/8/2025
	</pre>''')
elif cmd == "BR 11AD9271":
	print('''<pre>
	Car Number: BR11AD9271
	Car Model: Renault Kwid	
	Registration Name: Ashish Shukla
    Registration Number: KL234H2XXXXXXX
	Registration Date: 7/9/2016
	Fuel Type: Petrol
	Location: Delhi, India
	Vehicle Class: SUV
	Insurance Upto: 6/9/2026
	</pre>''')

elif cmd == "H982 FKL":
	print('''<pre>
	Car Number: SN66 XMZ
	Car Model: Mercedes GLA 250
	Registration Name: Shreyansh Singh
    Registration Number: UIVBN3XXXXXXX
	Registration Date: 20/5/2019
	Fuel Type: Petrol
	Location: Noida Uttar Pradesh, India
	Vehicle Class: SUV
	Insurance Upto: 19/5/2029
	</pre>''')



import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
while True:
	br.open('http://127.0.0.1:8000/polls/1/vote/')

	response = br.response()

	#print response.geturl() # URL of the page we just opened
	#print response.info()   # headers
	#print response.read()   # body
	br.select_form('myform')
	br.form.find_control(name="choice").value = ['1']
	br.submit()
	print 'submitted'

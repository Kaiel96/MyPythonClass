print 'Do you want to go on... an adventure? (yes/no)'
if raw_input() == 'yes': 
	print 'ADVENTURE TIME! CHOOSE YOUR WEAPON!(sword/bow/flail/pizza) '
	if raw_input() == 'sword': 
		print 'With your blade sharpened and your mind prepared, you set out to\
		 the land of Baldurs Gate...Where will you go first? (Beregost/Friendly Arm Inn)'
		if raw_input() == 'Beregost': 
			print 'Cool beans bro'
		else: 
			print 'O_o'
	
	elif raw_input() == 'bow':
		print 'With your Bow and a notched arrow at hand, you head out to the burn land of\
		 Westeros...Which King do you support? (The King of the North: Rob Stark, The King \
		 	of the Iron Islands: Balon Greyjoy, The Bastard King: Joffery Lanister)'
	
	elif raw_input() == 'pizza':
		print '...pizza? Really? Okay then... You encounter a giant. You entice him with \
		pizza. He is unappaled and killed you. srs'
	
	else: 
		print 'You have chosen wisely'
else: 
	print '...well this is awkward... I wanted to adventure with you...'
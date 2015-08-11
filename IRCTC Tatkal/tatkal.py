#!/usr/bin/env python3
#
#
#UNDER CONSTRUCTION#
#
#
#
from selenium import webdriver as wd;

if (__name__ == '__main__'):
	username = 'USERNAME';
	password = 'PASSWORD';
	i = '';
	fromStation = 'NEW DELHI - NDLS';
	toStation = 'DEHRADUN - DDN';
	day = '31';
	month = '07';
	year = '2015';

	fox = wd.Firefox ();
	fox.get ('http://irctc.co.in');

	fox.find_element_by_id ('usernameId').send_keys (username);
	fox.find_element_by_class_name ('loginPassword').send_keys (password);

	print ('Fill in the Captcha and then press y');
	while (not i == 'y'):
		print ('continue? (y / n): ');
		i = input ();

	fox.find_element_by_id ('loginbutton').click ();
	fox.find_element_by_id ('jpform:fromStation').send_keys (fromStation);
	fox.find_element_by_id ('jpform:toStation').send_keys (toStation);
	fox.find_element_by_id ('jpform:journeyDateInputDate').send_keys (day + '-' + month + '-' + year);
	fox.find_element_by_id ('jpform:jpsubmit').click ();

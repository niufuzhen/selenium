import os,sys, time, re
from main.page.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.page.desktop_v3.inbox_message.pe_inbox_message import *
from main.page.desktop_v3.product.pe_product import *
from main.page.desktop_v3.shop.pe_shop import *
from main.page.desktop_v3.people.pe_people import *
from main.page.desktop_v3.index.pe_index import *
from random import randint





class sendMessageActivity():
	#subject = "autotest send message #"
	#messagebody = "42451247624 dbfahbfscxzm hello this is messagebot."
	def __init__(self, driver):
		self.driver = driver
		self.shop = ShopPage(driver)
		self.index = IndexPage(driver)

	#STABLE VERSION
	def send_message(self, driver, count=0):
		subject = "autotest send message #" + str(randint(1,9999))
		messagebody = "Msg#" + str(randint(1,9999)) + ". This is tokopedia QC. Message ID ini cuma ngetes yah, jadi.. link ini harusnya disensor: http://apaya.co.cc www.santai.bloomberg www.lazada.com www.zalora.com www.berniaga.com. link ini harusnya nggak disensor: http://uktplink.com http://laptoprepairnewcastle.com link ini harusnya diabaikan : trx.cvv.cvv 2.000.000"
		self.shop.click_send_message(driver, subject, messagebody)
		time.sleep(2)
		return (subject, messagebody)

	def loop_send_msg(self, message="", loop=1):
		try:
			i = 0
			while i < loop: 
				print("Loop send message #" + str(i+1))
				self.send_message(self.driver, message)
				#self.driver.refresh()
				i = i + 1
		except Exception as inst:
			print("Exception in loop send_msg", inst)

	#check if sent message 
	def is_message_sent(self, driver, total_msg_old, total_msg_new, list_msg_new, subject, msgtext):
		inbox_msg = InboxMessagePage(driver)
		time.sleep(3)
		inbox_msg.select_tab_sent()
		isMessageSent = 0
		diff = (total_msg_new) - (total_msg_old)
		print('diff : ' + str(diff))
		list_diff = (list_msg_new)[0:diff] #shortlist new sent message
		total_list_diff = len(list_diff)
		print('list ID message terkirim:')
		print(list_diff)
		for i in list_diff:
			print('test debug')
			print(i)
			#get subject & message preview to be compared
			subject_preview = inbox_msg.get_message_subject(i)
			content_preview = inbox_msg.get_message_preview(i)
			if (subject) == subject_preview and (msgtext) == content_preview:
				isMessageSent = 1
				break
			else:
				pass
		#endfor
		if isMessageSent==1:
			print('Sent message subject = ' + subject_preview)
			print('Sent message preview = ' + content_preview)
			print('Message was successfully sent')
			return(isMessageSent, total_list_diff, list_diff)
		else:
			print('Message not sent')
			return(isMessageSent, total_list_diff, list_diff)

	#==================FOR UNIT TESTING PURPOSE DO NOT DELETE==============#
	def send_message__bypass(self, driver, count, domain_shop, site):
		subject = "autotest send message #"
		messagebody = "42451247624 dbfahbfscxzm hello this is messagebot."
		shop = ShopPage(driver)
		people = peoplePage(driver)
		index = IndexPage(driver)
		time.sleep(2)
		index.click_my_username_at_panel_left() #masuk halaman people
		user_ID = people.get_people_ID() #ambil userIDnya
		#shop.click_send_message(driver, subject, messagebody)
		shop.domain(site, domain_shop)
		shop.bypass_send_message(user_ID)
		time.sleep(2)
		return (subject, messagebody)


	#======================================================================#

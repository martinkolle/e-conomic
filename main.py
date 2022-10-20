#Support for .env
import os
from dotenv import load_dotenv

import datetime
from dateutil import relativedelta
from pprint import pprint

#own imports for E-Conomic integrations
from factory.Subscriber import Subscriber
from model.SubscriberModel import SubscriberModel
from service.integration.soap.Client import SoapClient

load_dotenv()

# Connect to the Soap setup
soapClient = SoapClient( os.environ.get('ECONOMIC_TOKEN'), os.environ.get('ECONOMIC_APPTOKEN'))

def createSubscriber() :

	# Minimal fields
	DebtorId = 1000
	SubscriptionId = 2
	StartDate = datetime.datetime.now()
	RegisteredDate = datetime.datetime.now()
	EndDate = StartDate + relativedelta.relativedelta(months=1)
	subscriber = Subscriber(DebtorId, SubscriptionId, StartDate, RegisteredDate, EndDate, ExtraTextForInvoice="kagemand")

	# Create a subscriber of a specific subscription
	create = SubscriberModel( soapClient ).create( subscriber )
	pprint( "We have added a subscriber", create.toObject() )


def getSubscriber() :
	subscriberId = 10

	# Get a subscriber
	get = SubscriberModel( soapClient ).get( subscriberId )
	pprint( get.toObject() )


if __name__ == "__main__":
	#createSubscriber()
	getSubscriber()
		
	# Don't remove this line - we need to disconnect to the service
	soapClient.disconnect()
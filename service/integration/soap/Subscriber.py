from lxml import etree
from pprint import pprint
from mapper.SubscriberSoapMapper import SubscriberSoapMapper

##
# Integration to Soap endpoint
##
class SubscriberSoapIntegration(object):

	##
	# @soap 	- Type: SoapClient
	## 
	def __init__(self, soap):
		super(SubscriberSoapIntegration, self).__init__()
		self.soap = soap
		self.mapper = SubscriberSoapMapper( soap )
	
	##
	# Create a Subscriber
	# @Subscriber 	- Type: Subscriber class 
	##
	def create( self, Subscriber ) :
		endpointData = self.mapper.SubscriberToEndpoint( Subscriber )
		result = self.soap.client.service.Subscriber_CreateFromData( endpointData )
		#self.debug()
		
		# Created with success		
		if isinstance(result, int) :
			Subscriber.SubscriberId = result
			return Subscriber

		return result

	##
	# Get a Subscriber
	# @Subscriber 	- Type: int 
	##
	def get( self, SubscriberId ) :
		SubscriberHandle = self.soap.factory.SubscriberHandle( SubscriberId )
		result = self.soap.client.service.Subscriber_GetData( SubscriberHandle )
		self.debug()

		return self.mapper.endpointToSubscriber( result )

	##
	# Debug Soap request before and after 
	# requested to the server
	# 
	def debug( self ) :
		try:
			for hist in [self.soap.history.last_sent, self.soap.history.last_received]:
				print(etree.tostring(hist["envelope"], encoding="unicode", pretty_print=True))
		except (IndexError, TypeError):
			# catch cases where it fails before being put on the wire
			pass
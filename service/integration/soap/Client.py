from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin

from service.integration.soap.Subscriber import SubscriberSoapIntegration

class SoapClient():
	endpointUrl = "https://api.e-conomic.com/secure/api1/EconomicWebService.asmx?wsdl"
	isAuthenticated = None

	def __init__(self, token, appToken ):
		# Endpoint authentication 
		self.token = token
		self.appToken = appToken
		
		self.initClient()

		# Endpoint integrations
		self.subscriber = SubscriberSoapIntegration( self )

	def initClient(self) :
		self.history = HistoryPlugin()
		transport = Transport(cache=SqliteCache())
		self.client = Client( self.endpointUrl, plugins=[self.history], transport=transport )
		self.factory = self.client.type_factory('ns0')
		self.authenticate( self.token, self.appToken)

	def authenticate( self, token, appToken) :
		if self.isAuthenticated is not None :
			print( "authenticated is not none: %s", self.isAuthenticated)
			return True

		print( "Authenticating ...")
		cookie = self.client.service.ConnectWithToken( self.token, self.appToken )
		print( "Authenticated: %s", cookie )

		if cookie :
			self.isAuthenticated = True
			self.cookie = cookie

	def disconnect( self ) :
		self.client.service.Disconnect()
		
from factory.Subscriber import Subscriber

class SubscriberSoapMapper(object):

	def __init__(self, integration):
		self.integration = integration
		
	##
	# Map endpoint result for a subscriber to Subscriber()
	# @endpoint - Type: Soap return request for a Subscriber
	# @todo		- Maybe change to Pyhton Date instead of datestring
	## 
	def endpointToSubscriber( self, endpoint ) :
		DebtorId = endpoint['DebtorHandle']['Number']
		SubscriptionId = endpoint['SubscriptionHandle']['Id']
		StartDate = endpoint['StartDate']
		RegisteredDate = endpoint['RegisteredDate']
		EndDate = endpoint['EndDate']
		SubscriberId = endpoint['SubscriberId']
		ExpiryDate = endpoint['ExpiryDate']
		DiscountExpiryDate = endpoint['DiscountExpiryDate']
		ExtraTextForInvoice = endpoint['ExtraTextForInvoice']
		Comments = endpoint['Comments']
		SpecialPrice = endpoint['SpecialPrice']
		QuantityFactor = endpoint['QuantityFactor']
		PriceIndex = endpoint['PriceIndex']
		DiscountAsPercent = endpoint['DiscountAsPercent']

		return Subscriber(
				DebtorId,
				SubscriptionId,
				StartDate,
				RegisteredDate,
				EndDate,
				SubscriberId,
				ExpiryDate,
				DiscountExpiryDate,
				ExtraTextForInvoice,
				Comments,
				SpecialPrice,
				QuantityFactor,
				PriceIndex,
				DiscountAsPercent
			)

	##
	# Mapper to prepare Subscriber() to Soap endpoint
	## 
	def SubscriberToEndpoint( self, Subscriber ) :

		debtor = self.integration.factory.DebtorHandle( Subscriber.DebtorId )
		subscription = self.integration.factory.SubscriptionHandle( Subscriber.SubscriptionId )

		data = self.integration.factory.SubscriberData(**
			self.noneToDefault(
				SubscriberId=0,
				DebtorHandle=debtor,
				SubscriptionHandle=subscription,
				StartDate=Subscriber.StartDate,
				RegisteredDate=Subscriber.RegisteredDate,
				EndDate=Subscriber.EndDate,
				ExpiryDate=Subscriber.ExpiryDate,
				DiscountExpiryDate=Subscriber.DiscountExpiryDate,
				ExtraTextForInvoice=Subscriber.ExtraTextForInvoice,
				Comments=Subscriber.Comments,
				SpecialPrice=Subscriber.SpecialPrice,
				QuantityFactor=Subscriber.QuantityFactor,
				PriceIndex=Subscriber.PriceIndex,
				DiscountAsPercent=Subscriber.DiscountAsPercent
				)
			)

		return data
	
	##
	# Remove None variables from method arguments
	## 
	def noneToDefault( self, **kwargs ):
		return {k: v for k, v in kwargs.items() if v is not None}
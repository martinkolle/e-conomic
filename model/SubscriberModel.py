from mapper.SubscriberSoapMapper import SubscriberSoapMapper

## 
# Model for a Subscriber
# Current implementation can create and get a
# subscriber from e-conomic api
# 
# The model is an overall model with delegation to a
# integration like soap or rest
##
class SubscriberModel(object):

	def __init__(self, integration):
		super(SubscriberModel, self).__init__()
		self.integration = integration
	
	##
	# Create a Subscriber
	# @Subscriber 	- Type: Subscriber() 
	##
	def create( self, Subscriber ) :
		result = self.integration.subscriber.create( Subscriber )

		return result

	##
	# Get a Subscriber
	# @SubscriberId 	- Type: int
	# 
	def get( self, SubscriberId ) :
		result = self.integration.subscriber.get( SubscriberId )

		return result
class SubscribersFactory :
	def __init__(self, subscribers):
		self.elements = []
		super(Subscribers, self).__init__()

	def add( subscriber ) : 
		self.elements.add( subscriber )

	def remove( index ) : 
		self.elements.remove( index )

	def toArray() :
		return self.elements

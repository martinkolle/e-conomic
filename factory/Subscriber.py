class Subscriber :
	def __init__(self,
		DebtorId,
		SubscriptionId,
		StartDate,
		RegisteredDate,
		EndDate,
		SubscriberId = 0,
		ExpiryDate = None,
		DiscountExpiryDate = None,
		ExtraTextForInvoice = None,
		Comments = None,
		SpecialPrice = None,
		QuantityFactor = None,
		PriceIndex = None,
		DiscountAsPercent = None) :

		self.SubscriberId = SubscriberId
		self.DebtorId = DebtorId
		self.SubscriptionId = SubscriptionId
		self.StartDate = StartDate
		self.RegisteredDate = RegisteredDate
		self.EndDate = EndDate
		self.ExpiryDate = ExpiryDate
		self.DiscountExpiryDate = DiscountExpiryDate
		self.ExtraTextForInvoice = ExtraTextForInvoice
		self.Comments = Comments
		self.SpecialPrice = SpecialPrice
		self.QuantityFactor = QuantityFactor
		self.PriceIndex = PriceIndex
		self.DiscountAsPercent = DiscountAsPercent

	##
	# Easy way to debug data
	# 
	def toObject(self) :
		return {
			"DebtorId" : self.DebtorId,
			"SubscriptionId" : self.SubscriptionId,
			"StartDate" : self.StartDate,
			"RegisteredDate" : self.RegisteredDate,
			"EndDate" : self.EndDate,
			"SubscriberId" : self.SubscriberId,
			"ExpiryDate": self.ExpiryDate,
			"DiscountExpiryDate": self.DiscountExpiryDate,
			"ExtraTextForInvoice": self.ExtraTextForInvoice,
			"Comments": self.Comments,
			"SpecialPrice": self.SpecialPrice,
			"QuantityFactor": self.QuantityFactor,
			"PriceIndex": self.PriceIndex,
			"DiscountAsPercent": self.DiscountAsPercent
		}
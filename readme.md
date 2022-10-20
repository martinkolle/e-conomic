# Python integration to e-conomic.com 

## Setup
1. Duplicate `.env.template` and change to `.env`
2. Insert `token` and `appToken`

## Where to find e-conomic tokens?
1. Sign up as [E-conomic Developer](https://www.e-conomic.com/developer)
2. Create an E-conomic app (it is not needed to be approved)
3. Use the authentication link when logged into your normal e-conomic account
4. On redirect - you get the token in GET request

## Authentication and init
````python
soapClient = SoapClient( os.environ.get('ECONOMIC_TOKEN'), os.environ.get('ECONOMIC_APPTOKEN') )
````

## Endpoint integrations

### Subscriber
| Field | Type | Required | Description |
|--|--|--|--|
| DebtorId | Number | `Required` | Customer id |
| SubscriptionId | Number | `Required` | The subscription |
| StartDate | DateTime | `Required` | Start date of the Subscriber |
| RegisteredDate | DateTime | `Required` | Date of the creation of the subscriber |
| EndDate | DateTime | `Required` | Renewal date |
| SubscriberId | Number | `optional` | Current Subscriber ID |
| ExpiryDate | DateTime | `optional` | Date where the Subscriber should expire |
| DiscountExpiryDate | DateTime | `optional` | Date where discount price expire |
| ExtraTextForInvoice | DateTime | `optional` | Extra line text |
| Comments | Text | `optional` | Own comments text in backend |
| SpecialPrice | Number | `optional` | Discount price |
| QuantityFactor | Number | `optional` | Quantity of products per Invoice |
| PriceIndex | Number | `optional` | XX |
| DiscountAsPercent | Number | `optional` | Instead of Special price add a percent discount |

`GET` /Subscriber

```python
subscriberId = 10
get = SubscriberModel( soapClient ).get( subscriberId )
pprint( get.toObject() )
```

`POST` /Subscriber
It is possible to use all fields above

````python
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
````

### Subscriber
|asda	dasas  |asdasd  |
|--|--|
|  |  |

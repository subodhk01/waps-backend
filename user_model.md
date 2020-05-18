# User Model




## Predefined Django User Model Fields
- First Name 
- Last Name
- Email
- Username
- Password


## More Fields

- City = CharField
- Pincode = IntegerField
- Mobile Number= CharField
- Keywords = onetomanyField(keyword model)
- Favourite Books = onetomany(book model)
- Profile Picture = ImageField

## More info about the user

- We can get the books user owns thorough the reverse relation to OWNER FIELD(ForeingKey) used in Book Model
- We can get the books user rented thorough the reverse relation to RENTED_BY FIELD(ForeingKey) used in Book Model 
-

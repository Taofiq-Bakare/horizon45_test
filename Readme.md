## Tasks

### Required

- [ ] Create a GitHub repo and invite sedia.jaiteh@horizons45.com. Your Github repo should contain the whole project with the truck application and basic server settings. Make sure the local server can be spun up without any errors. (You don't need to commit the local database .sqlite to the repo).
- [x] Design one or more models to store driver information in the database. (Note: You may need multiple models and use database relationships such as one-to-one, one-to-many, etc.). Each driver has the following fields or attributes:

    - [x] name
    - [x] mobile_number
    - [x] email
    - [x] city
    - [x] district
    - [x] language
    - [x] an_asigned_truck (each truck has a unique number_plate and a unique registration_number)

- [ ] API endpoints and expected responses:
  - [x] /domain/driver
    * Return a list of available drivers.
    * Allow filtering using a driver's email, mobile_number, language, and assigned truck number_plate.
  - [x] /domain/driver/id
    * Return a single driver
  - [x] /domain/driver
    * create a single driver



### Extras

- [ ] Creating bulk drivers
- [ ] Unit tests
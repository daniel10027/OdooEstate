# OdooEstate

# Estate Module

The Estate module is designed to manage properties within your real estate agency. It allows you to track property details, sales, and availability.

## Features

- Manage property listings with details such as name, description, postcode, and availability date.
- Track expected and selling prices for properties.
- Record property attributes like number of bedrooms, living area, and number of facades.
- Option to indicate if a property has a garage, garden, and garden area.
- Ability to assign a salesman to each property.
- Capture the last seen date for each property.
- Compute the total area of each property based on living area and garden area.
- Status management for properties including new, offer received, offer accepted, sold, and canceled.
- Actions to mark properties as sold or canceled, with appropriate validations.

## Installation

1. Copy the `estate` folder into your Odoo addons directory.
2. Restart the Odoo server.
3. Install the `Estate` module from the Apps menu in Odoo.

## Usage

1. After installation, navigate to the `Estate Application` menu in Odoo.
2. Under `Master Data`, you can access the list of properties.
3. From the property list view, you can search, filter, and sort properties based on various criteria.
4. Click on a property to view its details, update information, or perform actions like marking it as sold or canceled.

## Security

- Access to the Estate module is controlled through the `access_estate_property` group.
- Users with access to this group can read, write, create, and delete property records.

## Credits

- Author: Daniel Guedegbe
- Version: 1.0

## License

This module is open-source and licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.



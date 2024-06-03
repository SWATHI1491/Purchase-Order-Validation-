#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


import pandas as pd

# Sample data
purchase_orders = [
    {
        "po_number": "PO12345",
        "item_code": "ITEM001",
        "supplier_id": "SUPP001",
        "quantity": 100,
        "price_per_unit": 10.50
    },
    {
        "po_number": "PO12346",
        "item_code": "ITEM002",
        "supplier_id": "SUPP002",
        "quantity": 10,
        "price_per_unit": 5.00
    }
]

product_catalog = {
    "ITEM001": {"name": "Item 1", "min_price": 10, "max_price": 20},
    "ITEM002": {"name": "Item 2", "min_price": 5, "max_price": 15},
}

suppliers = ["SUPP001", "SUPP002", "SUPP003"]

# Convert purchase orders to DataFrame
po_df = pd.DataFrame(purchase_orders)

# Convert product catalog to DataFrame
product_catalog_df = pd.DataFrame.from_dict(product_catalog, orient='index').reset_index()
product_catalog_df.columns = ['item_code', 'name', 'min_price', 'max_price']

# Convert suppliers to DataFrame
suppliers_df = pd.DataFrame(suppliers, columns=['supplier_id'])

# Display the tables
print("Purchase Orders:")
print(po_df)
print("\nProduct Catalog:")
print(product_catalog_df)
print("\nSuppliers:")
print(suppliers_df)


# In[3]:


def validate_purchase_order(po, product_catalog, suppliers):
    errors = []
    
    # Check if item code exists in the product catalog
    if po["item_code"] not in product_catalog:
        errors.append(f"Invalid item code: {po['item_code']}")
        
    # Check if supplier ID is valid
    if po["supplier_id"] not in suppliers:
        errors.append(f"Invalid supplier ID: {po['supplier_id']}")
        
    # Check if quantity is positive
    if po["quantity"] <= 0:
        errors.append(f"Invalid quantity: {po['quantity']}")
        
    # Check if price per unit is within the valid range
    if po["item_code"] in product_catalog:
        item = product_catalog[po["item_code"]]
        if not (item["min_price"] <= po["price_per_unit"] <= item["max_price"]):
            errors.append(f"Invalid price: {po['price_per_unit']} for item {po['item_code']}")
    
    return errors

# Function to validate a list of purchase orders
def validate_purchase_orders(purchase_orders, product_catalog, suppliers):
    for po in purchase_orders:
        errors = validate_purchase_order(po, product_catalog, suppliers)
        if errors:
            print(f"Errors in PO {po['po_number']}: {errors}")
        else:
            print(f"PO {po['po_number']} is valid.")

# Validate sample purchase orders
validate_purchase_orders(purchase_orders, product_catalog, suppliers)


# In[ ]:





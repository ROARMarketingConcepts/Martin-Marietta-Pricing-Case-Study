# Martin Marietta Pricing Analysis Exercise

**Overview:** We are provided with a dataset containing sales transactions for 2022. Each record represents a shipment of a construction material product to a customer. Our task is to analyze the dataset and derive pricing insights based solely on the available variables.

**Objective:** Using the provided dataset, derive an optimal price range (floor, middle, and ceiling) for each customer-product-region segment based on the observable patterns in the data.

**Dataset Structure:**

* `shipment_month`: Month of the transaction (e.g., Jan, Feb, etc.)
* `region`: Anonymized regional code (e.g., Region A, Region B, etc.)
* `product_category`: Broad category of the product
* `product_id`: Unique identifier for the product
* `customer_id`: Unique identifier for the customer
* `transfer_flag`: indicates if the shipment is plant to plant transfer or shipment to External customer.
* `pickup_or_delivery`: Indicates whether it was picked up by the customer or delivered
* `Job_distance`: Approximate delivery distance bucket (e.g., 0–5, 5-10, 10-15 miles)
* `Shipment_qty`: Quantity of products shipped (in tons)
* `avg_price_per_ton`: Average price per ton (this is the target variable)
  
**Deliverables (within 90-120 minutes):**

* Brief exploratory summary identifying key factors that appear to drive price variation.
* A proposed logic or simple model (e.g., segmentation, CHAID-style tree) that defines pricing bands.
* Example pricing bands (floor, middle, ceiling) for 2–3 segments of your choice.
* A short-written summary / verbal explanation outlining your assumptions, approach, and conclusions.

**Note:** Focus strictly on patterns in the data. If a hands-on environment is unavailable, be prepared to walk through your analytical approach step-by-step.

**Stretch Goal (Optional):** Suggest how your pricing approach might be deployed or scaled in a production setting.

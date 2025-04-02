# biden-foreign-awards-analysis
Analyzed federal contracts from the Biden administration’s lame duck period, identifying 26 foreign awards to undisclosed recipients with over $3.7M in unspent funds. Focused on delivery and purchase orders to flag potentially cancellable, opaque obligations.
---

## 📊 Dataset Source

Filtered directly from [USAspending.gov](https://www.usaspending.gov) using:

- **Time Period:** Nov 6, 2024 – Jan 19, 2025  
- **Place of Performance:** All Foreign Countries  
- **Award Types:**  
  - Delivery Orders (DO)  
  - Purchase Orders (PO)  
  - Definitive Contracts  
  - Blanket Purchase Agreements (BPA)  
  - Basic Ordering Agreements (BOA)  
  - Indefinite Delivery / Definite Quantity Contracts  
  - Indefinite Delivery / Indefinite Quantity (IDIQ) Contracts  

📎 Raw data download (~43MB): [Download ZIP from USAspending](https://files.usaspending.gov/generated_downloads/PrimeAwardSummariesAndSubawards_2025-04-01_H22M09S23335138.zip ))

Full Description: 
Potentially Cancellable Contracts Logic

During the Biden administration’s lame duck period (November 6, 2024, to January 19, 2025), an analysis of federal contracts was conducted to identify potentially cancellable spending commitments. Data was sourced from USAspending.gov and filtered for new awards designated for performance in foreign countries, with a focus on contract types such as delivery orders and purchase orders, while grants and loans were excluded. This distinction was made because delivery and purchase orders are tied to tangible goods and services, with clear obligation and performance terms, making them more traceable and legally reversible—particularly when funds have not yet been outlayed. In contrast, grants are often fully disbursed upfront and difficult to claw back, while loans typically involve repayment structures and are tracked separately. The filtered dataset was exported as a CSV and loaded into Cursor, where Python was used to calculate the unspent amount on each contract by subtracting total outlays from total obligations. Awards were further filtered to include only those where the recipient name contained “undisclosed,” signaling potential anonymity or classification. This process resulted in the identification of 26 foreign contracts issued during the transition period to anonymous recipients, each with significant unspent funds—highlighting awards that are politically sensitive, lack transparency, and may be subject to cancellation or reallocation. The total unspent amount identified exceeds $3.7 million.

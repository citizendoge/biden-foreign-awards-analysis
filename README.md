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
Full Description: Potentially Cancellable Contracts Logic
During the Biden administration’s lame duck period (November 6, 2024, to January 19, 2025), we conducted an analysis of federal contracts to identify potentially cancellable spending commitments. Using USAspending.gov, we filtered for new awards designated for performance in foreign countries, focusing specifically on contract types such as delivery orders and purchase orders, while excluding grants and loans. We made this distinction because delivery and purchase orders are tied to tangible goods and services, with clear obligation and performance terms, making them more traceable and legally reversible—particularly if funds haven’t been outlayed. In contrast, grants are often fully disbursed upfront and harder to claw back, and loans typically involve repayment structures and are tracked differently. After exporting the filtered dataset as a CSV and loading it into Cursor, we used Python to calculate the unspent amount on each contract by subtracting total outlays from total obligations. We then narrowed our focus to awards where the recipient name contained “undisclosed,” signaling potential anonymity or classification. This led to the identification of 26 foreign contracts awarded during the transition period to anonymous recipients, with significant unspent funds—highlighting them as politically sensitive, lacking transparency, and potentially subject to cancellation or reallocation. Totaling over $3.7m. 

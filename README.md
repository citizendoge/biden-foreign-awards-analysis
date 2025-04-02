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

During the Biden administration’s lame duck period (November 6, 2024, to January 19, 2025), I set out to identify federal contracts that could realistically be cancelled or clawed back. Using data from USAspending.gov, I filtered for new awards set to be performed overseas and narrowed in on contract types like delivery and purchase orders—excluding grants and loans. These types of contracts are tied to specific goods or services and usually have clearer obligations, which makes them easier to track and unwind if needed. Grants, on the other hand, are often paid upfront and harder to reverse, and loans operate under completely different terms. After exporting the dataset and loading it into Cursor, I used Python to calculate the unspent amount on each contract (obligated minus outlayed), then focused on awards with recipients listed as “undisclosed.” That final filter surfaced 26 foreign contracts issued during the transition period with over $3.7 million in unspent funds—each flagged for its lack of transparency and potential reversibility under a new administration.

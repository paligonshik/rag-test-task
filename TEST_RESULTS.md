# Test Results

Q1: List all clients with their industries.

Here is the list of all clients with their industries:

- Acme Corp – Manufacturing  
- Bright Legal – Legal  
- Summit Finance – Financial Services  
- GreenField Retail – Retail  
- Northwind Logistics – Logistics  
- BlueSky Consulting – Consulting  
- Nova Health – Healthcare  
- Urban Tech – Technology  
- RedRock Energy – Energy  
- Silverline Media – Media  
- Zenith Education – Education  
- Alpine Hospitality – Hospitality  
- Orion Security – Security  
- Pacific Foods – Food & Beverage  
- Metro Transport – Transportation  
- Vertex Analytics – Technology  
- Harbor Insurance – Insurance  
- Crescent Pharma – Pharmaceuticals  
- Aurora Textiles – Manufacturing  
- Prairie Agriculture – Agriculture

Q2: Which clients are based in the UK?

The clients based in the UK are:

- Bright Legal  
- Silverline Media

Q3: List all invoices issued in March 2024 with their statuses.

In March 2024, there were 2 invoices issued, and both have been paid:

- Invoice **I1003** issued on **2024-03-05** – **Paid**
- Invoice **I1004** issued on **2024-03-20** – **Paid**

Q4: Which invoices are currently marked as "Overdue"?

The invoices currently marked as **"Overdue"** are:

- Invoice **I1002** for client **C002** (invoice date: 2024-02-15, due date: 2024-03-15, currency: EUR, FX rate to USD: 1.10)  
- Invoice **I1005** for client **C004** (invoice date: 2024-04-01, due date: 2024-05-01, currency: EUR, FX rate to USD: 1.09)  
- Invoice **I1009** for client **C008** (invoice date: 2024-06-01, due date: 2024-07-01, currency: EUR, FX rate to USD: 1.12)  
- Invoice **I1013** for client **C012** (invoice date: 2024-07-20, due date: 2024-08-19, currency: CHF, FX rate to USD: 1.12)  
- Invoice **I1015** for client **C014** (invoice date: 2024-08-10, due date: 2024-09-09, currency: NZD, FX rate to USD: 0.62)  
- Invoice **I1020** for client **C019** (invoice date: 2024-10-01, due date: 2024-10-31, currency: EUR, FX rate to USD: 1.07)  
- Invoice **I1028** for client **C007** (invoice date: 2024-11-15, due date: 2024-12-15, currency: USD, FX rate to USD: 1.00)  
- Invoice **I1032** for client **C011** (invoice date: 2024-12-05, due date: 2025-01-04, currency: USD, FX rate to USD: 1.00)  
- Invoice **I1038** for client **C017** (invoice date: 2024-12-26, due date: 2025-01-25, currency: USD, FX rate to USD: 1.00)

Q5: For each service_name in InvoiceLineItems, how many line items are there?

There are the following numbers of line items for each `service_name` in `InvoiceLineItems`:

- Contract Review: 11 line items  
- Court Appearance: 13 line items  
- Custom Reporting: 11 line items  
- IT Security Assessment: 14 line items  
- M&A Advisory: 16 line items  
- Regulatory Compliance Audit: 10 line items  
- Tax Planning: 14 line items  
- Training Session: 7 line items

Q6: List all invoices for Acme Corp with their invoice IDs, invoice dates, due dates, and statuses.

Here are all the invoices for **Acme Corp** along with their invoice IDs, invoice dates, due dates, and statuses:

- **Invoice ID:** I1001  
  - Invoice Date: 2024-01-10  
  - Due Date: 2024-02-10  
  - Status: Paid  

- **Invoice ID:** I1004  
  - Invoice Date: 2024-03-20  
  - Due Date: 2024-04-20  
  - Status: Paid  

- **Invoice ID:** I1022  
  - Invoice Date: 2024-10-15  
  - Due Date: 2024-11-14  
  - Status: Paid

Q7: Show all invoices issued to Bright Legal in February 2024, including their status and currency.

There was 1 invoice issued to Bright Legal in February 2024:

- Invoice ID: I1002  
  - Date: 2024-02-15  
  - Status: Overdue  
  - Currency: EUR

Q8: For invoice I1001, list all line items with service name, quantity, unit price, tax rate, and compute the line total (including tax) for each.

For invoice **I1001**, there are 3 line items. Here are the details, including the line total with tax:

1. **Court Appearance**  
   - Quantity: **1**  
   - Unit price: **$500.00**  
   - Tax rate: **20.00%**  
   - Line total (including tax): **$600.00**

2. **M&A Advisory**  
   - Quantity: **2**  
   - Unit price: **$200.00**  
   - Tax rate: **0.00%**  
   - Line total (including tax): **$400.00**

3. **Court Appearance**  
   - Quantity: **5**  
   - Unit price: **$300.00**  
   - Tax rate: **0.00%**  
   - Line total (including tax): **$1,500.00**

Q9: For each client, compute the total amount billed in 2024 (including tax) across all their invoices.

Each client’s total amount billed in 2024 (including tax) is:

- Acme Corp: **$6,830.00**
- Vertex Analytics: **$6,106.00**
- BlueSky Consulting: **$5,757.50**
- RedRock Energy: **$5,506.00**
- Zenith Education: **$5,407.50**
- Aurora Textiles: **$5,104.00**
- Orion Security: **$4,062.50**
- Silverline Media: **$3,830.00**
- Nova Health: **$3,696.00**
- Bright Legal: **$3,590.00**
- Harbor Insurance: **$3,487.50**
- Alpine Hospitality: **$3,398.50**
- Metro Transport: **$3,310.00**
- GreenField Retail: **$3,287.50**
- Urban Tech: **$2,632.00**
- Summit Finance: **$2,582.00**
- Northwind Logistics: **$2,426.50**
- Crescent Pharma: **$2,401.50**
- Prairie Agriculture: **$2,051.50**
- Pacific Foods: **$2,037.50**

Q10: Which client has the highest total billed amount in 2024, and what is that total?

The client with the highest total billed amount in 2024 is **Acme Corp**, with a total billed amount of **$6,830.00**.

Q11: Across all clients, which three services generated the most revenue in 2024? Show the total revenue per service.

Across all clients in 2024, the three services that generated the most revenue were:

- **Court Appearance**: **$12,133.50**
- **M&A Advisory**: **$11,961.50**
- **Tax Planning**: **$11,743.50**

Q12: Which invoices are overdue as of 2024-12-31? List invoice ID, client name, invoice_date, due_date, and status.

As of 2024-12-31, the following invoices are overdue:

- **Invoice ID:** I1002  
  - Client: Bright Legal  
  - Invoice Date: 2024-02-15  
  - Due Date: 2024-03-15  
  - Status: Overdue  

- **Invoice ID:** I1005  
  - Client: GreenField Retail  
  - Invoice Date: 2024-04-01  
  - Due Date: 2024-05-01  
  - Status: Overdue  

- **Invoice ID:** I1028  
  - Client: Nova Health  
  - Invoice Date: 2024-11-15  
  - Due Date: 2024-12-15  
  - Status: Overdue  

- **Invoice ID:** I1009  
  - Client: Urban Tech  
  - Invoice Date: 2024-06-01  
  - Due Date: 2024-07-01  
  - Status: Overdue  

- **Invoice ID:** I1013  
  - Client: Alpine Hospitality  
  - Invoice Date: 2024-07-20  
  - Due Date: 2024-08-19  
  - Status: Overdue  

- **Invoice ID:** I1015  
  - Client: Pacific Foods  
  - Invoice Date: 2024-08-10  
  - Due Date: 2024-09-09  
  - Status: Overdue  

- **Invoice ID:** I1020  
  - Client: Aurora Textiles  
  - Invoice Date: 2024-10-01  
  - Due Date: 2024-10-31  
  - Status: Overdue

Q13: Group revenue by client country: for each country, compute the total billed amount in 2024 (including tax).

In 2024, total billed revenue (including tax) by client country is as follows:

- USA: **$22,003.00**
- UK: **$7,420.00**
- Ireland: **$6,106.00**
- Australia: **$5,757.50**
- Norway: **$5,506.00**
- Portugal: **$5,104.00**
- France: **$4,062.50**
- Switzerland: **$3,398.50**
- Spain: **$3,310.00**
- Germany: **$3,287.50**
- Netherlands: **$2,632.00**
- Canada: **$2,426.50**
- India: **$2,401.50**
- Brazil: **$2,051.50**
- New Zealand: **$2,037.50**

Q14: For the service “Contract Review”, list all clients who purchased it and the total amount they paid for that service (including tax).

For the service **“Contract Review”**, the following clients purchased it and these are the total amounts they paid (including tax):

- Aurora Textiles – **$2,200.00**
- Orion Security – **$1,812.50**
- BlueSky Consulting – **$907.50**
- Pacific Foods – **$800.00**
- Summit Finance – **$600.00**
- Zenith Education – **$600.00**
- Nova Health – **$360.00**
- Bright Legal – **$220.00**
- Silverline Media – **$220.00**
- Prairie Agriculture – **$181.50**

Q15: Considering only European clients, what are the top 3 services by total revenue (including tax) in H2 2024 (2024-07-01 to 2024-12-31)?

The top 3 services by total revenue (including tax) from European clients in H2 2024 (2024-07-01 to 2024-12-31) are:

1. **Tax Planning** – **$7,360.00**
2. **Regulatory Compliance Audit** – **$4,486.00**
3. **Contract Review** – **$4,232.50**
